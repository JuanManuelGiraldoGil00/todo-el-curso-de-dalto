numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


# creando uan funcion lambda para multiplicar por 2 
multiplicar_por_dos= lambda x : x*2

# #creando funcion comun que diga si es par o no 
# def es_par(num):
#     if (num % 2 == 1):
#         return True
    
#usando filter como una funcion comun
# numeros_pares= filter(es_par,numeros)    
# print(list(numeros_pares))

#creando lo mismo que antes pero con lambda

numeros_pares= filter(lambda numero:numero%2 == 0,numeros )
print(list(numeros_pares))