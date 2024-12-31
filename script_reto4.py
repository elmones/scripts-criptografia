from Crypto.Util.number import getPrime, inverse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Cipher import AES
import xml.etree.ElementTree as ET
import base64
from math import gcd

n1=0xa2ab2060a88b37bb96b8d8776ccbaf8eead78ec03961339a4dd53cd2b2cbd39e0b3027a3f6739fdaeff499ba4756487615f95579a9af7fd58d66174b97e6fee2f8fff2a89e8cff03cb6261241eed69010af110aefbff0c93e24c6e2911f235d7ba8e9ec513a8d9a1c13e857eac146749c23e0c94172af60f7a8ae0d2a416fd4fb419c15366fdf53131d31dbd52f05b868af7a84e480761feb1bc53a6ca3d605998ea80f98a30d8ee9487178972fb84bfed9f85d73f5bc518a85ebb02cb6f2b00a3107e4be277d709627d319c49eb3e1b67099eb90ced5ef759d222cc7958d70023f4b393b278d9f93ea3abc96b7e7a164f75a4bc8343e0b1dd0d53577825f803
n2=0xa959e70de200970af9da1f97454b64149d30fa47b9fc5ef716a0b67ea75d2234624c6ef56bc14a386cf814f4cf1dd7373aa6a54c8a0e0263d341be3f895cd8dd233ca59be3b9e4e3d793abf796ea09df8c6d7555a88985eed8386d57243a37073c7115cf74ab2f01b76f0ad07bf83ebd096a5c9e23466397943f7a053403fbf3f8f3162fe9517fe10f9164bdeeabbd75fc2b799eb51f7c88acc15048093ca4df9e7ef1d036914f69a158a0efa33fca21c803b04d2861f515259ca9b22fa31e4f13a5574437b82ac0e5603d9806aabc3775d43250479553931c4a7304d92d3b657378c7020cdc086f8e92800f6a7e5dde7d7bbf6dd865ce53ec5789d9c754088f
p=0xca4c0d9ca51b07eb22bca9d13b7bada9c3ac8c6fcbd399ffe17388ff32e7a99927f32fd9ecf4dd0a587c5e6451a29bec804dbcfbf37af9fb721648f47ee5f01f1041bd5be7c8b1690704865440cd741f56286610583327644e10aa68e42da2c5fea8ad4c50f958de15b2d5d59048713ad7d06925380d8b1537a6b7deca2d64bd
q1=0xcdd9f1b799968cf0581692970b6c5a482188b6c47501c670607c468fb0d6516f9c675dce203ff4a679f7ad3724595a7dfa1a727f8cc636c9fa9a6ff28b592cd264608ce0996e6cfcca5617c8e0b38ba29eb21e821ceda6f458fb43d4c65f4e71a4f8d0e24a2725d2dfccd1c2bba1cbf2aed04d89872539fba360e6e988f57bbf
q2=0xd64edf5bcc339f0ca59cacded895bd1a0c1aaa314d169cea0dda78e6beb044b10f5ea69e3c5eab562ce0e7ac61f2bff1d28d0bb48be08255e59e0cd11ffdadf7d4178f15758f8c97aceb38be8cf078b3292ae2083749ff0101b2930fd86bd3d058cad52ca521cee4294139150f92fce08f715b3d133529d3f9b253a187b0a53b

#Leer el archivo xml
file1="RansomFile1.xml"
file2="RansomFile2.xml"


#leer y extraer la informacion de los archivos xml. +
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
