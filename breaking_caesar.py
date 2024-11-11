from collections import Counter
from prettytable import PrettyTable

freq_eng = { 'A': 0.0817, 'B': 0.0149, 'C': 0.0278, 'D': 0.0425, 'E': 0.1270, 'F': 0.0223, 'G': 0.0202, 'H': 0.0609, 'I': 0.0697, 'J': 0.0015, 'K': 0.0077, 'L': 0.0403, 'M': 0.0241, 'N': 0.0675, 'O': 0.0751, 'P': 0.0193, 'Q': 0.0010, 'R': 0.0599, 'S': 0.0633, 'T': 0.0906, 'U': 0.0276, 'V': 0.0098, 'W': 0.0236, 'X': 0.0015, 'Y': 0.0197, 'Z': 0.0007}
answers=["Y", "Yes", "y", "yes"]
def text_analysis(text):
    lang_factor=0
    answer=[]
    letters=[]
    clean_text=[char.upper() for char in text if char.isalpha()]
    frequency=Counter(clean_text)
    total_letter=sum(frequency.values())
    for i in frequency.keys(): 
        lang_factor+=(frequency[i]/total_letter)**2   
    letters=sorted(frequency, key=lambda x:frequency[x], reverse=True)
    answer=[lang_factor, letters, frequency, total_letter]
    return answer 

def caesar_breaker(text, shift):
    decypher_text = ""
    for i in text:
        if i.isalpha():
            shift_mod = shift % 26  # Asegurar que el desplazamiento este dentro del rango del espacio de claves
            if i.isupper():
                new_char = chr((ord(i) - 65 - shift_mod) % 26 + 65)
            elif i.islower():
                new_char = chr((ord(i) - 97 - shift_mod) % 26 + 97)
            decypher_text += new_char
        else:
            decypher_text += i
    return decypher_text


raw_cypher_text=input("ingresar texto cifrado: ")

#raw_cypher_text="""NOYZU XEOYV ATIZA GZKJC OZNIU JKYZN KENGB KJKIO JKJZN KUAZI USKYU LHGZZ RKYGT JRKJZ UZNKJ KGZNY ULQOT MYGTJ WAKKT YONGB KZNKX KLUXK HKKTG HRKZU IGRRA VUTYZ UXOKY ULVUR OZOIG ROTZX OMAKG TJZGR KYULR OLKGT JJKGZ NZUOR RAYZX GZKZN KQKEZ AXTOT MVUOT ZYOTZ NKKBU RAZOU TGXEJ KBKRU VSKTZ ULIUJ KYZNK NOYZU XEULI UJKYO YYUOT UXJOT GZKRE XOINZ NGZON GBKHK KTLUX IKJZU RKGBK UAZSG TELGY IOTGZ OTMYZ UXOKY CNOIN OTZAX TSKGT YZNGZ SEGII UATZO YTUZJ KLOTO ZOBKO LEUAC UARJR OQKZU LOTJU AZSUX KGHUA ZEUAX LGBUX OZKZG RKUXE UAXLG BUXOZ KIUJK HXKGQ KXZNK TOCUA RJXKL KXEUA ZUZNK ROYZU LLAXZ NKXXK GJOTM CNOIN YNUAR JNKRV ZNUYK XKGJK XYCNU CUARJ ROQKZ UYZAJ EZNKY AHPKI ZOTSU XKJKZ GOR"""

print("Analizando el texto ingresado... ")

text_analytics=text_analysis(raw_cypher_text)

letter=text_analytics[1]
for char_1 in freq_eng.keys():
    if char_1 not in letter:
        letter.append(char_1)
      
print("Se tiene la siguiente frecuencia de letras:")

freq_table=PrettyTable()

freq_table.fieldname=["Letra","Frecuencia"]
for i in text_analytics[1]:
    freq_table.add_row([i, text_analytics[2][i]/text_analytics[3]])
print(freq_table)

if text_analytics[0]>0.060 and text_analytics[0]<0.070: 
    print ("Lo que nos da un factor de lenguaje de: ", text_analytics[0], " correspondiente del idioma ingles")
    print ("La letra con la frecuencia mas alta es: ", text_analytics[1][0])
    for char in letter:#text_analytics[1]:
        shift=(ord(char)-69)%26
        print("Se inicia el intento de romper el cifrado suponiendo que la letra E corresponde a:" , char, "con un desplazamiento de:", shift)
        print(caesar_breaker(raw_cypher_text, shift))
        user_answer=input("Es este decifrado preciso para usted? (Y/N) ")
        if user_answer in answers:
            print("GRACIAS!")
            break
        else: 
            print("Continuaremos con la proxima iteracion")
            continue
        
else: print ("Un factor de: ", text_analytics[0], " no permite concluir un lenguaje de origen.")






