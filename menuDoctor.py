from turtle import clear
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from Conexion import Conexion
class CrudDoctor:
    def __init__(self,login):
        self.conexion = Conexion()
        self.menu=uic.loadUi("Crud_Doctor.ui")
        self.login=login
        self.menu.frame_superior.mouseMoveEvent = self.moveWindow 
        self.menu.boton_menu.clicked.connect(self.moveMenu)
        self.menu.boton_volver.clicked.connect(self.volver)
        self.menu.boton_registrar_paciente.clicked.connect(self.registrarDoctor)
        self.menu.pushButton.clicked.connect(self.mostrarDoctor)
        self.menu.boton_buscar_editar_2.clicked.connect(self.buscarDoctor)
        self.menu.pushButton_2.clicked.connect(self.eliminarDoctor)
        self.menu.boton_buscar_editar.clicked.connect(self.obtenerDoctor)
        self.menu.boton_actualizar_datos.clicked.connect(self.actualizarDoctor)


    def menuPrincipal(self):
        self.menu.show()
        self.menu.boton_editar.clicked.connect(lambda: self.menu.stackedWidget.setCurrentWidget(self.menu.page_tres))
        self.menu.boton_registrar.clicked.connect(lambda: self.menu.stackedWidget.setCurrentWidget(self.menu.page_dos))
        self.menu.boton_buscar.clicked.connect(lambda: self.menu.stackedWidget.setCurrentWidget(self.menu.page_uno)) and self.mostrarDoctor()

    def volver(self):
        self.menu.hide()
        self.login.show()

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

#regitrar Doctor-----------------------------------------------------------
    def registrarDoctor(self):
        ci =self.menu.entry_ci_doc.text()
        nombre =self.menu.entry_nombre_doc.text()
        apellidoPaterno =self.menu.entry_paterno_doc.text()
        apellidoMaterno =self.menu.entry_materno_doc.text()
        genero=self.menu.entry_genero_doc.text()
        telefono =self.menu.entry_telefono_doc.text()
        edad = self.menu.entry_edad_doc.text()
        usuario =self.menu.entry_usuario_doc.text()
        contrasenia1 =self.menu.entry_contrasenia_doc.text()
        contrasenia2 =self.menu.entry_repit_contrasenia_doc.text()
        
        if ci and nombre and apellidoPaterno and apellidoMaterno and genero and telefono and edad and usuario and contrasenia1 and contrasenia2 != "":
            verificarCi = self.revisar(ci)
            if verificarCi == True:
                self.menu.label_12.setText("La persona ya existe")
            else:
                if contrasenia1 == contrasenia2:
                    print("perfecto")
                    self.conexion.insertarDoctor(int(ci),nombre,apellidoPaterno,apellidoMaterno,genero,int(telefono),int(edad),usuario,contrasenia1)
                    self.menu.label_12.setText("registrado")
                    
                    self.menu.entry_ci_doc.clear()
                    self.menu.entry_nombre_doc.clear()
                    self.menu.entry_paterno_doc.clear()
                    self.menu.entry_materno_doc.clear()
                    self.menu.entry_genero_doc.clear()
                    self.menu.entry_telefono_doc.clear()
                    self.menu.entry_edad_doc.clear()
                    self.menu.entry_usuario_doc.clear()
                    self.menu.entry_contrasenia_doc.clear()
                    self.menu.entry_repit_contrasenia_doc.clear()

                else:
                    self.menu.label_12.setText("Contraseña no coincide")
        else:
            self.menu.label_12.setText("Complete todo")
            
    def revisar(self,ci):
        listaCi = self.conexion.getCiDoctor()
        for buscar in listaCi:
            if int(ci) == buscar[0]:
                return True
        else:
            return False

#---------------------------------------------------------------------------------------

#mostrar Doctor
    def mostrarDoctor(self):
        datosDoctor = self.conexion.mostrarDatosDoctor()
        filas = len(datosDoctor)
        self.menu.tabla_lista.setRowCount(filas)
        tablafila = 0

        for dato in datosDoctor:
            self.menu.tabla_lista.setItem(tablafila,0,QtWidgets.QTableWidgetItem(str(dato[0])))
            self.menu.tabla_lista.setItem(tablafila,1,QtWidgets.QTableWidgetItem(dato[1]))
            self.menu.tabla_lista.setItem(tablafila,2,QtWidgets.QTableWidgetItem(dato[2]))
            self.menu.tabla_lista.setItem(tablafila,3,QtWidgets.QTableWidgetItem(dato[3]))
            self.menu.tabla_lista.setItem(tablafila,4,QtWidgets.QTableWidgetItem(dato[4]))
            self.menu.tabla_lista.setItem(tablafila,5,QtWidgets.QTableWidgetItem(str(dato[5])))
            self.menu.tabla_lista.setItem(tablafila,6,QtWidgets.QTableWidgetItem(str(dato[6])))
            self.menu.tabla_lista.setItem(tablafila,7,QtWidgets.QTableWidgetItem(dato[7]))
            self.menu.tabla_lista.setItem(tablafila,8,QtWidgets.QTableWidgetItem(dato[8]))

            tablafila +=1

    def buscarDoctor(self):
        print("")
        buscarCi= self.menu.entry_nombre_paciente_2.text()
        listaDoctor = self.conexion.buscarDoctor(buscarCi)
        fila = len(listaDoctor)
        self.menu.tabla_lista.setRowCount(fila)
        tablaFila = 0

        for dato in listaDoctor:
            self.menu.tabla_lista.setItem(tablaFila,0,QtWidgets.QTableWidgetItem(str(dato[0])))
            self.menu.tabla_lista.setItem(tablaFila,1,QtWidgets.QTableWidgetItem(dato[1]))
            self.menu.tabla_lista.setItem(tablaFila,2,QtWidgets.QTableWidgetItem(dato[2]))
            self.menu.tabla_lista.setItem(tablaFila,3,QtWidgets.QTableWidgetItem(dato[3]))
            self.menu.tabla_lista.setItem(tablaFila,4,QtWidgets.QTableWidgetItem(dato[4]))
            self.menu.tabla_lista.setItem(tablaFila,5,QtWidgets.QTableWidgetItem(str(dato[5])))
            self.menu.tabla_lista.setItem(tablaFila,6,QtWidgets.QTableWidgetItem(str(dato[6])))
            self.menu.tabla_lista.setItem(tablaFila,7,QtWidgets.QTableWidgetItem(dato[7]))
            self.menu.tabla_lista.setItem(tablaFila,8,QtWidgets.QTableWidgetItem(dato[8]))

            tablaFila +=1



#-----------------------------------------------------------------------------------------
#eliminar doctor 
    def eliminarDoctor(self):
        eliminar = self.menu.entry_nombre_paciente_2.text()
        self.conexion.eliminarDoctor(eliminar)
        self.mostrarDoctor()
#------------------------------------------------------------------------------------------
#actualizar doctor
    def obtenerDoctor(self):
        aCi=self.menu.entry_nombre_paciente.text()
        if aCi =="":
            self.menu.label_datos_actualizados.setText("Introduzca Ci")
        else:
            doctor = self.conexion.getDoctor(aCi)
            if doctor ==[]:
                self.menu.label_datos_actualizados.setText("Doctor no existe")
            else:
                self.menu.label_datos_actualizados.clear()
                self.menu.entry_ci_doc_edit.setText(str(doctor[0][0]))
                self.menu.entry_nombre_doc_edit.setText(doctor[0][1])
                self.menu.entry_paterno_doc_edit.setText(doctor[0][2])
                self.menu.entry_materno_doc_edit.setText(doctor[0][3])
                self.menu.entry_genero_doc_edit.setText(doctor[0][4])
                self.menu.entry_telefono_doc_edit.setText(str(doctor[0][5]))
                self.menu.entry_edad_doc_edit.setText(str(doctor[0][6]))
                self.menu.entry_usuario_doc_edit.setText(doctor[0][7]) 
                self.menu.entry_contrasenia_doc_edit.setText(doctor[0][8])   
                self.menu.entry_repit_contrasenia_doc_edit.setText(doctor[0][8])   


        
    def actualizarDoctor(self):
        Aci=self.menu.entry_nombre_paciente.text()
        ci =self.menu.entry_ci_doc_edit.text()
        nombre =self.menu.entry_nombre_doc_edit.text()
        apellidoPaterno =self.menu.entry_paterno_doc_edit.text()
        apellidoMaterno =self.menu.entry_materno_doc_edit.text()
        genero=self.menu.entry_genero_doc_edit.text()
        telefono =self.menu.entry_telefono_doc_edit.text()
        edad = self.menu.entry_edad_doc_edit.text()
        usuario =self.menu.entry_usuario_doc_edit.text()
        contrasenia1 =self.menu.entry_contrasenia_doc_edit.text()
        contrasenia2 =self.menu.entry_repit_contrasenia_doc_edit.text()
        
        if ci and nombre and apellidoPaterno and apellidoMaterno and genero and telefono and edad and usuario and contrasenia1 and contrasenia2 != "":
            
            if contrasenia1 == contrasenia2:
                print("perfecto")
                self.conexion.actualizarDoctor(int(ci),nombre,apellidoPaterno,apellidoMaterno,genero,int(telefono),int(edad),usuario,contrasenia1,int(Aci))
                self.menu.label_datos_actualizados.setText("Actualizado....")

                self.menu.entry_ci_doc_edit.clear()
                self.menu.entry_nombre_doc_edit.clear()
                self.menu.entry_paterno_doc_edit.clear()
                self.menu.entry_materno_doc_edit.clear()
                self.menu.entry_genero_doc_edit.clear()
                self.menu.entry_telefono_doc_edit.clear()
                self.menu.entry_edad_doc_edit.clear()
                self.menu.entry_usuario_doc_edit.clear()
                self.menu.entry_contrasenia_doc_edit.clear()
                self.menu.entry_repit_contrasenia_doc_edit.clear()



            else:
                self.menu.label_datos_actualizados.setText("Contraseña no coincide")
        else:
            self.menu.label_datos_actualizados.setText("Complete todo")
