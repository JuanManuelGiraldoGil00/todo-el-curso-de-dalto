# froma no optima de sumar valores
# def suma(lista):
#     numeros_sumados= 0
#     for numero in lista:
#         numeros_sumados= numeros_sumados + numero 
#     return numeros_sumados
# resultado= suma([1,2,1,3,4,3,19,23])
# print(resultado)

# utilizando  el parametro args *

def suma(*numeros):
    return sum(numeros)
resultado= suma(5,3,9,10,20,3)
print(resultado)
# utilizando args par meter nombre y sumar numeros
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es : { sum(numeros)}"


resultado= suma("juan",5,3,9,10,20,3)
print(resultado)

