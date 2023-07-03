
# si el modulo  estuviera  dentro de  una carpeta en la misma ruta 
#import funcionesbuenas.saludar


" asi se importa un modulo que esta afuera "
import sys
sys.path.append ("C:\\Users\\pixel\\onedrive\\escritorio\\curso de python\\funcionesbuenas")
print (sys.path)
import saludar 
print(saludar.saludar("juan"))
