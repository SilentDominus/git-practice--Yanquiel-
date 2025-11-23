class Gestor_De_Tareas:
    listaT = list()
    def __init__(self):
        pass
        
    def agregarTarea(self,Tarea):
        self.listaT.append(Tarea)
                
        
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.estado = False
        

        