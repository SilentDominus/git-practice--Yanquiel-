import json
from core import *
FILE_PATH = r"D:\Yanquiel\Programacion\Proyectos VSC\DevForge\Lista_de_Tareas\datos.json"

Gestor = Gestor_De_Tareas()
def guardarDatos():
    data = [T.convertirDiccionario() for T in Gestor.getLista()]
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
        
def cargarDatos():
    try:
        with open(FILE_PATH, "r") as File:
            diccionarios = json.load(File)
        if len(diccionarios) == 0:
            print("!!!!!! No hay archivos guardados !!!!!")
        else:
            for D in diccionarios:
                Gestor.setLista(D['Descripcion'], D['Estado'])   
    except:
        print("!!!!!! No hay archivos guardados !!!!!")
        return []     