# creando las litas 
frutas= ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena= " hola soy juan"
numeros= [12,34,27,88]
# evitando  que se coma una manzana con la sentencia continue 
for fruta in frutas:
    if fruta == "pera":
        continue 
    print(f"me voy a comer una  {fruta}")
    
    
 # evitar que siga ejecutandose  si se le pone u else no seva ajecutar cuando alla un break 
for fruta in frutas:
    if fruta == "pera":
        break
    print(f" mevoy a comer una {fruta}")
    
    print("bucle terminado")
    
# recorreer una cadena de texto 
for letra in cadena:   
    print(letra) 
    
# for en una sola lnea de codigo (duplicamos los numeros)

numero_duplicados= [x*2 for x in numeros]   
print(numero_duplicados) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    