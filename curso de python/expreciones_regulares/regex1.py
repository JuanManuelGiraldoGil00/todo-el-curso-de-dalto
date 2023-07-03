import re 
text= "the  quick brown fox jumps the lazy dog"

x= re.search("^the.*dog$", text)

if x:
    print("SI")
    
else:
    print("NO")
    
        