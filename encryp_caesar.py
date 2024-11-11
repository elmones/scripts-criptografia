# HACER DEBBUG PARA ENCONTRAR LA FALLA CON LAS Y 

def caesar_enc(text_clear, shift):
    cypher_text=""
    for i in text_clear:
        if i.isalpha():
            if i.isupper() and ord(i)+shift>90:
                shift=shift-(90-ord(i))
                i=chr(64)
            elif i.islower() and ord(i)+shift>122:
                shift=shift-(122-ord(i)) 
                i=chr(96)   
            cypher_text=cypher_text+chr(ord(i)+shift) 
        else: 
            cypher_text=cypher_text+i  
    return cypher_text

clear_text=input("insertar un texto a encriptar: ")
shift=int(input("insertar un numero de desplazamiento: "))
print(caesar_enc(clear_text, shift))

#LIFE COULD BE AWESOME IF YOU HAVE SOMEONE SPECIAL BY YOUR SIDE
