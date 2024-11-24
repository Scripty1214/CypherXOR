import random
import string

def GetStr(length):
    str = string.ascii_lowercase
    return ''.join(random.choice(str) for i in range(length))


def padding (message, taille_bloc):
    if isinstance(message, str):
        message_bytes = message.encode('utf-8')
    else:
        message_bytes = message
    taille_message = len(message_bytes)
    padding_manquant = (taille_bloc - (taille_message % taille_bloc))
    padding_random = GetStr(padding_manquant - 1).encode("utf-8")
    taille_padding = bytes([padding_manquant])
    message_padded_utf8 = message_bytes + padding_random + taille_padding
    return message_padded_utf8


def remove_padding(message):
    if isinstance(message, str):
        message = message.encode('utf-8')
    padding_longueur = message[-1]
    message_unpadded = message[:-padding_longueur]
    return message_unpadded


def divide_message(message, taille_bloc):
    if isinstance(message, str):
        message = message.encode('utf-8')
    taille_message = len(message)
    blocs = []
    for i in range(0, taille_message):
        if i %16 == 0:
            blocs.append(message[i:i + taille_bloc])
    return blocs