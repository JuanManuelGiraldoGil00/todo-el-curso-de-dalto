import pandas as pd

# usando la funcion read_csv para leer el archivo CSV 
df= pd.read_csv("archivos\\datos.csv")
df2= pd.read_csv("archivos\\datos.csv")


# obteniendo los datos de la colummna nombre
nombres= df["nombre"]


# ordenando la edad frame por la edad y este esta ordenado en desorden
df_ordenado= df.sort_values("edad")



#ordenandolo de forma desendente 
df_ordenado_decendente= df.sort_values("edad",ascending=False)


#ordenandolo de  forma ascendente 
df_ordenado_acendente= df.sort_values("edad",ascending=True)



#contatenando los 2 dataframes 
df_concatenado=pd.concat([df,df2])

#accediendo  a las primeras 3 filas con head()
primeras_filas= df.head(1)

#accediendo alas ultimas 3 filas con  tail()
ultimas_filas=df.tail(2)

# accediendo a la cantidad de filas y commnas con shape
filas_totales,colummnas_totales= df.shape


# obteniendo data estadistica del dataframe 
#df_info= df.describe()

# accediendo a un elemento en especifico del df con loc 

elemento_especifico_loc= df.loc[2,"edad"]
print(elemento_especifico_loc)


# es lo mismo qur loc si no que a este se accede desde el indice 

elemento_especifico_loc= df.iloc[2,2]
print(elemento_especifico_loc)

#accediendo alos apellidos 

apellidos=df.iloc[:,1]
print(apellidos)

# accediendo a al fila 3 con loc
fila_3= df.loc[2,:]
print(fila_3)


# accediendo a filas con edad mayor a 30
mayor_que_30= df.loc[df["edad"]>30,:]
print(mayor_que_30)

#cambiando el nombre de las colummnas 
# df= pd.read_csv("archivos\\datos.csv",names=["name","lastname","age"])
# diferente=df
# print(diferente)




#para nosotros acceder a un elemento de un indice hasta sirto indice utilizamos esto : asi
# cadena= "0123456789"
# print(cadena[0:10])