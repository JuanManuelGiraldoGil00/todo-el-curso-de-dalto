archivo=open ("archivos\\texto_de_dalto.txt",encoding="UTF-8")
#leer archivo completo
# archivo=open ("archivos\\texto_de_dalto.txt",encoding="UTF-8")
# print(archivo.read())

#leer linea por linea 
#lineas=archivo.readlines()

#leer una sola linea 
linea = archivo.readline()
print(linea)


# cerrar el archivo
cerrar=archivo.close() 

