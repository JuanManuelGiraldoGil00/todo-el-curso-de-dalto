
def porcetaje_de_grasa(a,b):
    return round(b / (a*a),2)


altura=float(input("ingrese su altura en metros : "))
peso=float(input("ingrese su peso en kilogramos : "))

porcentaje=print(f"su nivel de grasa corporal es de {porcetaje_de_grasa(altura,peso)}%")



