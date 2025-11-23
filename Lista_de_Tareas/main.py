from core import * 
from storage import *

flag = True
while(flag):
    print("--------------Gestor de tareas--------------")
    print("Que desa hacer?")
    print("1-Agregar Tarea")
    print("2-Ver Tareas")
    print("3-Marcar Tarea como completada")
    print("4-Eliminar Tarea")
    print("5-Guardar datos")
    print("6-Cargar datos")
    print("7-Salir")
    eleccion = input("Elija una opcion: ")
    
    if int(eleccion) < 1 or int(eleccion) > 7:
        print("\n!!!!!!!FUERA DE RANGO!!!!!!")
    elif eleccion == "7":
        flag = False
        
    gestor = Gestor_De_Tareas()
    Opciones = {
    "1": lambda: gestor.agregarTarea(),
    "2": lambda: gestor.verTareas(),
    "3": lambda: gestor.marcarCompletada(),
    "4": lambda: gestor.eliminaTarea(),
    "4": lambda: guardarDatos()
    }

    action = Opciones.get(eleccion,lambda: print(" "))
    action()
    
    


        
        





