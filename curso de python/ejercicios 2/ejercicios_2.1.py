# pedir el nombre y las edades alos compañeros 


# funcion para  obtener al asistente  ya al profesor segun la edad 
def obtener_compañeros(cantidad_de_compañeros):
    
#creando una lista con los compañeros     
  compañeros= []

#ejecutando un for para pedir informacion de cada compañero
  for i in range(cantidad_de_compañeros):
     nombre= input(" ingrese el nombre del compañero :")
     edad =  int(input(" ingrese la edad del compañero :"))
     alumnos= (nombre,edad)
     
     #agregando la informacion ala lista 
     compañeros.append(alumnos)
     
  # ordenandolos de menor a mayor    
  compañeros.sort(key=lambda x:x[1])
  
  #compañeros [x] devuelve una tupla con (nombre,edad ) y despues accedemos al nombre 
  # para definir al asistente y al profesor 
  asistente= compañeros [0][0]
  profesor =  compañeros[-1][0]
  
  
  # retonamos una tupla 
  return asistente, profesor 

#desenpaquetamos lo que nos retorna la funcion 
asistente,profesor= obtener_compañeros(5)

#mostrando el resultado
print(f" el profesor es : {profesor} y el asistente es :{asistente}")
   



