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
    if resto==a:
        return True
    else:
        return False 
    
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

def verificar_existencia_empleado(cedula, lista_empleados):
    existencia = False
    while existencia == False:
        for empleado in lista_empleados:
            if empleado.get_C()== cedula:
                existencia=True
        if existencia==True:
            return True
        if existencia==False:
            cedula=input("inserte una cedula veridica sin puntos ni guiones que ya este registrada en el sistema: ")


