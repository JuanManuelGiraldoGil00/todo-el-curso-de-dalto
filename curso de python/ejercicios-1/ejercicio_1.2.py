#ejercicio echo por mi que despues arregle el orden pero como lo tenia tambien me hubiera contestado como lo hiso dalto
#lepedimos al usuario que nos diga una frase (o varias )
usuario= input("señor deme una frase y le voy adecir cuanto traadaria en decirla y cuantas palabras dijo: ")

#creamos una lista con todas de la frase (se  separan cada vez que haya un espacio en blanco)
palabras_con_espacios= usuario.split(" ")

#usamos len() para saber la cantidad de elmentos que tine la lista 
palabras_de_la_frase=len(palabras_con_espacios)

#la respuesta si se demora mas de un minuto en decir la frase 
if (palabras_de_la_frase/2) > 60:
   
    print("para flaco tampoco de pedi un testamento ")
    
#calculamos cuanto tradaria en decir  las palabras y se lo decimos 
print(f"usted dijo esta cantidad de palabras{palabras_de_la_frase} y setardaria {palabras_de_la_frase/2}segundos en decirla  ")
print("-----------")
print(f"estos tardaria dalto en decir esa misma frase {palabras_de_la_frase*100//2*1.3/100} segundos en decirlo ")



    
    
# ejercicio echo por dalto     
#frase= input("decime una frase y te calculo cuanto tardarias si tuvieras que desirla : ")
#palabras_separadas= frase.split(" ")
#cantidad_de_palabras=len(palabras_separadas)
#print(f"dijiste {cantidad_de_palabras} palabras, y tradarias {cantidad_de_palabras/2}segundos en decirla")

