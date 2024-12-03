
from os import strerror
from Crypto.Cipher import AES
import binascii

def encrypt_aes_ecb(plaintext_bytes, key_bytes):
    cipher = AES.new(bytes(key_bytes), AES.MODE_ECB)
    encrypted = cipher.encrypt(bytes(plaintext_bytes))
    return list(encrypted)

source_file="M1-1732957655763.hex"
path="C:/Users/manue/Documents/Master Ciberseguridad/Criptologia y privacidad/"+source_file
destination_file="C:/Users/manue/Documents/Master Ciberseguridad/Criptologia y privacidad/M1_dec.txt"

try:
  with open(path, "rb") as file:
    cypher_file=file.read()
    file.close()

except IOError as e:
   print("se ha producido un erro de E/S: ", strerror(e.errno))
   exit()

#print("la longitud del archivo en bloques es: ", len(cypher_file)/16)

bloques_cifrados=[] # Contiene los bloques de 16 bytes cifrados. 

for i in range(0, len(cypher_file), 16):
    bloques_cifrados.append(list(cypher_file[i:i + 16]))

mensaje_cifrado=bloques_cifrados[2:]

# for i, lista in enumerate(bloques_cifrados):
#    print ("el bloque ", i, "contiene:")
#    for n in lista:
#       print(hex(n), sep=" ", end=" ")
#    print()

session_key=[0x9C, 0x2F, 0xE1, 0x0E, 0x63, 0xF3, 0x2B, 0x48, 0xC5, 0x06, 0x79, 0xA7, 0xAD, 0x59, 0x94, 0x12]
secuencia_cifrante_0=[0x62, 0x0F, 0x38, 0x55, 0x32, 0x1E, 0x64, 0x37, 0xAD, 0xEE, 0x51, 0x99, 0xFE, 0x57, 0xDF, 0x11]

secuencias_cifrantes=[[0x62, 0x0F, 0x38, 0x55, 0x32, 0x1E, 0x64, 0x37, 0xAD, 0xEE, 0x51, 0x99, 0xFE, 0x57, 0xDF, 0x11]]

for i in range(len(mensaje_cifrado)-1):
   plaintext_bytes = secuencias_cifrantes[i]
   encrypted_bytes = encrypt_aes_ecb(plaintext_bytes, session_key)
   secuencias_cifrantes.append(encrypted_bytes)
  
# for i, item in enumerate(secuencias_cifrantes):
#    print(f"Elemento {i}: {[hex(byte) for byte in item]}")

clear_text=[]

if len(mensaje_cifrado)==len(secuencias_cifrantes):
   for i in range(len(mensaje_cifrado)):
      for n in range(16):
        clear_text.append(mensaje_cifrado[i][n]^secuencias_cifrantes[i][n])
        
# for i in clear_text:
#    print(hex(i), sep="", end=" ")

output=bytearray(len(clear_text))
   
for b in range(len(clear_text)):
   output[b]=clear_text[b]

try: 
   output_file=open(destination_file, "wb")
   output_file.write(output)
   output_file.close()
except IOError as e:
   print("Hubo un problema creando el archivo: ", strerror(e.errno))
   exit()