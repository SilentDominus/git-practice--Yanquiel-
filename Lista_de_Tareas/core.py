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
        if marcar > range(self.listaT)-1 or marcar < range(self.listaT)-1:
            raise Exception("El numero esta fuera de rango")
        else:
            self.listaT[marcar].setestado(True)
        
    def eliminaTarea(self):
        borrar = int(input("Seleccione el numero de la tarea a borrar"))
        if borrar > range(self.listaT)-1 or borrar < range(self.listaT)-1:
            raise Exception("El numero esta fuera de rango")
        else:
            self.listaT.pop(borrar-1)
            
    
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.estado = False
        
    def getestado(self):
        return self.estado
    
    def setestado(self, estado):
        self.estado = estado
        

        