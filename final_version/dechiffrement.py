import base64
from others import divide_message, remove_padding



def dechiffrement_xor(message_chiffre, IV, secret_key, taille_bloc):
    IV_Initial = IV.encode('utf-8')
    key = secret_key.encode('utf-8')

    encrypted_message_bytes = base64.b64decode(message_chiffre)

    blocs_chiffre = divide_message(encrypted_message_bytes, taille_bloc)

    resultat_liste = []
    for un_bloc in blocs_chiffre:
        bloc_dechiffre = b""
        for j in range(len(un_bloc)):
            xor_with_key = un_bloc[j] ^ key[j]
            xor_with_iv = xor_with_key ^ IV_Initial[j]
            bloc_dechiffre += bytes([xor_with_iv])
        resultat_liste.append(bloc_dechiffre)
        IV_Initial = un_bloc
    resultat_message = b"".join(resultat_liste)
    resultat_unpadded = remove_padding(resultat_message)
    return resultat_unpadded