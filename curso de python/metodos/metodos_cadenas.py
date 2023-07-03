cadena1= "hola,soy,juan"
cadena2= "bienvenido juan"

# metodos(se da primero el dato que es cadana1 despues el punto y por ultimo el metodo que es uppr y se cierra con estos()

# upper manda todo a mayuscula
mayus=cadena1.upper() 

#manda todo a minuscula
minus=cadena1.lower() 

#primera letra en mayuscula
primera_letra_en_mayus= cadena1.capitalize()


# buscamos una cadena en otra cadena, si no hay coincidenciasnos devuelve -1
busqueda_find= cadena1.find("soy")

# buscamos un a cadena dentro de otra cadena, si no hay coincidencias nos lnsa una excepcion osea nos devuele un error

busqueda_index= cadena1.index("h")

#si es numerico, devolvemos true, si no devolvemos false

es_numerico= cadena1.isnumeric()

# si es alfa numerico devolvemos true, si no devolvemos false(solo es alf numerico desde la A ala Z y sin espacios )

es_alfanumerico= cadena1.isalpha()

#buscamos una cadena en otra cadena, develve la cantidad de veces que coincida (lo que aparece repetido )
contar_coincidencias= cadena1.count("H")

#contamos cuantos caracteres tine una cadena
contar_caracteres= len(cadena1)

# verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True

empieza_con= cadena1.startswith("hol") 

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True

termina_con= cadena1.endswith("an") 

#rempplasa un pedaso de la cadena dada, por otra dada (osea da remplaza una letra que esta dentro de la variable y la remplaza por la nueva )
cadena_nueva= cadena1.replace(","," ")



# separar cadenas con la que le pasemos  y nos devuelve una lista 
cadena_separada= cadena1.split(",")

print(cadena_separada[1])
