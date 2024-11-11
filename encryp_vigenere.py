def data_collection(user_select):


def caesar_enc(text_clear, shift):
    cypher_text = ""
    for i in text_clear:
        if i.isalpha():
            shift_mod = shift % 26  # Asegurar que el desplazamiento este dentro del rango del espacio de claves
            if i.isupper():
                new_char = chr((ord(i) - 65 + shift_mod) % 26 + 65)
            elif i.islower():
                new_char = chr((ord(i) - 97 + shift_mod) % 26 + 97)
            cypher_text += new_char
        else:
            cypher_text += i
    return cypher_text

def vigenere_enc(text_clear, key):
    cypher_text = ""
    key = key.upper()  # Convertimos la clave a Mayusculas. 
    key_length = len(key)
    key_shifts = [(ord(k) - 65) for k in key]  # covierto cada letra en un numero de desplazamiento
    non_letter=0
    for index, char in enumerate(text_clear):
        if char.isalpha():
            shift=key_shifts[(index-non_letter)%key_length]
            cypher_text+=caesar_enc(char,shift)
        else:
            shift=1
            non_letter+=1
            cypher_text+=caesar_enc(char,shift)

    return cypher_text

user_selection=True
while (user_selection):
    print("""Bienvenido al script de servicios de cifrado clasico, con este podras: 
      1) Cifrar un texto claro usando cifrado por desplazamiento
      2) Cifrar un texto claro usando cifrado Vigenère
      3) Romper cifrado por deplazamiento
      4) Romper cifrado Vigenère.
      5) salir
      """)
    try:
        user_choise=int(input("Selecciona mediante el numero una opcion: "))
    except: print ("por payaso te jodiste!")

    if user_choise==1:
    elif user_choise==2:
    elif user_choise==3:
    elif user_choise==4:
    elif user_choise==5:
    
# Solicitar entrada de usuario
clear_text = input("Inserta un texto a encriptar: ")
key = input("Inserta la clave para el cifrado Vigenère: ")

# Mostrar el texto cifrado
print("Texto encriptado:", vigenere_enc(clear_text, key))



