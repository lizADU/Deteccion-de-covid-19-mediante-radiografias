import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from loginUi import Login_Ui
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5 import uic
from Conexion import Conexion
from menuWindow import MenuWindow
from menuDoctor import CrudDoctor


class LoginWindow (QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.login = uic.loadUi("login.ui")
        #self.login = Login_Ui()
        #self.login.setupUi(self)
        #self.paciente = uic.loadUi("Paciente.ui")
        self.Doctor = uic.loadUi("Crud_Doctor.ui")
        self.login.boton_iniciar.clicked.connect(self.iniciar_sesion)
        self.conection = Conexion()

    def iniciar_sesion(self):
        self.login.label_usuario_incorrecto.setText("")
        self.login.label_contrasenia_incorrecta.setText("")
        user_entry = self.login.entry_usuarios.text()
        password_entry = self.login.entry_contrasenia.text()

        user_entry = str(user_entry)
        password_entry = str(password_entry)
        usuarios =self.conection.getUser()

        admin = self.conection.getAdmin()
        user_admin = admin[0][0]
        user_password = admin[0][1]
        #print(usuarios)

        for user in range(len(usuarios)):
            if (user_entry==usuarios[user][0] and password_entry == usuarios[user][1]):
                if user_entry == user_admin and password_entry == user_password:
                    self.menuDoctor = CrudDoctor(self.login)
                    self.login.entry_usuarios.clear()
                    self.login.entry_contrasenia.clear()
                    self.menuDoctor.menuPrincipal()
                    self.cerrar()
                    break
                else:

                    dato1 = usuarios[user][0]
                    id = self.conection.getDoctorCI(dato1)
                    id = id[0][0]
                    self.menuPaciente = MenuWindow(int(id),self.login)
                    self.login.entry_usuarios.clear()
                    self.login.entry_contrasenia.clear()
                    self.menuPaciente.menuPaciente()
                    self.cerrar()
# self.close()

    def abrir(self):
        self.login.show()

    def cerrar(self):
        self.login.hide()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = LoginWindow()
    login.abrir()
    sys.exit(app.exec_())