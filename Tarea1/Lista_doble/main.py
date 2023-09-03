from lista_doble_enlazada import ListaDoblementeEnlazada

lista = ListaDoblementeEnlazada()

print("******AGRENGADO DATOS DE MANERA ORDENADA******")
lista.Add_last(12)
lista.Add_last(56)
lista.Add_last(21)
lista.Add_last(10)
lista.Add_last(11)
lista.Print_data()

print("******LISTA VOLTEADA******")
lista.Print_dataBack()

print("******LISTA CON EL PRIMER Y ULTIMO ELEMENTOS BORRADOS******")
lista.Remove_first()
lista.Remove_last()
lista.Print_data()


print("******LISTA CON LOS PRIMEROS TRES ELEMENTOS BORRADOS******")
lista.Add_first(12)
lista.Add_last(11)
lista.Remove_first()
lista.Remove_first()
lista.Remove_first()
lista.Print_data()

print("******LISTA CON LOS 3 ULTIMOS ELEMENTOS BORRADOS******")
lista.Add_first(21)
lista.Add_first(56)
lista.Add_first(12)
lista.Remove_last()
lista.Remove_last()
lista.Remove_last()
lista.Print_data()

print("******AGREGANDO DATOS EN EL INICIO DE LA LISTA*****")

lista.Add_first(123)
lista.Add_first(122)
lista.Add_first(45)
lista.Add_first(21)
lista.Add_first(10)
lista.Add_first(11)
lista.Print_data()
