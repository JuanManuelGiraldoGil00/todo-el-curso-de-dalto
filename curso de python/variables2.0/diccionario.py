# creando un diccionario con dict ()
diccionario= dict(nombre="juan",apellido="giraldo")



# las listas no puenden ser claves y usamos frozenzet para meter conjuntos 
diccionario={frozenset(["dalto","rancio"]):"jajaj"}
print(diccionario)

# crendo un diccionario co formkeys y que cada letra sea una key y el segundo su value 
diccionario0= dict.fromkeys("abcd","estoy aprendiendo")
print(diccionario0)

#creando diccionarios con fromkeys : valor por defecto :none 
diccionario1= dict.fromkeys({"nombre","apellido"})
print(diccionario1)

#creando diccionarios con fromkeys() cambiando el valor por defecto a nose
diccinario2= dict.fromkeys({"nombre","apellido"},"no se")
print(diccinario2)



















