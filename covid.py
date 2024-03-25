import os
import shutil #provee funciones que dan soporte a la copia y remoción de archivos.
import random
import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


##################################################
#   Preparando Datasets y Dataloaders
##################################################
print("\n####################### Cargando Datasets ######################")
# Clase contenedora de nuestro conjunto de datos
class ChestXRayDataset(Dataset):
    #Cargamos y alamcenamos el conjunto de datos.
    def __init__(self, image_dirs, transform):
        
        #Devuelve un arreglo con el nombre de cada imagen.
        def get_images(class_name): 
            images = [x for x in os.listdir(image_dirs[class_name]) if x[-3:].lower().endswith('png')]  #Obtenemos el nombre de cada imagen
            print(f'Ejemplos {len(images)} {class_name} encontrados')
            return images
        
        
        self.images = {} #Diccionario  de la forma ----> {clase1: [nombreImg1, nombreImg2,...], ...}, 
        self.class_names = ['normal', 'viral', 'covid'] #Tipos de clases
        for class_name in self.class_names:
            self.images[class_name] = get_images(class_name)
            
        self.image_dirs = image_dirs #Diccionario de la forma----> {clase1: path, ...}
        self.transform = transform
        
    # Devuelve el tamaño del conjunto de datos.
    def __len__(self):
        # Devuelve el numero de imagens que hay en el diccionario "self.images"
        return sum([len(self.images[class_name]) for class_name in self.class_names]) 
    
    # Devuelve un elemento de nuestro conjunto de datos
    def __getitem__(self, index):
        class_name = random.choice(self.class_names) #Aleatoriamente seleccionamos una clase
        index = index % len(self.images[class_name]) #Prevenimos que no se elija un indice no valido
        image_name = self.images[class_name][index] #Seleciona el nombre de la imagen
        image_path = os.path.join(self.image_dirs[class_name], image_name) #seleccionamos la imagen
        image = Image.open(image_path).convert('RGB') #Abrimos la imagen con pillow en modo rgb
        return self.transform(image), self.class_names.index(class_name) #Devolvemos [imagenTratada, la clase] 



# conjunto de entrenamiento: Redimencionamos, Alatoriamente giramos, convertimos en tensor, y normalizamos
train_transform = torchvision.transforms.Compose([
    torchvision.transforms.Resize(size=(224, 224)),
    torchvision.transforms.RandomHorizontalFlip(),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# conjunto de prueva: Redimencionamos,  convertimos en tensor, y normalizamos
test_transform = torchvision.transforms.Compose([
    torchvision.transforms.Resize(size=(224, 224)),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])


train_dirs = {
    'normal': 'Radiography/normal',
    'viral': 'Radiography/viral',
    'covid': 'Radiography/covid'
}
test_dirs = {
    'normal': 'Radiography/test/normal',
    'viral': 'Radiography/test/viral',
    'covid': 'Radiography/test/covid'
}

print("#### Conjunto de Entrenamiento ####")
train_dataset = ChestXRayDataset(train_dirs, train_transform)
print("######## Conjunto de Prueva #######")
test_dataset = ChestXRayDataset(test_dirs, test_transform)

batch_size = 6

# DataLoader
dl_train = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
dl_test = DataLoader(test_dataset, batch_size=batch_size, shuffle=True)
class_names = train_dataset.class_names

print('Número de lotes de entrenamiento', len(dl_train))
print('Número de lotes de prueba', len(dl_test))


##################################################
#   Creando el modelo
##################################################

resnet18 = torchvision.models.resnet18(pretrained=True) # Usamos el modelo resnet18, ya preentrenado

resnet18.fc = torch.nn.Linear(in_features=512, out_features=3) #Fully conected layer

loss_fn = torch.nn.CrossEntropyLoss() #Funcion de pertida 

optimizer = torch.optim.Adam(resnet18.parameters(), lr=3e-5) #Algirtmo de optimizacion, Forma en la que se actualizan los pesos sinapticos



##################################################
#   Visualizacion de predicciones
##################################################
from matplotlib import pylab

def show_images(images, labels, preds, title):
    plt.figure(figsize=(8, 4)).canvas.manager.set_window_title(title)
    for i, image in enumerate(images):
        plt.subplot(2, 6, i + 1, xticks=[], yticks=[])
        if(i==1):
            plt.title("Estado del modelo: "+title+'\n', fontsize='20')
        
        image = image.numpy().transpose((1, 2, 0))
        mean = np.array([0.485, 0.456, 0.406])
        std = np.array([0.229, 0.224, 0.225])
        image = image * std + mean
        image = np.clip(image, 0., 1.)
        plt.imshow(image)
        col = 'green'
        msg= 'ACERTO !!'
        if preds[i] != labels[i]:
            col = 'red'
            msg="FALLO"

        plt.xlabel(f'y: {class_names[int(labels[i].numpy())]}\n' + msg, color = col)
        plt.ylabel(f'ŷ: {class_names[int(preds[i].numpy())]}',color=col)

    
    plt.tight_layout()
    plt.show()


def show_preds(title= "Modelo de Entrenamiento"): 
    resnet18.eval()  #Modo evaluaar modelo
    images, labels = next(iter(dl_test))   # Nos devuelve un lote de imagenes
    outputs = resnet18(images) #Evaluamos lote de imagnes
    _, preds = torch.max(outputs, 1) #Obtenemos la prediccion del lote
    show_images(images, labels, preds,title) # Mostramos las imagenes
show_preds("Modelo NO entrenado")


##################################################
#   Entrenando el modelo
##################################################
print("\n####################### Entrenando Modelo ######################")
def train(epochs):
    for e in range(0, epochs): #Por cada epoca
        train_loss = 0.
        val_loss = 0.

        resnet18.train() #Modo entrenamiento

        for train_step, (images, labels) in enumerate(dl_train): #Por cada lote del dataloader de entrenamiento
            
            optimizer.zero_grad() #Ponemos a zero los gradientes.

            outputs = resnet18(images) #Evaluamos las imagenes con el modelo
            loss = loss_fn(outputs, labels) #Calculamos la funcion de perdida. Esto devuelve un tensor.
            loss.backward() #Propagacion hacia atras.
            optimizer.step() #Actualizamos los parametros/pesos
            train_loss += loss.item() #actualizamos el error en el conjunto de datos de entrenamiento

            # Cada 20 lotes, verificamos la precision del modelo con el dataset de entrenamiento
            if train_step % 20 == 0:
                accuracy = 0
                resnet18.eval()  # Modo de evaluacion del modelo

                for val_step, (images, labels) in enumerate(dl_test):
                    outputs = resnet18(images)
                    loss = loss_fn(outputs, labels)
                    val_loss += loss.item() #Actualizamos el error en el conjunto de datos de prueva
                    _, preds = torch.max(outputs, 1)
                    accuracy += sum((preds == labels).numpy())  # Calculamos la precision del modelo con el lote

                
                val_loss /= (val_step + 1)
                accuracy = accuracy/len(test_dataset)
                print(f'Pérdida de validación: {val_loss:.4f}, Precisión: {accuracy:.4f}')


                resnet18.train() # Modo entrenamiento

                if accuracy >= 0.95: #Detenmos si alcanza la precision deseada.
                    print('Condición de rendimiento satisfecha, deteniéndose ...')
                    return accuracy

        train_loss /= (train_step + 1) # Ajustamos la funcion de perdida

        print(f'Pérdida de entrenamiento: {train_loss:.4f}')
    print('Entrenamiento completo ...')


accuracy = train(epochs=1)
print("\n####################### Modelo Entrenado ########################")
#print("accuracy: ", accuracy)
#show_preds("Trained Model, Accuracy " + str(round(accuracy,4)*100) + "%")


##################################################
#   Guardando el modelo
##################################################
PATH_OUTPUT = "resnet/modelV2.pt"
torch.save(resnet18.state_dict(), PATH_OUTPUT)