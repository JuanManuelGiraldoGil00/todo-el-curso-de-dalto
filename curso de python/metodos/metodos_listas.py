#creando una lista con list y recuerda que se crean usando doble parentesis (())
#lista2=list(("juan","manuel"))
lista=[9,27,34]

#devuelve la cantidad de elmentos de una lista 
len(lista)

#agregando una elmento ala lista 

lista.append(67)

#agregando un elmentoa ala lista en un indice especifico 
lista.insert(0,55)
print(lista) 
#agregando varios elmentos ala lista ose agrega una lista denrto de otra lista 

lista.extend([9,2050])

#eliminando un elmento de una lista (por su indice)

lista.pop(-3)#  -1 elimina el ultimo de la lista, el -2 el penultimo de la lista y asi susecivamente

# removiendo un elmento  de la lista por su valor  osea por su nombre
lista.remove(34)

# eliminando toso os elemntos de la lista 
#lista.clear()


#organisa todo los numero dentro de una lista pero si encutra letras o strings nos manda error

lista.sort(reverse=True)#si usamos la funcion de reverse  nos da vuelta y ahora serian de mayor a meno y no de menor a mayor

#invirteindo los elmentos de una lista (es como usar reverse=True  en un metodo por fuera)
lista.reverse()






