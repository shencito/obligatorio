from funciones import *
#def class sector
class Sector:
    empleados=[]
    def __init__(self, empleados=None, supervisor=None, puntos=0):
        self.empleados= empleados
        self.supervisor= supervisor
        self.puntos= puntos
    def agregarEmpleado(self, empleado):
        self.empleados.append(empleado)
    def otorgar_puntos(self, puntos):
        a=0
        while a==0:
            try:
                if puntos>0:
                    self.puntos+= puntos
                    a=1
            except:
                ValueError
            if a==0:
                puntos= input("inserte una cantidad de puntos valida")
    def get_empleados(self):
        a=[]
        for empleado in self.empleados:
            a.append(empleado)
        return a
            
    # def set_supervisor(self, empleado,cedula):
    #     supervisor = 
    #     if 


# definimos clase de empleados        

class Empleado:
    def __init__(self, nombre=None, cedula=None, salario=None, cargo=None):
        self.nombre = nombre
        self.cedula = cedula
        self.salario = salario
        self.cargo= cargo
#geters para cada uno de los atributos
    def get_E(self):
        print(self.nombre)
        print(self.cedula)
        print(self.salario)
        print(self.cargo)
    def get_C(self):
        return self.cedula
    def get_cargo(self):
        return self.cargo

#setters Empleado
    def set_nombre(self,nombre):
        while len(nombre)<3 or len(nombre)>20 or verificar_nombre(nombre)== False:
            nombre = input('el nombre tiene que ser solo letras y debe de ser minimo 3 caracteres y maximo de 20: ')
        self.nombre = nombre
         
    def set_cedula(self,cedula):
        a=False
        while a == False:
            a= verificar_cedula(cedula)
            if a == True:
                self.cedula=cedula

            else:
                cedula=input("inserte una cedula veridica sin puntos ni guiones: ")

    def set_salario(self, salario):
        a=0
        while a==0:
            try:
                int(salario)
                self.salario=salario
                a=1
            except ValueError:
                salario= input("el salario debe ser un numero")

    def set_cargo(self, cargo):
        if cargo == 1:
            self.cargo= "supervisor"
        elif cargo == 2:
            self.cargo= "Team Leader"
        elif cargo == 3:
            self.cargo= "Analista"
        elif cargo == 4:
            self.cargo= "Desarrollador"

        else:
            print("inserte uno de los cargos de la lista")
            
