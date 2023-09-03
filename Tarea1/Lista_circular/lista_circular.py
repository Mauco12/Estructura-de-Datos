#IMPORTANDO LA CLASE NODO
from nodo import Nodo

#CREANDO LA CLASE DE LA LISTA
class ListaCircular():
    
    def __init__(self):
        self.first = None
        self.last = None
    
    #METODO QUE MUESTRA SI LA LISTA ESTA VACIA
    def Empty(self):
        return self.first == None
    
    #METODO PARA AGREGAR ELEMENTOS AL INICIO DE LA LISTA
    def Add_first(self,value):
        if self.Empty():
            self.first = self.last = Nodo(value)
            self.last.next = self.first
        else:
            aux = Nodo(value)
            aux.next = self.first
            self.first = aux
            self.last.next = self.first
    
    #METODO PARA AGREGAR ELEMENTOS A LA LISTA        
    def Addd_last(self,value):
        if self.Empty ():
            self.first = self.last = Nodo(value)
            self.last.next = self.first
        else:
            aux = self.last
            self.last = aux.next =Nodo(value)
            self.last.next = self.first
    
    #ELIMINAR ELEMENTOS AL PRINCIPIO DE LA LISTA
    def Remove_first(self):
        if self.Empty():
            print("La lista es vacia")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.last.next = self.first
        
    #ELIMINAR ELEMENTOS DE LA LISTA
    def Remove_last(self):
        if self.Empty():
            print("La lista esta vacia")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            aux = self.first
            while aux.next != self.last:
                aux = aux.next
            aux.next = self.first
            self.last=aux
            
             
    
    #Refactory para que no muestre error cuando la lista este vacia
    def Print_data(self):
        aux = self.first
        while aux:
            print (aux.value)
            aux = aux.next
            if aux == self.first:
                break
    