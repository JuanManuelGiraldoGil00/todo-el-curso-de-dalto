#2 listas, una con nombres otra con apellidos 
nombres=["lucas","matias","camila","pedro","roberto"]
apellidos=["dalto","zing","dalto","robetix","tarado"]

#registrar esta informacion en un txt de forma optima

with open("nombres_y_apellidos.txt","w") as arch:
    arch.writelines("los datos son :\n \n")
    [arch.writelines(f"Nombre : {n}\n apellido : {a}\n----------------------\n ")for n,a in zip(nombres,apellidos)]
    