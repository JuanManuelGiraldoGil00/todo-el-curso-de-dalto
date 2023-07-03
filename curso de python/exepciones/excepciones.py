#creando funcion que suma numeros 
def sumar_dos():
    #iniciando el bucle
    while True:
        #pidiendo numeros    
     a=input("numero 1: ")
     b= input("numero 2: ")
    #intentando covertirlos a enteros y sumarlos 
     try:
      resultado= int(a) + int(b)
      
      #si lanzo una excepcion, pedirle que reingrese los datos
     except Exception as e:
         print("te pedi un numero salame, no te hagas el gracioso")
         print(f" ERROR :{e}")
     #si todo salio bien terminamos con el bucle 
     else:
         break   
     finally:
         print("manejo de excepcion finalizado")
    
    # mostrando el resultado
    
    return resultado


print(sumar_dos())
