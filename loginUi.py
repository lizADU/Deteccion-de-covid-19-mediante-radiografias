# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Login_Ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1294, 838)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imagenes login/Isometric hospital website page.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(230, 40, 281, 171))
        self.label_4.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"border:None;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("imagenes login/hospital.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(280, 240, 191, 51))
        self.label_5.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"font: 20pt \"MV Boli\";\n"
"border:None;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.entry_usuarios = QtWidgets.QLineEdit(self.frame_2)
        self.entry_usuarios.setGeometry(QtCore.QRect(240, 300, 281, 51))
        self.entry_usuarios.setStyleSheet("QPushEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.entry_usuarios.setAlignment(QtCore.Qt.AlignCenter)
        self.entry_usuarios.setObjectName("entry_usuarios")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(290, 420, 191, 31))
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"font: 20pt \"MV Boli\";\n"
"border:None;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.entry_contrasenia = QtWidgets.QLineEdit(self.frame_2)
        self.entry_contrasenia.setGeometry(QtCore.QRect(250, 470, 281, 51))
        self.entry_contrasenia.setStyleSheet("QPushEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"}")
        self.entry_contrasenia.setEchoMode(QtWidgets.QLineEdit.Password)
        self.entry_contrasenia.setAlignment(QtCore.Qt.AlignCenter)
        self.entry_contrasenia.setObjectName("entry_contrasenia")
        self.boton_iniciar = QtWidgets.QPushButton(self.frame_2)
        self.boton_iniciar.setGeometry(QtCore.QRect(310, 600, 161, 41))
        self.boton_iniciar.setStyleSheet("QPushButton{\n"
"\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 255);\n"
"    font: 75 12pt \"MS Shell Dig 2\";\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color:rgb(85, 170, 255);\n"
"    font: 75 12pt \"MS Shell Dig 2\";\n"
"}")
        self.boton_iniciar.setObjectName("boton_iniciar")
        self.boton_salir = QtWidgets.QPushButton(self.frame_2)
        self.boton_salir.setGeometry(QtCore.QRect(330, 670, 121, 31))
        self.boton_salir.setStyleSheet("QPushButton{\n"
"\n"
"    \n"
"    background-color: rgb(0, 0, 0,0%);\n"
"    font: 75 12pt \"MS Shell Dig 2\";\n"
"    border-radius:10px;\n"
"    border:None;\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"    background-color: rgb(85, 170, 255);\n"
"    font: 75 12pt \"MS Shell Dig 2\";\n"
"    \n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagenes login/cerrar-sesion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_salir.setIcon(icon)
        self.boton_salir.setIconSize(QtCore.QSize(20, 20))
        self.boton_salir.setObjectName("boton_salir")
        self.label_usuario_incorrecto = QtWidgets.QLabel(self.frame_2)
        self.label_usuario_incorrecto.setGeometry(QtCore.QRect(300, 370, 181, 31))
        self.label_usuario_incorrecto.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"font: 12pt \"MV Boli\";\n"
"color: rgb(255, 0, 0);\n"
"border:None;")
        self.label_usuario_incorrecto.setText("")
        self.label_usuario_incorrecto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_usuario_incorrecto.setObjectName("label_usuario_incorrecto")
        self.label_contrasenia_incorrecta = QtWidgets.QLabel(self.frame_2)
        self.label_contrasenia_incorrecta.setGeometry(QtCore.QRect(300, 550, 181, 31))
        self.label_contrasenia_incorrecta.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"font: 12pt \"MV Boli\";\n"
"color: rgb(255, 0, 0);\n"
"border:None;")
        self.label_contrasenia_incorrecta.setText("")
        self.label_contrasenia_incorrecta.setAlignment(QtCore.Qt.AlignCenter)
        self.label_contrasenia_incorrecta.setObjectName("label_contrasenia_incorrecta")

        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.boton_salir.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Usuario"))
        self.entry_usuarios.setPlaceholderText(_translate("MainWindow", "Ingrese su correo"))
        self.label_3.setText(_translate("MainWindow", "Contraseña"))
        self.entry_contrasenia.setPlaceholderText(_translate("MainWindow", "Ingrese su contraseña"))
        self.boton_iniciar.setText(_translate("MainWindow", "Iniciar sesion"))
        self.boton_salir.setText(_translate("MainWindow", "Salir"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login_Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
