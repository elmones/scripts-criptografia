from Crypto.Util.number import getPrime, inverse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Cipher import AES
import xml.etree.ElementTree as ET
import base64
from math import gcd

#Nombre de los archivos 

file1="RansomFile1.xml"
file2="RansomFile2.xml"


#leer y extraer la informacion de los archivos xml.

def xml_parcer(file):
    path="C:/Users/manue/Documents/Master Ciberseguridad/Criptologia y privacidad/Reto 4 - Cifrado hibrido/"+file
    xml = ET.parse(path)
    root = xml.getroot()
    public_key_raw=(root.find("PublicKey").text)
    public_key=RSA.import_key(public_key_raw.strip())
    n=public_key.n
    e=public_key.e
    secret_key_enc=root.find("FileEncryptionKey").text
    init_vect=base64.b64decode(root.find("iv").text)
    message_enc=base64.b64decode(root.find("EncryptedFile").text)
    datos={'public_key':public_key, 'n':n,'e':e, 'init_vec':init_vect, 'secret_key_enc': secret_key_enc, 'message_enc':message_enc}
    
    return datos

def find_p_q(n1,n2):
    p = gcd(n1,n2)
    q1=int(n1)//p
    q2=int(n2)//p
    return p, q1, p, q2

def PrivKeyGen(n, e, p, q):

    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    key = RSA.construct((n, e, d, p, q))

    return key

def decrypt_RSA(secret_crypt, private_key):
    
    cipher_rsa = PKCS1_v1_5.new(private_key)
    secret_b64=base64.b64decode(secret_crypt)
    decryp_secret = cipher_rsa.decrypt(secret_b64, None)
    return decryp_secret


def descifrar_aes_128_cbc(msj, secret_key, init_v):
    
    cifrador=AES.new(secret_key, AES.MODE_CBC, init_v)
    msj_desc=cifrador.decrypt(msj)
    padding_length = msj_desc[-1] 
    mensaje_descifrado = msj_desc[:-padding_length] 
    
    return mensaje_descifrado.decode('utf-8')

#extraer informacion de archivo 1.

file_1=xml_parcer(file1)
file_2=xml_parcer(file2)

#Calculamos los valores de p y q en funcion de ataque batch. 

file_1['p'], file_1['q'], file_2['p'], file_2['q'] = find_p_q(file_1['n'], file_2['n'])

# Se generan las llaves privadas a partir de los datos encontrados.

file_1['private_key']=PrivKeyGen(file_1['n'], file_1['e'], file_1['p'], file_1['q'])
file_2['private_key']=PrivKeyGen(file_2['n'], file_2['e'], file_2['p'], file_2['q'])

file_1['secret_key']=decrypt_RSA(file_1['secret_key_enc'], file_1['private_key'])
file_2['secret_key']=decrypt_RSA(file_2['secret_key_enc'], file_2['private_key'])

print(descifrar_aes_128_cbc(file_1['message_enc'],file_1['secret_key'] , file_1['init_vec']))
print(descifrar_aes_128_cbc(file_2['message_enc'],file_2['secret_key'] , file_2['init_vec']))
