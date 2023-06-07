# a=0
# salario= input()
# try:
#     int(salario)
#     a=1
# except ValueError:
#     a=-1

def str(nom):  
    a=0   
    r=0
    abc = "abcdefghijklmnopqrstuvwxyz"
    for x in range(len(nom)):
        for i in range(len(abc)):    
            if nom[x]==abc[i]:
                a+=1
    if a != len(nom):
        return "no es str"
    if a==len(nom):
        return "es str"
nom = input()
print(str(nom))

####OBIGATORIO####
##FUNCIONES:
#verifica que la cedula es real
def verificar_cedula(cedula):
    a=1
    suma=0
    digitos=[] 
    verificador=[2,9,8,7,6,3,4]                  #digito verificador de cedulas uruguayas
    for i in range(0,len(cedula), a):
        try:
            digitos.append(int(cedula[i : i+a])) #convierte el str a una lista de ints
        except ValueError:                       #intenta lo de arriba, si falla entonces no es una cedula 
            return False
    if len(digitos)==7:                          #si la cedula no tiene millones, le agrega un cero a la izq
        digitos.insert(0, 0)
    if len(digitos)==8:
        a=digitos[7]
        digitos.pop()
        for x in range(len(digitos)):
            suma+=digitos[x]*verificador[x]
        resto=10-suma%10
        if resto==10:
            resto=0
    else:
        resto= "ERROR"
    return resto

    
#verificar si es string
def verificar_nombre(palabra):  
    a=0   
    abc = "abcdefghijklmnopqrstuvwxyz"
    for x in range(len(palabra)):
        for i in range(len(abc)):    
            if palabra[x]==abc[i]:
                a+=1
    if a != len(palabra):
        return False
    if a==len(palabra):
        return True

#def class sector
class Sector:
    empleados=[]
    def __init__(self, empleados=None, supervisor=None, puntos=0):
        self.empleados= empleados
        self.supervisor= supervisor
        self.puntos= puntos
    def agregarEmpleado(self, empleado):
        self.empleado.append(empleado)
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

#setters Empleado
    def set_nombre(self,nombre):
        while len(nombre)<3 or len(nombre)>20 or str(nombre)== False:
            nombre = input('el nombre tiene que ser solo letras y debe de ser minimo 3 caracteres y maximo de 20')
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
        if cargo == 4:
            self.cargo= "Desarrollador"

        else:
            print("inserte uno de los cargos de la lista")
            
