Deteccion de COVID - 19 con Inteligencia Artificial
Intrucciones para la implementacion del Entrenamiento y el Clasificador de radiografias:

Requisitos Previos
1. Tener instalado Python.
2. Tener instalado Miniconda.
3. Crear un environment con el comando:
conda create -n nombre
4. Activar el environment con el comando:
conda activate nombre
5. Tener instalado PyTorch y torchvision, el comando para instalarlo mediante minianaconda es el siguiente: 
conda install pytorch torchvision cudatoolkit=10.2 -c pytorch;
6. Tener instalado las librerias necesarias para PyQt con el siguiente comando:
conda install -c anaconda pyqt
7. Tener instalado las librerias de Matplotlib con el siguiente comando:
conda install -c conda-forge matplotlib
8. Tener instalado MySql y activar el connector con los comandos:
pip install mysql
pip install mysql-connector-python
9. Seleccionar el environment en tu editor de codigo, seleccionar loginWindow.py y darle run. 

Nota Extra: En caso de ejecutar el programa clasificador.py es necesario crear una carpeta llamada resnet_uploads/ y guardar aqui las imagenes a clasificar en formato png.


Entrenamiento
1. Descarga el conjunto de datos: https://www.kaggle.com/tawsifurrahman/covid19-radiography-database y guárdala en la carpeta del repositorio.
2. Renombra la carpeta a Radiography
3. Ejecuta el archivo Python covid.py.
Nota Extra: En caso de entrenar el modelo, este sobrescribirá al modelo guardado de la carpeta resnet/

Ejecutar Clasificador
1. Las imágenes que el clasificador usara se deben de guardar en una carpeta llamada resnet_uploads/ y deben de estar en formato .png
2. Ejecuta el archivo Python clasificador.py.

