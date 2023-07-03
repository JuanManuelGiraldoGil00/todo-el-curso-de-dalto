import re 
email= "example@example.com"

pattern= "[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result= re.match(pattern,email)

if result:
    print("direcion de codigo valida ")
    
    
else:
    print("direccion de corre valida")
        