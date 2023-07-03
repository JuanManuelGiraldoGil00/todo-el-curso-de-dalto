#programa que tomo las tres notas de un estudiante y diga  la nota final del curso
# tenga en cuenta que la primera y seginda nota valen 30% y la ultima vale el 40% 

# def clacular_nota_final(nota1,nota2,nota3):
#     return round((nota1*0.3) +(nota2*0.3)+(nota3*0.4),2)

# nota1= float(input(" por favor registre su primera nota :"))
# nota2= float(input(" por favor registre su segunda nota :"))
# nota3= float(input(" por favor registre su tercera nota :"))

# nota_final=clacular_nota_final(nota1,nota2,nota3)
# print(f"la nota  final de estudiante es de : {nota_final}")

#--------------------------------------------------------------

#programa que calcule  el iva de una compra, siendo el iva del 19%sobre el valor total de la compra 
#la primera parte la hice ami estilo y salio bien lo unico que se puede detallar es que solo estaba calcculando de una el iva y ya lo demas bien a y en la multiplicacion tambien me equivoque
# def calculando_iva(p):
#     iva= (p *0.19 )
#     return iva
# compra=float(input("cual fue el valor total de su compra : "))
# iva=calculando_iva(compra)

   
   
# valor_del_iva=calculando_iva(compra)
# print(f"el valor de la compra sin iva es de :{compra}")
# print(f"este es el valor del iva  en la compra : {compra + iva}")   
       
#-------------------------------------------------------------------------------------------------------

#progarma que calcula la tabla de multiplicar de cualquier numero entero dado pr el usuario debe calcular la tabla desde 0 hasta el 12    
#todo esto lo hiso el 

         #aqui se crea la funcion       
# def tabla_del_numero(n1,n2):
#     #aqui el le da como retornar a return primero convierte a srting n1  despues el signo de multiplicar despues el signo de = y por ultimo multiplica 
#     #n1 y n2 y los convierte a string
#     return str(n1) + "*"+ str(n2) + "="+ str(n1*n2)

# # aqui se le pide un numero cualquiera al usuario y este es el que va definido en los parametros para que sea el n1  del string
# numero_dado=int(input("porfavor ingrese el numero de su preferencia :"))       

# # aqui el bucle for va a recorre desde el 0 hasta el 12 recordar que la (i) es una secuencia de numero que se va definir en el parentesis de range(0,13) desde cero hasta 12
# for i in range(0,13):
#     #aqui imprimimos por pantalla la funcion con sus parametros n1 que esta definido como el numero dado y i que es la linea de numeros que va desde 0 hasta 12 
#     #y la i es n2 convertido a srting 
#     print(tabla_del_numero(numero_dado,i))
    
#--------------------------------------------------------------------------------------------------

# programa que valide si una contraseña espesificada(oseaque la da el usuario) es segura 
#la contraseña segura debera tener mas 8 caracteres tener una letra  en mayscula y tener un numero 



#no puede le trate como 2 horas 
# def validar_contraseña(con_escrita):
    
  
    
    
#     caracteres=len(con_escrita)
#     if caracteres >= 8:  True
#     else:
#         False
    
#     for i in range(len(con_escrita)):
#         if con_escrita[i].isupper():
#             True
#         else:
#             False
   
            
#     if con_escrita[i].isnumeric():True
            
            
#     if   caracteres and i:
#         return True
#     else:
#         return False
                 
        
    
# con_escrita=input(" por favor ingrese una contraseña: ")
# contraseña_verificada= validar_contraseña(con_escrita)
# if contraseña_verificada:
#     print("la contraseña es segura")
# else:
#     print("la contraseña no es segura ")

# la de el 
#lo que utilizo el  print(len(hola))
#print("a".isupper())
#print("a".isnumeric())
#cadena= "hola
# for i in range(len(candena)):
#    print(cadena[i])


# def comprobar_contraseña(password):
#     largo=False
#     mayus=False
#     numer=False
#     if len(password) >8:
#         largo=True
#     for i in range(len(password)):
#         if password[i].isupper():
#             mayus=True
            
#         if password[i].isnumeric():
#             numer=True
#     if largo and mayus and numer:
#         return True
#     else:
#         return False
                
# password= input("ingrese una contraseña : ")
# verificacion= comprobar_contraseña(password)            
# if verificacion:
#     print("la contraseña es segura ")
# else:
#     print("la contrasela no es segura ")                  

#_-----------------------------------------------------------------------------------------------------------------------             

        
# progama que valide si un numero  se primo 
        
    
# def es_primo(puesto):
#     if puesto <=1:
#         return False
  
#     elif puesto == 2:
#         return True
  
#     else:
#       for i in range(2,puesto):
#           if puesto % i == 0:
#                 return False
#     return True
 
    
        
     

        
# for i in range(1,101):
#     print(i,"",es_primo(i))    

#--------------------------------------------------------------------------------------------------------------------



# def nuevo_salario(inc):
#     sal_antiguo= float(input(" porfavor ingres su salario : "))
#     ecuacion= sal_antiguo *inc/ 1000 *10 
#     total=sal_antiguo + ecuacion
#     return f"este es su salario antiguo {(sal_antiguo)} y este es su nuevo salario con el incremento {(total)}" 

  
    
# incremento= nuevo_salario(13)
#print(incremento)


# este lo hise yo mismo 
#-----------------------------------------------------------------------------------------------------------------------
    
# este lo hice bien lo que paso es que el pedia un programa que escogiera  y diera con la ecuacion para los 2 numeros pero esta bien 

# def operaciones(n1,n2):
#     n1=float(input(" por favor deme su primer numero : "))
#     n2= float(input(" por favor deme su segundo numero : "))
#     suma= (f" esta es la suma de los 2 numeros{ n1 + n2}")
#     resta= (f" esta es la resta de los 2 numeros {n1 - n2}")
#     multi= (f" esta es la multiplicacion de los 2 numeros {n1 * n2 }")
#     divi= (f" estaes la divicion entre los 2 numeros {n1 / n2}") 
#     expo= (f" esta es la esponeciacion entre  los 2 numeros {n1 ** n2}")
#     return suma,resta,multi,divi,expo

# resultado= operaciones(1,8)
# print(resultado)
# def sum(a,b):
#     return a + b 

# def resta(a,b):
#     return a -b

# def multiplicacion(a,b):
#     return a * b
# def divicion(a,b):
#     return a / b
# def exponeciacion(a,b):
#     return a ** b

# def raiz(a,b):
#     return a ** (1/b)

# n1=float(input(" por favor deme su primer numero : "))
# n2= float(input(" por favor deme su segundo numero : "))
# print("1.suma")
# print("2.resta")        
# print("3.multiplicacion")    
# print("4.divicion")    
# print("5.exponenciacion")
# print("6.raiz ")
# opc=float(input(" elija la opcion que nesecite :"))

# if opc == 1:
#     print(n1,"+",n2,"=", sum(n1,n2))
    
# elif opc==2:
#     print(n1,"-",n2,"=", resta(n1,n2))
    
    
# elif opc==3:
#     print(n1,"*",n2,"=", multiplicacion(n1,n2))    
    
# elif opc==4:
#     print(n1,"/",n2,"=", divicion(n1,n2))    
               
    
# elif opc==5:
#     print(n1,"**",n2,"=", exponeciacion(n1,n2))    
        
           
# elif opc==6:
#     print(n1,"^1/",n2,"=", raiz(n1,n2))    
 
 
#----------------------------------------------------------------------------------------------------------------------------------

"programa que convierta una unidad  en dias, hora,minutos, y segundos "


# def calcularsegundos(dias,horas,minutos,segundos):
#     segundos_totales= 0
#     segundos_totales += segundos
#     segundos_totales += minutos * 60
#     segundos_totales += horas* 60* 60
#     segundos_totales += dias  * 24 * 60 *60
#     return segundos_totales

# dias=int(input( "ingrese la cantidad de  dias :"))
# horas=int(input(" ingrese la cantidad de horas :"))
# minutos=int(input(" ingrese la cantidad de minutos :"))
# segundos=int(input(" infrese la cantida de segundos :"))

# segundos_totales= calcularsegundos(dias,horas,minutos,segundos)
# print(f" este es la cantidad de segundos  en el tiempo que ingreso  : {segundos_totales}")


# este lo hiso el el 
#--------------------------------------------------------------------------------------------------
        
        
"""programa que calcule  el imc de un a persona dada su peso y estaturay luego indicar su nivel de peso asi
imc       clasificasion
------------------------

<18.5  ->  bajo peso

18.5 - 24.9 ->normal 
25.0 - 29.9 ->sobre peso
30.0 - 34.9 -> obesidad I
35.0 - 39.9 ->obesidad II
40.0 - 49.9 -> obesidad III
  > 58.8       -> obesidad IV


imc =  peso / (estatura * estatura )
"""
            
# estatura= float(input(" ingrese su estatura :"))
# peso=float(input("ingrese su peso : "))
# imc= float(peso / (estatura*estatura))



# asi iva  bien pero no medaba  ningun resutado 
# if imc== 18 >= 24:
#      print("tienes un peso normal ")
    



# elif  25.0 <= imc <= 29.9:
#     print(" tienes un poco de sobres peso ")
    
# elif imc == 30.0 <= 34.9:
#     print("tienes obesidad I")
    
# elif imc == 35.0 <= 39.9:
#     print("tienes obesidad II")        

# elif imc == 40.0 <= 49.9:
#     print("tienes obesidad III") 
    
           
# elif imc== 50.0 <= 60.0 :
#    print("TIENES OBESIDAD IV")
    
    
# else:
#    print("balla al hospital ahora ")  
    


# def calcularImc(p,a):
#     return p / (a*a)

# def nivel_de_peso(imc):
#     if imc <18.5 :
#         return "bajo peso "
#     elif  18.5<= imc <= 24.9:
#      return("tienes un peso normal ")
#     elif  25.0 <= imc <= 29.9:
#      return(" tienes un poco de sobres peso ")
    
#     elif 30.0<= imc <= 34.9:
#      return("tienes obesidad I")
    
#     elif  35.0<= imc <= 39.9:
#      return("tienes obesidad II")     
       
#     elif  40.0<= imc  <= 49.9:
#      return("tienes obesidad III") 
    
#     elif imc >= 50 :
#      return("TIENES OBESIDAD IV")
 
# estatura= float(input(" ingrese su estatura :")) 
# peso=float(input("ingrese su peso : "))
# print(" su nivel de peso es : ", nivel_de_peso(calcularImc(peso,estatura)))
                
                
                                
 
    
    


    











   
    
    
    
    
    
    
    
