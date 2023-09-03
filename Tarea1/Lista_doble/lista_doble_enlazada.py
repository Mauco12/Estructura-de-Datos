#IMPORTANDO LA CLASE NODO 
from nodo import Nodo

class ListaDoblementeEnlazada():
    
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
     
    #METODO PARA MOSTRAS QUE LA CLASE ESTA VACIA   
    def Empty (self):
        return self.first == None
    
    #METODO PARA AGREGAR ELEMENTOS AL FINAL DE LA LISTA
    def Add_last(self,value):
        if self.Empty ():
            self.first = self.last = Nodo (value)
        else:
            aux = self.last
            self.last = aux.next = Nodo(value)
            self.last.back = aux
        self.size += 1
        
    #METODO PARA AGREGAR ELEMENTOS AL INICIO DE LA LISTA   
    def Add_first(self,value):
        if self.Empty():
            self.first = self.last = Nodo(value)
        else:
            aux = Nodo(value)
            aux.next = self.first
            self.first.back=aux
            self.first = aux
        self.size += 1
        
    #METODO PARA ELIMINAR ELEMENTOS AL INICIO DE LA LISTA  
    def Remove_first(self):
        if self.Empty():
            print("La lista es vacia")
        elif self.first.next == None:
            self.first = self.last = None
            self.size=0
        else:
            self.first = self.first.next
            self.first.back = None
            self.size -= 1
    
    #METODO PARA ELIMINAR ELEMENTOS AL FINAL DE LA LISTA        
    def Remove_last(self):
        if self.Empty():
            print("La lista es vacia")
        elif self.first.next == None:
            self.first = self.last = None
            self.size = 0
        else:
            self.last = self.last.back
            self.last.next = None
            self.size -= 1
    
    #METODO PARA MOSTRAR TODOS LOS ELEMENTOS DE LA LISTA EMPEZANDO POR EL PRIMER ELEMENTO     
    def Print_data(self):
        aux = self.first
        while aux != None:
            print(aux.value)
            aux = aux.next
    
    #METODO PARA MOSTRAR TODOS LOS ELEMENTOS DE LA LISTA EMPEZANDO POR EL ULTIMO ELEMENTO Y RETROCEDIENDO        
    def Print_dataBack(self):
        aux =self.last
        while aux != None:
            print(aux.value)
            aux = aux.back
                

            
    