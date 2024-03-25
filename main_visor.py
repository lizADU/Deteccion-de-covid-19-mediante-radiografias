from os import getcwd
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QPalette, QImage, QPixmap
from PyQt5.QtCore import (Qt, QDir, QFile, QFileInfo, QPropertyAnimation, QRect,
                          QAbstractAnimation, QTranslator, QLocale, QLibraryInfo)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QMessageBox,
                             QFrame, QLabel, QFileDialog)
import os
import shutil
from clasificador import Clasificador
from datetime import datetime
from Conexion import *

class Ventana:
    def __init__(self, app, ci, nombre, sexo, edad):
        self.__app = app
        self.__ci = ci
        self.__nombre = nombre
        self.__sexo = sexo
        self.__edad = edad
        self.ventana=uic.loadUi("visorDeImagenes.ui")
        self.resultado = uic.loadUi('reporte.ui')
        self.conexion = Conexion()
        self.ventana.pushButton_12.clicked.connect(self.seleccionarImagen)
        self.ventana.pushButton_10.clicked.connect(lambda: self.ventana.label.clear())
        self.ventana.pushButton_9.clicked.connect(self.analizarImagen)
        self.ventana.pushButton_7.clicked.connect(self.cerrar)

    def abrir(self):
        self.ventana.show()
        
    def seleccionarImagen(self):
        self.imagen, extension = QFileDialog.getOpenFileName(self.ventana, "Seleccionar imagen", getcwd(),
                                                        "Archivos de imagen (*.png *.jpg *.jpeg)",
                                                        options=QFileDialog.Options())

        if self.imagen:
            # Adaptar imagen
            pixmapImagen = QPixmap(self.imagen).scaled(500,600, Qt.KeepAspectRatio,
                                                  Qt.SmoothTransformation)

            # Mostrar imagen
            self.ventana.label.setPixmap(pixmapImagen)

    def analizarImagen(self):
        shutil.copy(str(self.imagen), 'resnet_uploads/')
        resultado = next(os.walk('resnet_uploads/'))[2]
        #os.rename(('resnet_uploads/',str(resultado[0])), ('resnet_uploads/ejemplo.png'))

        pronostico = Clasificador()
        pronostico.loadData()
        final = pronostico.evalImages()

        fecha = datetime.today().strftime('%Y-%m-%d %H:%M')
        os.remove('resnet_uploads/'+resultado[0])
        shutil.copy(str(self.imagen), 'Pacientes/{}'.format(str(self.__nombre)))
        self.conexion.editarAnalisis(final, fecha, self.__ci)

        self.resultado.show()
        self.resultado.label_15.setText(final)
        self.resultado.label_7.setText(self.__nombre)
        self.resultado.label_9.setText(fecha)
        self.resultado.label_12.setText(str(self.__ci))
        self.resultado.label_10.setText(self.__sexo)
        self.resultado.label_11.setText(str(self.__edad))

    def cerrar(self):
        self.ventana.hide()
        #self.__app.exit()
    

#app = QtWidgets.QApplication([])
#my_app = Ventana(app)
#my_app.abrir()
#app.exec_()
