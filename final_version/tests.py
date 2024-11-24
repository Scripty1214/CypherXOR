import base64
import random
import os
import string


def GetStr(length):
    str = string.ascii_lowercase
    print(str)
    return ''.join(random.choice(str) for i in range(length))
    

message = "ceci est le 1ér messaefzfzefezfezffzege fezrfoihergf *$ù^m^p&'é(&dé_èuàtest"


taille_message = len(message.encode("utf-8"))
taille2 = len(message)
print("-----------------", taille_message, taille2)


taille_bloc = 16

print(f"Le message fait : {taille_message} octets")
'''
# ajoute un padding si le msg est pas un multiple du bloc
def padding (message, taille_bloc):
    padding_manquant = (taille_bloc - (taille_message % taille_bloc))
    padding_verif = padding_manquant % taille_bloc
    message_padded = message + '\x00' * padding_verif
    # print(f"padding manquant : {padding_manquant} octets, après verification: {padding_verif}")
    # print(f"message après padding : {message_padded}")
    # print(f"taille après padding : {len(message_padded.encode('utf-8'))} octets")
    return message_padded
'''
def padding (message, taille_bloc):
    taille_message = len(message.encode("utf-8"))
    padding_manquant = (taille_bloc - (taille_message % taille_bloc))
    if padding_manquant == 0:
        padding_manquant = taille_bloc
    padding_random = GetStr(padding_manquant-1)
    taille_padding = chr(padding_manquant)
    message_padded = message + padding_random + taille_padding
    return message_padded


def remove_padding(message):
    padding_length = ord(message[-1])  # Lire la longueur du padding
    return message[:-padding_length]


message_padded = padding(message, taille_bloc)

print("aaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", message_padded, len(message_padded), len(message_padded.encode()))
print("---------- Autres tests: ")

"""
my_list = [1, 2, 3, 4, 5]
my_list[2:2]=[99]
print(my_list) 

test1 = "salut c'est moi"
test1_encode = test1.encode("utf-8")
longueur = len(test1_encode)
print(test1, longueur)
"""

print(message_padded)
print("juste len", len(message_padded))
print("len avec encode", len(message_padded.encode("utf-8")))

# divise le message en blocs de 16 octets
def divide_message(message, taille_bloc):
    message = padding(message, taille_bloc)
    taille_message = len(message.encode("utf-8"))
    blocs = []
    for i in range(0, taille_message):
        if i %16 == 0:
            blocs.append(message[i:i + taille_bloc])
    return blocs

print("--------------------------------------------------------------------------------------")
test = divide_message(message, taille_bloc)
print(test)

"""  
def chiffrement_xor(message, taille_bloc):
    blocs = divide_message(message, taille_bloc)
    IV = "Vecteurtinitialt"
    key = "secret"
    result = ""
    for i in range (0, len(blocs)):
        for j in range(0, len(blocs[i])):
            blocs[i] = blocs[i][ord(j)]

        
    for i in range(0, len(blocs)):
        bloc_sep = blocs[i]
        salut = []
        for j in range(0, len(bloc_sep)):
            salut[i] = bloc_sep[ord(j)] ^ bloc_sep[ord(j+1)]
            result.append(salut)
            print(result)
        """

test2 = ord(" ")
print(test2)
'''

test_list = b"salut c'est moi"
list2 = []
for i in range (0, len(test_list)):
    list2.append(test_list[i] ^ (test_list[i] + 2))

print(list2)
'''


test2 = ord('a')
test3 = ord('b')

resultest = test2 ^ test3
print(test2, test3, resultest)


list_test = ["abcdefrtghytgfdg", "efgh"]
# print(ord(list_test[0]))

list_test1 = []
for i in range(0, len(list_test)):
    for j in range(len(list_test[i])):
        #print(ord(list_test[i][j]))
        print(list_test[i][j])
        list_test1.append(ord(list_test[i][j]))

print(list_test1)


def chiffrement_xor(message_dechiffre, taille_bloc, IV, secret_key):
    blocs = divide_message(message_dechiffre, taille_bloc)
    IV_initial = IV
    key = secret_key
    resultat_chiffre = []
    for un_bloc in blocs:
        bloc_chiffre = ""
        for j in range(len(un_bloc)):
            xor_resultat_iv = chr(ord(un_bloc[j]) ^ ord(IV_initial[j]))
            xor_resultat_key = chr(ord(xor_resultat_iv) ^ ord(key[j]))
            bloc_chiffre += xor_resultat_key
        resultat_chiffre.append(bloc_chiffre)
        IV = bloc_chiffre
    resultat_chiffre = "".join(resultat_chiffre)
    resultat_chiffre = resultat_chiffre.encode("utf-8")
    resultat_chiffre_b64 = base64.b64encode(resultat_chiffre)
    return resultat_chiffre_b64





def dechiffrement_xor(message_chiffre, IV, secret_key, taille_bloc):
    IV_Initial = IV
    encrypted_message_b64 = message_chiffre
    encrypted_message_utf8 = base64.b64decode(encrypted_message_b64)
    encrypted_message = encrypted_message_utf8.decode('utf-8')
    blocs_chiffre = divide_message(encrypted_message, taille_bloc)
    resultat_liste = []
    for un_bloc in blocs_chiffre:
        bloc_dechiffre = ""
        for j in range(len(un_bloc)):
            xor_with_key = chr(ord(un_bloc[j]) ^ ord(secret_key[j]))
            xor_with_iv = chr(ord(xor_with_key) ^ ord(IV_Initial[j]))
            bloc_dechiffre += xor_with_iv
        resultat_liste.append(bloc_dechiffre)
        IV_Initial = un_bloc

    resultat_message = "".join(resultat_liste)
    resultat_unpadded = remove_padding(resultat_message)
    return resultat_unpadded



message_utilisateur = input("Entre ton message à chiffrer: \n")
secret_key = GetStr(16)
IV = GetStr(16)
taille_bloc = 16
padded_message = padding(message_utilisateur, taille_bloc)
unpadded_message = remove_padding(padded_message)
message_chiffre = chiffrement_xor(message_utilisateur, taille_bloc, IV, secret_key) 
message_dechiffre = dechiffrement_xor(message_chiffre, IV, secret_key, taille_bloc)

print(f"Voici le message que tu veux chiffrer: {message_utilisateur}\n")
print(f"Voici le message avec padding: {padded_message}\n")
print(f"Voici le message sans padding: {unpadded_message}\n")
print(f"Voici le message chiffré: {message_chiffre}\n")
print(f"Voici ta clée secrète pour dechiffrer ton message: {secret_key}\n")
print(f"Voici ton IV pour dechiffrer ton message: {IV}")
print(f"Voici le message déchiffré: {message_dechiffre}\n")