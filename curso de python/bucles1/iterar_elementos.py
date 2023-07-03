
animales= ("gato","perro","loro","cocodrilo")
numeros=(44,55,66,78)

# recorriendo la lista de animales 
for animal in animales:
  print(f"ahora la variable animal es igual a : {animal}")
  
  
# recorriendo la lista de numero y multiplicando por 2  
for numero in numeros:
    print("---------")
    resultado= numero *2
    print(resultado)
    
    
# iterando  dos o las que allan  listas  del mismo tamaño  al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f" recorriendo lista 1 : {animal}")
    print(f" recorriendo lista 2 :  {numero}")
    
    
# froma no optima de recorrer una lista  y no funciona para conjuntos 
for numero in range(len(numeros)):
    print(numeros[numero])
    
    
# forma correcta de recorrer una lista 

for numero in enumerate(numeros):
    indice = numero[0]
    valor= numero [1]
    print(f" el indice es : {indice} y el valor es : {valor}")
    
    
# usando for/else 
for numero in numeros:
    print(f"ejecutando el ultimo bucle, el valor actual:{numero}")    
else :
    print("el bucle termino ")
    
    
# todo lo anterior  funciona exactamente igual  para las tuplas, listas y conjuntos 

    
    
    


  
  