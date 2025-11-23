class Gestor_De_Tareas:
    listaT = list()
    def __init__(self):
        pass
        
    def agregarTarea(self,Tarea):
        self.listaT.append(Tarea)
        
    def verTareas(self):
        posicion = 1
        print("\nLas tareas son: ")
        for T in self.listaT:
            print(f"{posicion}-{T}")
            posicion += 1
            
    
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.estado = False
        

        