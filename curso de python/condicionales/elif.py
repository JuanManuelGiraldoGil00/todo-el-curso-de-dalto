ingreso_mensual= 200
gasto_mensual= 0

# else y  if anidados  (elif)

if ingreso_mensual > 10000:
    if  ingreso_mensual - gasto_mensual < 0:
     print("estas en deficit ")
    
    elif ingreso_mensual- gasto_mensual > 3000 :
         print("estas bien economicamente en cualquier parte del mundo ")
    
    
    else:
     print(" estas gastando mucho ahorra mas ")
     
elif ingreso_mensual > 1000:
    print("estas bien economicamente en latinoa america  ") 
    
    
elif ingreso_mensual > 500:
    print("estas bien economicamente en venesuela ")
     
     
else:
    print("estas mal economicamente ")       
    