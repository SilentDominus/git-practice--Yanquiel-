class Gestor_De_Tareas:
    listaT = list()
    def __init__(self):
        pass
        
    def agregarTarea(self):
        descripcion = input("Introduzca la tarea: ")
        tarea = Tarea(descripcion)
        self.listaT.append(tarea)
        
    def verTareas(self):
        posicion = 1
        print("\nLas tareas son: ")
        for T in self.listaT:
            print(f"Tarea {posicion}- descripcion: {T.getdescripcion()}")
            print(f"         Estado: {'completado' if T.getestado() else 'No Completada'}")
            posicion += 1
            
    def marcarCompletada(self):
        marcar = int(input("Diga el numero de la tarea completada: "))
        if marcar > len(self.listaT) or marcar < 1:
            raise Exception("El numero esta fuera de rango")
        else:
            self.listaT[marcar-1].setestado(True)
        
    def eliminaTarea(self):
        borrar = int(input("Seleccione el numero de la tarea a borrar: "))
        if borrar > len(self.listaT) or borrar < len(self.listaT):
            raise Exception("El numero esta fuera de rango")
        else:
            self.listaT.pop(borrar-1)
            
    def getLista(self):
        return self.listaT
            
    
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.estado = False
        
    def getestado(self):
        return self.estado
    
    def setestado(self, estado):
        self.estado = estado
        
    def getdescripcion(self):
        return self.descripcion
    
    def convertirDiccionario(self):
        diccionario = {
            "Descripcion": self.descripcion,
            "Estado": self.estado
        }
        return diccionario
    

        

        