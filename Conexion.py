import mysql.connector


class Conexion:
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost', database='hospital', user='root', password='12345')

    def crearPaciente(self, doctor, ci, nombre, apellido1, apellido2, genero, telefono, edad):
        cur = self.connection.cursor()
        sql = "INSERT INTO PACIENTES (CI, NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO, GENERO, TELEFONO, EDAD, CI_DOCTOR) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(ci, nombre, apellido1, apellido2, genero, telefono, edad, doctor)
        cur.execute(sql)
        self.connection.commit()
        cur.close()
    
    def buscarPaciente(self, doctor, ci):
        cur = self.connection.cursor()
        sql = "SELECT CI, NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO, GENERO, TELEFONO, EDAD FROM PACIENTES WHERE CI_DOCTOR='{}' AND CI LIKE '{}'".format(doctor, ci)
        cur.execute(sql)
        paciente = cur.fetchall()
        cur.close()
        return paciente

    def editarPaciente(self, doctor, ci, nombre, apellido1, apellido2, genero, telefono, edad):
        cur = self.connection.cursor()
        sql = "UPDATE `PACIENTES` SET `NOMBRE` = '{}', APELLIDO_PATERNO = '{}', APELLIDO_MATERNO = '{}', GENERO = '{}', TELEFONO = '{}', EDAD = '{}' WHERE CI_DOCTOR = '{}' AND CI = '{}'".format(nombre, apellido1, apellido2, genero, telefono, edad, doctor, ci)
        cur.execute(sql)
        self.connection.commit()
        cur.close()

    def editarAnalisis(self, diagnostico, fecha, id):
        cur = self.connection.cursor()
        sql = "UPDATE `PACIENTES` SET `DIAGNOSTICO` = '{}', FECHA = '{}' WHERE CI = '{}'".format(diagnostico, fecha, id)
        cur.execute(sql)
        self.connection.commit()
        cur.close()
    
    def filtrarPacientes(self, doctor, ci):
        cur = self.connection.cursor()
        sql = "SELECT CI, NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO, GENERO, TELEFONO, EDAD FROM PACIENTES WHERE CI_DOCTOR='{}' AND CI LIKE '{}%'".format(doctor, ci)
        cur.execute(sql)
        filtro = cur.fetchall()
        cur.close()
        return filtro
    
    def eliminarPaciente(self, ci):
        cur = self.connection.cursor()
        sql = "DELETE FROM PACIENTES WHERE CI = '{}'".format(ci)
        cur.execute(sql)
        self.connection.commit()
        cur.close()

    def getRegistrosPacientes(self, doctor):
        cur = self.connection.cursor()
        sql = "SELECT CI, NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO, GENERO, TELEFONO, EDAD FROM PACIENTES WHERE CI_DOCTOR='{}'".format(doctor)
        cur.execute(sql)
        registro = cur.fetchall()
        cur.close()
        return registro

    def getCI(self, doctor):
        cur = self.connection.cursor()
        sql = "SELECT CI FROM PACIENTES WHERE CI_DOCTOR = '{}'".format(doctor)
        cur.execute(sql)
        registro = cur.fetchall()
        cur.close()
        return registro

    def getUser(self):
        cur= self.connection.cursor()
        cur.execute("SELECT USUARIO, CONTRASEÑA FROM DOCTORES")
        user = cur.fetchall()
        cur.close()
        return user
    
    def getDoctorCI(self, user):
        cur = self.connection.cursor()
        sql = "SELECT CI FROM DOCTORES WHERE USUARIO='{}'".format(user)
        cur.execute(sql)
        ci = cur.fetchall()
        cur.close()
        return ci

    def getAdmin(self):
        cur=self.connection.cursor()
        cur.execute("SELECT USUARIO,CONTRASEÑA FROM DOCTORES WHERE USUARIO = 'ADMIN'")
        admin = cur.fetchall()
        cur.close()
        return admin

    def getCiPasiente(self):
        cur =self.connection.cursor()
        cur.execute("SELECT CI FROM PACIENTES")
        ci=cur.fetchall()
        cur.close()
        return ci

    def getDatos(self,ci):
        cur =self.connection.cursor()
        cur.execute("SELECT NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO, DIAGNOSTICO, CI, GENERO, EDAD,FECHA FROM pacientes WHERE CI = {}".format(ci))
        datos = cur.fetchall()
        cur.close()
        return datos
        
 #DOCTOR

    def editarDoctor(self, ci, nombre, apellido1, apellido2, telefono, usuario, contraseña):
        cur = self.connection.cursor()
        cur.execute("UPDATE `DOCTORES` SET `NOMBRE` = '{}', APELLIDO_PATERNO = '{}', APELLIDO_MATERNO = '{}', TELEFONO = '{}', USUARIO = '{}', CONTRASEÑA = '{}' WHERE CI = '{}'".format(nombre, apellido1, apellido2, telefono, ci, usuario, contraseña))
        self.connection.commit()
        cur.close()
    
    def crearDoctor(self, ci, nombre, apellido1, apellido2, genero, telefono, edad, usuario, contraseña):
        cur = self.connection.cursor()
        cur.execute("INSERT INTO DOCTORES (CI, NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO, GENERO, TELEFONO, EDAD, USUARIO, CONTRASEÑA) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(ci, nombre, apellido1, apellido2, genero, telefono, edad, usuario, contraseña))
        self.connection.commit()
        cur.close()
    
    def getCiDoctor(self):
        cur =self.connection.cursor()
        cur.execute("SELECT CI FROM doctores ")
        ci=cur.fetchall()
        cur.close()
        return ci
    
    def getDoctor(self,aCi):
        cur = self.connection.cursor()
        cur.execute("SELECT CI, NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO, GENERO, TELEFONO, EDAD, USUARIO, CONTRASEÑA FROM doctores WHERE CI ={}".format(aCi))
        lista =cur.fetchall()
        cur.close()
        return lista

    def insertarDoctor(self,ci, nombre, apellido1, apellido2, genero, telefono, edad, usuario, contraseña):
        cur = self.connection.cursor()
        cur.execute("INSERT INTO doctores (CI, NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO, GENERO, TELEFONO, EDAD, USUARIO,CONTRASEÑA) VALUES({},'{}','{}','{}','{}',{},{},'{}','{}')".format(ci, nombre, apellido1, apellido2, genero, telefono, edad, usuario, contraseña))
        self.connection.commit()
        cur.close()

    def mostrarDatosDoctor(self):
        cur = self.connection.cursor()
        cur.execute("SELECT CI, NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO, GENERO, TELEFONO, EDAD, USUARIO, CONTRASEÑA FROM doctores")
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscarDoctor(self,ci):
        cur = self.connection.cursor()
        cur.execute("SELECT CI, NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO, GENERO, TELEFONO, EDAD, USUARIO, CONTRASEÑA FROM doctores WHERE CI LIKE '{}%'".format(ci))
        lista = cur.fetchall()
        cur.close()
        return lista

    def eliminarDoctor(self, ci):
        cur = self.connection.cursor()
        cur.execute("DELETE FROM doctores WHERE CI = '{}'".format(ci))        
        self.connection.commit()
        cur.close()

    def actualizarDoctor(self,ci,nombre,apellidoPaterno,apellidoMaterno,genero,telefono,edad,usuario,contrasenia1,Aci):
        cur=self.connection.cursor()
        cur.execute("UPDATE doctores set CI ={},NOMBRE ='{}',APELLIDO_PATERNO='{}', APELLIDO_MATERNO='{}', GENERO='{}', TELEFONO={}, EDAD={}, USUARIO='{}', CONTRASEÑA='{}' WHERE CI ={}".format(ci,nombre,apellidoPaterno,apellidoMaterno,genero,telefono,edad,usuario,contrasenia1,Aci))
        self.connection.commit()
        cur.close()


reg =Conexion()
print(reg.getAdmin())
#print(reg.getCiPasiente())
#print(reg.editarAnalisis('viral', '15/07/22', 7111403))
#print(reg.getDatos(7111403))