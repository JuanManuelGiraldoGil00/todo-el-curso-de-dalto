#cambiar el tipo de dato de una colummna 
import pandas as pd 
df= pd.read_csv("archivos_problemas\\datos.csv")

#convertir a  string los datos de un colummna 
df["edad"]= df["edad"].astype(str)


# mostrar el tipo de dato del primer elemento de la colummna edad 
#print(type(df["edad"][0]))

#remplazando los datos "dalto" por "maestro"
df["apellido"].replace("dalto","maestro",inplace=True)


# mostrando la colummna apellido
print(df["apellido"])


# eliminando las filas con datos vacios si quisieramos las filas con datos faltantes seria dropna(axis=1)
df= df.dropna()


#eliminando las filas repetidas 
df= df.drop_duplicates()
print(df)


# creando un csv con el dataframe resultante (limpio) osea vamos a crear un nuevo csv

df.to_csv("archivos_problemas\\datos_limpios.csv")

