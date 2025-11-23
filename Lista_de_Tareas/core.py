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
            
    def marcarCompletada(self):
        marcar = int(input("Diga el numero de la tarea completada: "))
        self.listaT[marcar].setestado(True)
            
    
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.estado = False
        
    def getestado(self):
        return self.estado
    
    def setestado(self, estado):
        self.estado = estado
        

        