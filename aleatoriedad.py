from os import strerror

source_file="claves.xlsx.enc"
destination_file="claves.xlsx"
clave=[0x4a, 0x1a, 0xcc, 0x43, 0x34, 0x60, 0x70, 0x9e]

try:
  with open(source_file, "rb") as file:
    cypher_file=file.read()
    file.close()

except IOError as e:
   print("se ha producido un erro de E/S: ", strerror(e.errno))
   exit()

claves=[]
for i in range(len(cypher_file)):
   claves.append(clave[i%len(clave)])
   
output=bytearray(len(cypher_file))
   
for b in range(len(cypher_file)):
   output[b]=cypher_file[b]^claves[b]


try: 
   output_file=open(destination_file, "wb")
   output_file.write(output)
   output_file.close()
except IOError as e:
   print("Hubo un problema creando el archivo: ", strerror(e.errno))
   exit()