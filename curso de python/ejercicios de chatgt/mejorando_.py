# def numeros_pares(num):
   
#     for i in range(2,num+1):
#         if i %2==0: 
          
#     return True
    
    
    
# def es_par(num):
#     pares=[]
#     for i in range(2,num+1):
#         resultado= numeros_pares(i)
#         if resultado == True:
#             pares.append(i)
#     return pares
        
# resultado= es_par(10)        
# print(resultado)



         
#lo corregi bien            
def numeros_pares(num):
    for i in range(num):
        if num %  2 == 0:  return True
            
   


def es_par(num):
    pares = []
    for i in range(2, num+1):
        resultado = numeros_pares(i)
        if resultado == True:
            pares.append(i)
    return pares


resultado = es_par(10)
print(resultado)
           
  
    
    
            





















