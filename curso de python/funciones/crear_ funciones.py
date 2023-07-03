# creando una funcion simple( osea eso que esa en saludar  si lo ponemos varias veses en lineas de codigo se va ejecutar lo mismo al menos que lo cambiemos)
# def saludar():
#     print("hola juan como andas men ?")
# # ejecutando la funcion simple     
# saludar()    


#creando una funcion que tenga parametros(osea una variable asi como abajo)

# def saludar(nombre,sexo):
#     sexo= sexo.lower()
#     if (sexo == "mujer"):
#         adjetivo="reina"
#     elif (sexo == "hombre"):
#         adjetivo="titan"
#     else:
#         adjetivo= "marica"
#     print(f"hola {nombre}, {adjetivo} como andas men ?")    
           
        

# saludar("juan","hombre")
# saludar("maria","mujer")
# saludar("esteban"," no binario ")

#  crear una funcion que nos retorne valores aleatorios para contraseñas y demas,  si queremos hacer algo fuera de la funciones utilizamos return  para poder trabajar fuer de las funciones 
def crear_contraseña_ramdom(num):
    chars= "gbsdbjbcdhb"
    num_entero= str(num)
    num= int (num_entero[0])
    c1=num -2
    c2= num
    c3= num-5 
    contraseña= f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

# desempaquetando la funcion num con primer_numero 
password,primer_numero=crear_contraseña_ramdom(5556)

# mostrando los resultados obtenidos y los datos utilixzados para obtenerlo 
print(f"tu contraseña nueva es : {password}")
print(f"el numero utilizado para crearla fue  : {primer_numero}")











