import base64
from others import divide_message, padding




def chiffrement_xor(message, taille_bloc, IV, secret_key):
    message_padded = padding(message, taille_bloc)
    blocs = divide_message(message_padded, taille_bloc)


    IV_initial = IV.encode('utf-8')

    key = secret_key.encode('utf-8')
    resultat_chiffre = []
    for un_bloc in blocs:
        bloc_chiffre = b""
        for j in range(len(un_bloc)):
            xor_resultat_iv = un_bloc[j] ^ IV_initial[j]
            xor_resultat_key = xor_resultat_iv ^ key[j]
            bloc_chiffre += bytes([xor_resultat_key])
        resultat_chiffre.append(bloc_chiffre)
        IV_initial = bloc_chiffre
    resultat_chiffre = b"".join(resultat_chiffre)
    resultat_chiffre_b64 = base64.b64encode(resultat_chiffre)
    return resultat_chiffre_b64