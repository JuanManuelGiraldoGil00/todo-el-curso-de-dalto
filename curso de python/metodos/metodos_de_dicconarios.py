diccionario= {
    "nombre":"juan",
    "apellido":"giraldo",
    "trabajo": "tendero",
    "edad": 18 
}
#señanlar o decir como comentaron las keys de el diccionario 
claves= diccionario.keys()

#este nos permite ver el valor de key  y con este metodo el programa no manda excepciones

valor_el_value= diccionario.get("nombre")

#eliminando todo el diccionario
#diccionario.clear()

#eliminando un elmento del diccionario 
diccionario.pop("trabajo")


# obteniendo un elemento dict_items iteriable
diccionario_iteriable= diccionario.items()

print(diccionario_iteriable)