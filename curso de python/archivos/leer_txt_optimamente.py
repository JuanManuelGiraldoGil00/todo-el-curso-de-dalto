with open("archivos\\texto_de_dalto.txt",encoding="UTF=8")as archivo:
    
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)
    
    
#no es nesesario cerrarlo al usar with open
   
        