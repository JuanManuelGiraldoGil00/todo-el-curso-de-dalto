#creando una funcion de 3 parametros 

# def frase(nombre,apellido,adjetivo):
#     return f"hola {nombre} {apellido},sos un capo {adjetivo}"


# # utilizando keywords arguments
# frase_resultante= frase( adjetivo="macho", nombre="juan", apellido="giraldo")
# print(frase_resultante)


# creando la misma funcion  con parametros opcional(adjetivo=) y  un valor por defecto(tonto )
def frase(nombre,apellido,adjetivo= "toro"):
    return f"hola {nombre} {apellido},sos un  {adjetivo}"

frase_resultante= frase(nombre="juan", apellido="giraldo", adjetivo="perro")
print(frase_resultante)








