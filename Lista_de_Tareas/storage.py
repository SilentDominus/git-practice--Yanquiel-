import json
from Lista_de_Tareas.core import *
FILE_PATH = "datos.json"

Gestor = Gestor_De_Tareas()
def guardarDatos():
    data = [T.convertirDiccionario() for T in Gestor.getLista()]
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
        
def cargarDatos():
    pass