from lista_circular import ListaCircular
#CREACION DE LA LISTA
lista = ListaCircular()
#AGREGANDO ELEMENTOS A LA LISTA
print("******CREANDO LA LISTA******")
lista.Addd_last(10)
lista.Addd_last(56)
lista.Addd_last(78)
lista.Addd_last(90)
lista.Print_data()

#ELIMINANDO EL ULTIMO Y PRIMER ELEMENTO DE LA LISTA
print("******ELIMINANDO EL ULTIMO Y PRIMER ELEMENTO DE LA LISTA******")
lista.Remove_last()
lista.Remove_first()
lista.Print_data()

#AGREGANDO EL PRIMER Y ULTIMO VALOR
print("******#AGREGANDO EL PRIMER Y ULTIMO VALOR******")
lista.Add_first(10)
lista.Addd_last(90)
lista.Print_data()