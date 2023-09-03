
#IMPORTACION DE LA CLASE NODO
from nodo import Nodo

class ListaSimpleEnlazada():
    
    def __init__(self):
        self.primero = None
        self.ultimo = None
     
    #METODO QUE MUESTRA SI LA LISTA ESTA VACIA   
    def vacia(self):
        return self.primero == None
    
    #METODO QUE AGREGA DATOS A LA LISTA
    def agregar_ultimo(self,dato):
        if self.vacia() == True:
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
    
    #METODO QUE AGREGA DATOS AL INICIO DE LA LISTA        
    def agregar_inicio(self,dato):
        if self.vacia == True:
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux 
    
    #METODO PARA ELIMINAR DATOS AL INICIO DE LA LISTA
    def eliminar_inicio(self):
        self.primero = self.primero.siguiente   
    
    #METODO PARA ELIMINAR DATOS AL FINAL DE LA LISTA        
    def eliminar_ultimo(self):
        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux = aux.siguiente
        aux.siguiente = None
        self.ultimo = aux
        
    #METODO QUE MUESTRA LA LISTA COMPLETA
    def recorrido(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente
