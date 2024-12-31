SCRIPT QUE TOMA LOS ARCHIVOS: 

RansomFile1.xml
RansomFile1.xml

Y consigue descifrar el mensaje contenido. 

############################################
#        Analisis del ejercicio            #
############################################

Inicialmente se inspecciono el archivo xml RansomFile<X>.xml

Se nota que el mismo contiene la clave publica con la que fue cifrado. 
Contiene el vector de inicializacion codificado en base64. 
Contiene la clave secreta que se uso para encriptar el mensaje, la misma esta cifrada y codificado base64.
Contiene el mensaje cifrado con aes-128-cbc en codificado base64.

Se parte del hecho de que para poder descifrar la llave secreta encriptada con la clave publica, tenemos que encontrar la clave privada. 
como parte del problema describe que se usaron generadores de numeros random pobres partimos de la hipotesis de: 

O los numeros primos p y q generados eran cercanos, con lo cual aplicabamos un ataque de factorizacion. 
O se repitio uno de los numeros p o q para generar ambas claves privadas con lo cual aplica un ataque del tipo batchGCD. 

Se escribio un script que probara la primera hipotesis pero el mismo no lograba encontrar los numeros con lo cual se descarto esta hipotesis.
Se escribio un script siguiendo la hipotesis de que se repite la p o la q para generar ambas claves privadas. 

###########################################
#    Descripcion del script               #
###########################################

El script esta compuesto de 5 funciones: 

xml_parcer: toma cada archivo RansomFile<X>.xml y parcea los valores para almacenarlos en un diccionario. 
find_p_q: toma dos parametros n de cada clave publica y con esto encuentra p y q suponiendo que uno de ellos se repite. 
PrivKeyGen: genera las llave privada.
def decrypt_RSA: Descifra la llave privada 
def descifrar_aes_128_cbc: toma la llave privada, el mensaje y el vector de inicializacion y entrega el mensaje descifrado. 

La idea general es tomar el diccionario con los diferentes valores, la llave publica, el IV, la llave secreta cifrada y el mensaje cifrado e ir encontrando cada dato que falta, tal que: 

con cada clave publica obtenemos la n y la e. 
con los valores de n de cada clave publica obtenemos p y q con el metodo BatchGCD.
con estos generamos los valores de phi y d. 
con esto tenemos todo para generar la clave privada con RSA.construct().
Una vez que tenemos la clave privada podemos descrifrar la clave secreta decodificandola primero de base64. 
con al clave secreta y el vector de inicializacion ya se puede descifrar el mensaje. 

mensaje 1: VIVA LA CRIPTOGRAFIA
mensaje 2: MUERTE AL RANSOMWARE 

