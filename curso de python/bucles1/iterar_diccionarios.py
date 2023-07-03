diccionario = { 
    "nombre":"soyjuan",
    "trabajo" : "programador",
    "esta haciendo ": "nada",
    "edad": 18

}

# recorriendo un diccionario con items() para obtener las claves  
for key in diccionario:
    
    print(f"la clave es : {key}")

#recorriendo un diccionario con items() para obtener la clave y el valor 
for datos in diccionario.items():
    key= datos[0]
    value=datos[1]
    print(f"la clave es : {key} y el valor es :{value}")
    







