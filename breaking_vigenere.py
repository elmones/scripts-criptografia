from collections import Counter

def text_sanitizer(text):
    clean_text=[char.upper() for char in text if char.isalpha() or char==" "]
    return clean_text

def agrupar_en_listas(cadena, k):
    listas = [[] for i in range(k)]
    contador=0
    # Recorrer cada carácter en la cadena
    for char in cadena:
        if char != ' ' and char.isalpha():  # Ignorar espacios vacíos y signos de puntuacion
            listas[contador % k].append(char)  # Añadir el carácter a la lista secundaria correspondiente
            contador+=1
    return listas

def lang_factor(list):
    lang_factor=0
    frequency=Counter(list)
    #print("para la lista: ", list)
    #print("Se tiene la siguiente distribucion: ", frequency)
    total_letter=sum(frequency.values())
    #print("se tienen la siguiente cantidad de letras: ", total_letter)
    for i in frequency.keys(): 
        lang_factor+=(frequency[i]/total_letter)**2   

    return lang_factor


#raw_cypher_text=input("ingresar texto cifrado: ")
raw_cypher_text="""KN T UMTNL MQWG PELVLXF BXVWXGN KQLEKNZ JIENS TPD LGRXPE ECKXU TAGRX NIOGD T AONPG PQMTP NTOEW GMBNY LJE PCS DPOPP FHT HXT LHXE HH BHQKL CNW JEK KNLCTBCBEG CNTIHUIMA AUQUM VHX YOKND LJE PQRDGD TV TAG LHEAE NIUTAKA WAGRX UHX UPXPT AGR WCYL UUKTONPDXF BR UTHTIXU AGF KGQWEGDZG FKQM XXEKA CHTNXT OY VHX ILHDE WGSIKTX VHX EAEO AGF PKGDBETTDIEKTR QF AGR EKFX GMBNY HHTXP DKGAFGD HH GKCNW CDOGNMWRXU AGF DBUTTPT ECNWU"""
#raw_cypher_text="""KVQMR KJSZG RJNOE IAKKF GCGWU WRHRU FIXDA GKOBP EGRQT TBZLF XAFHV ODWVL YHTEY WKHQR SSJHQ NRVKC FHRLY CZGVF JWPEG ZVSZT EWEQT MRFKC RTUWT OYPSW RFUNT VRBSE ELYSS AHDUW ECUSI UQDGZ VGBEN JRGTE USUPQ EAAEG FRHUK SPBLU YOZCR AKGFU PCWOE TVFKV QTBOV FMNQX FFFWB VRMEW NKECF SVYYH QDOQF IDTEG FDEOA LYSFH VJURM YVLNO ESVYY HQDOQ RGALQ AVFFA XWERA WASER PEYAM SDEQL FQUCR JFVQR RSUWF TUJFI SHNFU HTEAJ VQUTR VZHMT NHRFM DRGWH TEGJF CBSOJ ZBSIA YKVQG EWRHQ SGJVX AIPAE UFOND C"""
frecuencia=int(input("Ingresar una frecuencia a probar: "))


grupos = agrupar_en_listas(raw_cypher_text, frecuencia)

counter=0
for i, lista in enumerate(grupos):
    print("Para el grupo ", i, "el factor es: ", lang_factor(lista))
    counter+=1

if counter==frecuencia:
    print("EXITO!")
else: print("NO EXITOSO!") 

# print("Listas resultantes:")
# for i, lista in enumerate(grupos):
#     print(f"Lista {i + 1}: {lista}")