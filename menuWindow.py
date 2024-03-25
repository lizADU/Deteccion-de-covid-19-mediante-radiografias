
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation
from menuUi import Menu_Ui
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5 import uic
from Conexion import Conexion
from main_visor import *
import os


class MenuWindow():
    def __init__(self, doctor,login):
        self.doctor = doctor
        self.login = login
        #self.menu = Menu_Ui()
        self.menu = uic.loadUi("Paciente.ui")
        #self.menu.setupUi(self)
        self.windowSize = 10
        #self.grip = QtWidgets.QSizeGrip(self)
        #self.grip.resize(self.windowSize, self.windowSize)
        self.menu.frame_superior.mouseMoveEvent = self.moveWindow
        self.conexion = Conexion()
        self.cargarComboBox()

        self.menu.boton_menu.clicked.connect(self.moveMenu)
        self.menu.boton_registrar_paciente.clicked.connect(self.guardarPaciente)
        self.menu.boton_buscar_editar.clicked.connect(self.buscarPaciente)
        self.menu.boton_actualizar_datos.clicked.connect(self.actualizarPaciente)
        self.menu.boton_analizar.clicked.connect(self.rellenarTabla)
        self.menu.boton_buscar_editar_2.clicked.connect(self.getDatosPasiente)#self.filtrarPaciente) and self.getDatosPasiente()
        self.menu.boton_eliminar.clicked.connect(self.eliminarPaciente)
        self.menu.boton_buscar_2.clicked.connect(self.volver)
        #self.menu.boton,clicked.connect(self.getDatosPasiente) 

    def volver(self):
        self.menu.hide()
        self.login.show()    

    def menuPaciente(self):
        self.menu.show()
        self.menu.boton_registrar.clicked.connect(lambda: self.menu.stackedWidget.setCurrentWidget(self.menu.page_dos))
        self.menu.boton_editar.clicked.connect(lambda: self.menu.stackedWidget.setCurrentWidget(self.menu.page_tres))
        self.menu.boton_buscar.clicked.connect(lambda: self.menu.stackedWidget.setCurrentWidget(self.menu.page_cuatro))
        

    def cargarComboBox(self):
        self.menu.entry_ci_edit.clear()
        self.menu.entry_ci_eliminar.clear()
        i = 0
        combo = self.conexion.getCI(self.doctor)
        while i < len(combo):
            self.menu.entry_ci_edit.addItem(str(combo[i][0]))
            self.menu.entry_ci_eliminar.addItem(str(combo[i][0]))
            i = i + 1
            self.menu.entry_ci_edit.setCurrentIndex(-1)
            self.menu.entry_ci_eliminar.setCurrentIndex(-1)
            
    def moveMenu(self):
        if True:
            width = self.menu.frame_lateral.width()
            normal = 0
            if width == 0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.menu.frame_lateral, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.windowSize, rect.bottom() - self.windowSize)

    def moveWindow(self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <= 20:
            self.showMaximized()
        else:
            self.showNormal()

    def guardarPaciente(self):
        self.menu.label_12.setText("")
        ci = self.menu.entry_ci.text()
        nombre = self.menu.entry_nombre.text()
        apellidoP = self.menu.entry_apellido_paterno.text()
        apellidoM = self.menu.entry_apellido_materno.text()
        genero = self.menu.entry_genero.text()
        celular = self.menu.entry_celular.text()
        edad = self.menu.entry_edad.text()

        if ((ci == '' or nombre == '') or (apellidoP == '' or apellidoM == '')) or ((celular == '' or edad == '') or genero == ''):
            self.menu.label_12.setText("Ingrese todos los campos requeridos")
        else:
            verificador = self.revisar(ci)
            if verificador == True:
                self.menu.label_12.setText("La persona ya existe")
            else:
                if genero == "F" or genero == "M":
                    self.conexion.crearPaciente(self.doctor, ci, nombre, apellidoP, apellidoM, genero, celular, edad)
                    carpeta = nombre +' '+ apellidoP +' '+ apellidoM
                    os.mkdir('Pacientes/{}'.format(carpeta))
                    self.menu.label_12.setText("Registro Completado")
                    self.menu.entry_ci.setText("")
                    self.menu.entry_nombre.setText("")
                    self.menu.entry_apellido_paterno.setText("")
                    self.menu.entry_apellido_materno.setText("")
                    self.menu.entry_genero.setText("")
                    self.menu.entry_celular.setText("")
                    self.menu.entry_edad.setText("")
                    self.cargarComboBox()
                else:
                    self.menu.label_12.setText("Exprese Masculino con la letra M y Femenino con la letra F")
    
    def revisar(self,ci):
        listaCi =self.conexion.getCiPasiente()
        for buscar in listaCi:
            if ci == str(buscar[0]):
                return True
            else:
                return False

    def buscarPaciente(self):
        try:
            ci = self.menu.entry_ci_edit.currentText()
            search = self.conexion.buscarPaciente(self.doctor, ci)
            self.menu.entry_edit_ci.setText(str(search[0][0]))
            self.menu.entry_edit_nombre.setText(search[0][1])
            self.menu.entry_edit_apellido_paterno.setText(search[0][2])
            self.menu.entry_edit_apellido_materno.setText(search[0][3])
            self.menu.entry_edit_genero.setText(search[0][4])
            self.menu.entry_edit_celular.setText(str(search[0][5]))
            self.menu.entry_edit_edad.setText(str(search[0][6]))
        except:
            print(' ')

    def getDatosPasiente(self):
        try:
            ciPaciente = self.menu.entry_ci_edit.currentText()
            datosPaciente = (self.conexion.getDatos(ciPaciente))[0]
            print(datosPaciente)
            nombre = datosPaciente[0]+' '+datosPaciente[1]+' '+datosPaciente[2]
            sexo = datosPaciente[5]
            edad = datosPaciente[6]
            ci = datosPaciente[4]
            app = QtWidgets.QApplication([])

            my_app = Ventana(app, ci, nombre, sexo, edad)
            my_app.abrir()
            app.exec_()
        except:
            print(' ')
        
    def actualizarPaciente(self):
        ci = self.menu.entry_edit_ci.text()
        nombre = self.menu.entry_edit_nombre.text()
        apellido1 = self.menu.entry_edit_apellido_paterno.text()
        apellido2 = self.menu.entry_edit_apellido_materno.text()
        genero = self.menu.entry_edit_genero.text()
        celular = self.menu.entry_edit_celular.text()
        edad = self.menu.entry_edit_edad.text()
    
        if ((ci == '' or nombre == '') or (apellido1 == '' or apellido2 == '')) or ((celular == '' or edad == '') or genero == ''):
            self.menu.label_datos_actualizados.setText("Ingrese todos los datos requeridos")
        else:
            if genero == "F" or genero == "M":
                self.conexion.editarPaciente(self.doctor, ci, nombre, apellido1, apellido2, genero, celular, edad)
                self.menu.entry_edit_ci.setText("")
                self.menu.entry_edit_nombre.setText("")
                self.menu.entry_edit_apellido_paterno.setText("")
                self.menu.entry_edit_apellido_materno.setText("")
                self.menu.entry_edit_genero.setText("")
                self.menu.entry_edit_celular.setText("")
                self.menu.entry_edit_edad.setText("") 
                self.menu.label_datos_actualizados.setText("Datos Actualizados")
                self.cargarComboBox()
            else:
                self.menu.label_datos_actualizados.setText("Exprese Masculino con la letra M y Femenino con la letra F")
    
    def rellenarTabla(self):
        data = self.conexion.getRegistrosPacientes(self.doctor)
        length = len(data)
        self.menu.tabla_buscar.setRowCount(length)
        tablerow = 0
        for row in data:
            self.menu.tabla_buscar.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.menu.tabla_buscar.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.menu.tabla_buscar.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.menu.tabla_buscar.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.menu.tabla_buscar.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.menu.tabla_buscar.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.menu.tabla_buscar.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            tablerow += 1
    
    def filtrarPaciente(self):
        ci = self.menu.entry_nombre_buscar.text()
        filtro = self.conexion.filtrarPacientes(self.doctor, ci)
        length = len(filtro)
        self.menu.tabla_buscar.setRowCount(length)
        tablerow = 0
        for row in filtro:
            self.menu.tabla_buscar.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.menu.tabla_buscar.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.menu.tabla_buscar.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.menu.tabla_buscar.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.menu.tabla_buscar.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.menu.tabla_buscar.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.menu.tabla_buscar.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            tablerow += 1
    
    def eliminarPaciente(self):
        ci = self.menu.entry_ci_eliminar.currentText()
        self.conexion.eliminarPaciente(ci)
        self.cargarComboBox()