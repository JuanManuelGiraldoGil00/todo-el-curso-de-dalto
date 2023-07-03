import modulo_saludar as m_saludar
# # el as nos permite asignar un nuevo nombre para asi no tener problemas con el modulo



saludo= m_saludar.saludar("juan")
print(saludo)



# si nosotros queremos solo importar una funcion podemos utilizar from asi 


"""este que esta aca nos manda lo que contiene sin definirlo sirve solo si vamos a hacer lo mismo si no las otras 2 opciones
 y si queremos importar mas funciones solo hay que ponerle una coma  asi como a return"""
from modulo_saludar import saludar


lo= saludar("juan")
print(lo)



"si nosotros quisieramos ver todo lo que hay dentro de un modilo usamos dir "

print(dir(m_saludar))







