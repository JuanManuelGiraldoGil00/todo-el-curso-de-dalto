# creando una funcion que nos devuelve los numeros primos

# entre cero y el numero que le pasemos

# def numeros_primos(numero):
#     n_primos=[]
#     for primo in numero:
#         if primo == 1:
#          numero_pasado= int(input(" pase el numero de su agrado "))
#          primos= ( numero_pasado)
#     primos.append(n_primos)

#     sus_numeros_pri_= (n_primos)
#     return sus_numeros_pri_

# sus_numeros_prim = numeros_primos(5)


# lo trate de hacer pero no se pudo
#------------------------------------------------------------------------

# este es el de dalto 
# crear una  funcion que verifique si un numero es primo
def es_primo(num):
    
    # verificamos que el numero  pasado no puede dividirse por ningun numeo entero 2 y el mismo numero - 1 
    for i in range(2,num-1):
        
        #si es divisible por uno retomamos false y termina el bucle
        if num % i == 0: return False
        #si termina el bucle entoses ; significa que el numero no fue dividible entonces es primo  
        return True
    
    
# retonanado una funcion que retorne una lista con todos los numeros primos     
def primos_hasta(num):
    # creamos una lista 
    primos=[]
    for i in range(2,num + 1):  
    # verificamos si el valor es primo 
        resultado= es_primo(i)
        #en caso de que si lo sea  lo agregamos a la lista 
        if resultado == True:primos.append(i)
    # devolvemos la lista     
    return primos
    
 #creamos el resultado llamando ala funcion y lo mostramos            
resultado= primos_hasta(333)
print(resultado)    
    
    
    
    
        