# creando un conjunto con set ()
conjunto = set (["dato1"])


# metiendo un conjunto dentro de otro conjunto
conjunto1= frozenset(["dato 1", " dato 2"])

conjunto2= {conjunto1,"dato3"}
#print(conjunto2)


#teroria de conjuntos 

conjunto3={1,3,5,7}
conjunto4={1,3,7}
#virificando si es un subconjunto
resultado=conjunto4.issubset(conjunto3)
resultado= conjunto4 <= conjunto3


# verificando si es un superconjunto
resultado= conjunto4.issuperset(conjunto3)
resultado= conjunto4 > conjunto3

#verificasr si no tiene un elmento en comun
resultado=  conjunto4.isdisjoint(conjunto3)



print(resultado) 












