with open("archivos\\texto_de_dalto.txt","a",encoding="UTF=8") as archivo :
   
   #usando un bucle para agregar varias lineas
   archivo.write("\n")
   for i in range(5):
    #agregando contenido al  el archivo la \n se utiliza para organizar en lineas y no en una sola linea
     
     archivo.write(f"linea {i +1 } agregada\n")
    