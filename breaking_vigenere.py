from math import gcd
from functools import reduce
from collections import Counter


alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def text_sanitizer(text):
    clean_text=[char.upper() for char in text if char.isalpha()]
    return clean_text

def encontrar_secuencias_repetidas(cadena):
    secuencias = {}
    longitud = len(cadena)

    # Encontrar secuencias de longitud variable a partir de 3 caracteres
    for length in range(3, longitud // 2 + 1):
        for i in range(longitud - length + 1):
            secuencia = cadena[i:i + length]
            if secuencia in secuencias:
                secuencias[secuencia].append(i)
            else:
                secuencias[secuencia] = [i]
    
    # Filtrar secuencias que no se repiten
    secuencias_repetidas = {seq: pos for seq, pos in secuencias.items() if len(pos) > 1}

    # Encontrar el máximo número de apariciones
    max_apariciones = max(len(pos) for pos in secuencias_repetidas.values())

    # Filtrar secuencias con el mayor número de apariciones
    secuencias_max_apariciones = {seq: pos for seq, pos in secuencias_repetidas.items() if len(pos) == max_apariciones}

    # Calcular las distancias entre apariciones y el número de apariciones
    resultado = []
    todas_distancias = []
    for secuencia, posiciones in secuencias_max_apariciones.items():
        distancias = [posiciones[i+1] - posiciones[i] for i in range(len(posiciones) - 1)]
        todas_distancias.extend(distancias)
        apariciones = len(posiciones)
        resultado.append((secuencia, distancias, apariciones))

    # Calcular el MCD de todas las distancias
    if todas_distancias:
        mcd_total = reduce(gcd, todas_distancias)
    else:
        mcd_total = None

    #return resultado, mcd_total
    return mcd_total

def agrupar_en_listas(cadena, k):
    listas = [[] for i in range(k)]
    contador=0
    # Recorrer cada carácter en la cadena
    for char in cadena:
        if char != ' ' and char.isalpha():  # Ignorar espacios vacíos y signos de puntuacion
            listas[contador % k].append(char)  # Añadir el carácter a la lista secundaria correspondiente
            contador+=1
    return listas

def find_key(lists):
    key=""
    clave_procesada={}
    for list in lists: 
        clave=dict(Counter(list))
        for i in alphabet: 
            if i not in clave.keys():
                clave[i]=0
        for i in clave.keys():
            clave_procesada[i]=clave[i]+clave[chr(((ord(i)-65)%26 + 4)%26 +65)]+clave[chr(((ord(i)-65)%26 + 14)%26 +65)]+clave[chr(((ord(i)-65)%26 + 19)%26 +65)]
        letter=Counter(clave_procesada)
        clave_ordenada=sorted(letter, key=lambda x:letter[x], reverse=True)
        key+=clave_ordenada[0]
    return key

def lang_factor(list):
    lang_factor=0
    frequency=Counter(list)
    total_letter=sum(frequency.values())
    for i in frequency.keys(): 
        lang_factor+=(frequency[i]/total_letter)**2   

    return lang_factor

def vigenere_dec(text_cipher, key):
    text_clear = ""
    key_length = len(key)
    key_as_int = [ord(i.upper()) - 65 for i in key]
    key_index = 0
    
    for char in text_cipher:
        if char.isalpha():
            shift = key_as_int[key_index % key_length]
            if char.isupper():
                new_char = chr((ord(char) - 65 - shift + 26) % 26 + 65)
            elif char.islower():
                new_char = chr((ord(char) - 97 - shift + 26) % 26 + 97)
            text_clear += new_char
            key_index += 1
        else:
            text_clear += char

    return text_clear

raw_cypher_text=input("ingresar texto cifrado: ")
#raw_cypher_text="""KVQMR KJSZG RJNOE IAKKF GCGWU WRHRU FIXDA GKOBP EGRQT TBZLF XAFHV ODWVL YHTEY WKHQR SSJHQ NRVKC FHRLY CZGVF JWPEG ZVSZT EWEQT MRFKC RTUWT OYPSW RFUNT VRBSE ELYSS AHDUW ECUSI UQDGZ VGBEN JRGTE USUPQ EAAEG FRHUK SPBLU YOZCR AKGFU PCWOE TVFKV QTBOV FMNQX FFFWB VRMEW NKECF SVYYH QDOQF IDTEG FDEOA LYSFH VJURM YVLNO ESVYY HQDOQ RGALQ AVFFA XWERA WASER PEYAM SDEQL FQUCR JFVQR RSUWF TUJFI SHNFU HTEAJ VQUTR VZHMT NHRFM DRGWH TEGJF CBSOJ ZBSIA YKVQG EWRHQ SGJVX AIPAE UFOND C"""

cypher_text="".join(text_sanitizer(raw_cypher_text))
frecuencia=encontrar_secuencias_repetidas(cypher_text)

print("La longitud tentativa de la llave es: ", frecuencia)

grupos = agrupar_en_listas(raw_cypher_text, frecuencia)

key_text=find_key(grupos)

print("La llave tentativa es: ", key_text)

print("Texto descifrado:", vigenere_dec(raw_cypher_text, key_text))