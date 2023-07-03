import re

texto= """hola maestro, esta es la cadena 1. como estas mi capitan
Esta es la segunda linea 3224333 de texto.
hola men como bbb  a andas
Esta es la final definitiva mi capitan"""

#haciendo una busquedo simple usando el search este busca mas que todo por indice 
resultado= re.search("esta",texto)

#esta te muestra lo que encotro dentro de una lista 
resultado2= re.findall("esta",texto)

#esta se utiliza para buscar comosea  que este escrita
resultado3= re.findall("esta",texto,flags=re.IGNORECASE)

#\vvd -> busca digitos numericos del 0 -9
resultado4=re.findall(r"\d",texto)


#\D -> busca todo menos digitos numericos del 0 -9
resultado5=re.findall(r"\D",texto)


#\w -> busca careteres alfanumericos [a-z A-Z 0-9 _]
resultado6= re.findall(r"\w",texto)

#\s -> busca espacios en blanco -> espacios,tabs, saltos de line  
resultado7= re.findall(r"\W",texto)

#\s -> busca  todo menos espacios en blanco -> espacios,tabs, saltos de line  
resultado8= re.findall(r"\W",texto)

#\. -> busca todo menos saltos de linea 
resultado9= re.findall(r".",texto)


#\n -> busca saltos en linea 
resultado9= re.findall(r"\n",texto)

#\ -> cancelar  caracteres especiales, cacelando la funcio del punto y buscando puntos 
resultado10=re.findall(r"\.",texto)

# armando una cadena que busque  un numero, seguido de un punto y un espacio en linea 
resultado11=   re.findall(f"\d\.\s",texto)



#buscando el comienzo de una linea 
#^ -> busca el comienzo de una linea buscando  hola al principio de la linea 
# flags=re.M activa multunilininea 
resultado12=re.findall(f"^hola",texto,flags=re.M)


# $ -> busca el final de una linea
resultado14= re.findall(f"esta%",texto,flags=re.M)


#{n} -> busca n cantidad de veces el valor de la isquierda
resultado15= re.findall(r"\d{3}",texto)

# {n,m} -> busca al menos n, como maximo m
resultado16= re.findall(r"\d{2,4}",texto) 


## {n,m} -> busca al menos n, como maximo m 
resultado17= re.findall(r"\d{2,4}|hola",texto) 


print(resultado17)

