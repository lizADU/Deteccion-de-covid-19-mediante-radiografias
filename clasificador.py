import os
import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
from PIL import Image
#import numpy as np
#from matplotlib import image, pyplot as plt
#from matplotlib import pylab

# Clase contenedora de nuestro conjunto de datos
class XRayDataset(Dataset):
    #Cargamos y almacenamos el conjunto de datos.
    def __init__(self, path, transform):
       self.list_imgs = [x for x in os.listdir(path) if x[-3:].lower().endswith('png')] #Solo acepta pngs por el momento
       self.transform = transform
       self.path = path
        
    # Devuelve el tamaño del conjunto de datos.
    def __len__(self):
        return len(self.list_imgs)
    
    # Devuelve un elemento de nuestro conjunto de datos
    def __getitem__(self, index):
        index = index % len(self.list_imgs) #Prevenimos que no se elija un indice no valido
        path_img = self.path+self.list_imgs[index]
        image = Image.open(path_img).convert('RGB') #Abrimos la imagen con pillow en modo rgb
        return self.transform(image), self.list_imgs[index]
        

# Clasificador
class Clasificador():
    clasificacion = ['normal', 'viral', 'covid']
    
    def __init__(self,path_model= "resnet/modelV2.pt" ):
        self.path_model = path_model
        self.loadModel() #Cargamos el modelo

    def loadModel(self):
        self.resnet18 = torchvision.models.resnet18(pretrained=True)
        self.resnet18.fc = torch.nn.Linear(in_features=512, out_features=3)
        self.resnet18.load_state_dict(torch.load(self.path_model))

    def loadData(self, pathImages = "resnet_uploads/", batch_size=6):
        # Transform over image: Redimencionamos,  convertimos en tensor, y normalizamos
        transform = torchvision.transforms.Compose([
            torchvision.transforms.Resize(size=(224, 224)),
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        
        dataset = XRayDataset(pathImages, transform) # Cargamos data
        
        self.data_loader = DataLoader(dataset, batch_size=batch_size) # DataLoader
        #print('Number of batches', len(self.data_loader))

    def evalImages(self):
        self.resnet18.eval() # Modo Evaluacion
        images_batch, names_batch = next(iter(self.data_loader))   # Obtenemos el lote de imagenes.
        outputs = self.resnet18(images_batch) #Evaluamos lote de imagnes
        _, preds = torch.max(outputs, 1) #Obtenemos la prediccion del lote

        #for (index, item) in enumerate(preds):
        #    print("Imagen: ",names_batch[index], "| Sintoma: ",self.clasificacion[item])
        for (index, item) in enumerate(preds):
            sintoma = self.clasificacion[item]

        return sintoma

#pronostico = Clasificador()
#pronostico.loadData()
#pronostico.evalImages()