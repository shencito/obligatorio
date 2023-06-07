###OBLIGATORIO

from clases import *
from funciones import *

#empieza codigo
if __name__ == "__main__": 
    cedula_empleados=[]
    lista_sectores=[]
    sector_1=Sector()
    lista_sectores.append(sector_1)
    sector_2=Sector()
    lista_sectores.append(sector_2)

    #cant empleados, el supervisor,cuantos: team leaders analistas y desarrolladores hay, por ultimo puntos
    # sector_1=Sector(0, "manuel", 2, 3, 5, 0)

        #bucle del programa
    y=1
    cantidad_empleados = 0
    while y == 1:
        r=0
        lista_empleados = []
        print("1. Alta de empleado.")
        print("2. Alta de sector.")
        print("3. Asignar empleado a un sector")
        print("4. Otorgar puntos a un sector")
        print("5. Realizar consultas")
        print("6. Finalizar programa")
        try:
            r= int(input("introduzca el numero de la opcion que desea tomar: "))
        except ValueError:
            print("***** debe ingresar una opcion de la lista *****")
        #Alta de empleado
        if r == 1: 
            continuar = 1
            while continuar == 1:
                empleado=Empleado()
                empleado.set_nombre(input('inserte el nombre del empleado: '))
                empleado.set_cedula(input('igrese la cedula del empleado sin puntos ni guion: '))
                empleado.set_salario(input('ingrese el salario del empleado: '))
                print("1: Supervisor")
                print("2: Team Leader")
                print("3: Analista")
                print("4: Desarrollador")
                empleado.set_cargo(input('ingrese el numero del cargo del empleado: '))
                # for x in range(len(lista_empleados)):
                #     if lista_empleados[x] == empleado:
                #         pass
                #     else:
                lista_empleados.append(empleado)
                cantidad_empleados+=1
                a=False
                valid=False
                while a == False:
                    continuar =input('quiere registrar otro empleado?(1 afirmativo, 0 volver al menu): ')
                    try:
                        continuar=int(continuar)
                        valid=True
                    except ValueError:
                        pass
                    if continuar ==1 or continuar ==0 and valid==True:
                            a=True
                    else:
                        print("debe elegir una opcion valida")  
        #Alta de sector                
        if r == 2:
            if len(lista_empleados)>0:
                sup=False
                for empleado in lista_empleados:
                    if empleado.get_cargo()== "supervisor":
                        sup=True
                if sup==True:
                    nuevo_sector=input("ingrese nombre del sector: ")
                    nuevo_sector=Sector()
                    cedula=input("inserte la cedula del supervisor a cargo: ")
                    a= verificar_existencia_empleado(cedula,lista_empleados)
                    # if a == 

            if len(lista_empleados)==0 or sup == False:
                print("***** no puedes crear un sector sin tener un supervisor para asignarle *****")














        if r == 3:
            if len(lista_empleados)>0:
                cedula = input("ingrese la cedula del empleado que quiera agregar a un sector: ")
                verificar_existencia_empleado(cedula, lista_empleados)
                    
                for x in range(len(lista_sectores)):
                    print(str(x) + ": " + str(lista_sectores))
                x=str(input("a que sector quiere agregarlo?: "))
                lista_empleados[x].agregarEmpleado(empleado)
            else:
                print("***** debe agregar empleados al sistema antes de poder asignarlos *****")


    #if r == 4:
    #if r == 5:
    #if r == 6:

# getear la lista de empleados de lista_empleados
            # for empleado in lista_empleados:
            #     empleado.get_E()   
# getear la lista de empleados en un sector
print(sector_1.getEmpleados())
