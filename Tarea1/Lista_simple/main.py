from lista_simple import ListaSimpleEnlazada

lista = ListaSimpleEnlazada()
print("******CREACION DE LA LISTA******")
lista.agregar_ultimo(12)
lista.agregar_ultimo(2)
lista.agregar_ultimo(25)
lista.agregar_ultimo(19)
lista.agregar_ultimo(30)
lista.recorrido()

print("******LISTA CON EL PRIMER Y ULTIMO ELEMENTO BORRADO******")
lista.eliminar_inicio()
lista.eliminar_ultimo()
lista.recorrido()


print("******LISTA CON MAS ELEMENTOS AGREGADOS******")
lista.agregar_inicio(12)
lista.agregar_ultimo(30)
lista.agregar_ultimo(40)
lista.agregar_ultimo(670)
lista.agregar_ultimo(16)
lista.recorrido()
