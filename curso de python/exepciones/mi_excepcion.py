class MiExcepcion(Exception):
    def __init__(self,err):
        print(f" impresionante, cometiste el siguiente erro :{err}")
        
        
#lanzando mi propia excepcion y con raise siempre se va a ejecutar lo que le pongamos
#raise MiExcepcion("jajajajajaj, persona poco culta")
     
     
#manejando la excepcion 
try:
    raise MiExcepcion("jjajajajj,persona poco culta ")

except:
    print("coma vas  a cometer ese error?")
            
        
    