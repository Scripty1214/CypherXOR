from chiffrement import chiffrement_xor
from dechiffrement import dechiffrement_xor
from others import *
import argparse

TAILLE_BLOC = 16

options = argparse.ArgumentParser(description="Programme de chiffrement et déchiffrement XOR.")

options.add_argument("-c", "--chiffre", dest='chiffre', action="store_true", help="Message ou fichier à chiffrer.")
options.add_argument("-d", "--dechiffre", dest='dechiffre', action="store_true", help="Message ou fichier à déchiffrer.")
options.add_argument("-k", "--key", dest='key', help="Clé secrète pour déchiffrer un message ou un fichier.")
options.add_argument("-i", "--iv", dest='iv', help="Vecteur initial pour déchiffrer un message ou un fichier.")
options.add_argument("-f", "--file", dest='file', help="Nom du fichier à chiffrer ou déchiffrer.")
options.add_argument("-m", "--message", dest='message', help="Message texte à chiffrer ou déchiffrer.")
options.add_argument("-o", "--output", dest='output', help="Nom du fichier de sortie pour le résultat.")
args = options.parse_args()


if args.chiffre and args.dechiffre:
        print("Erreur : Vous ne pouvez pas chiffrer (-c | --chiffrer) et dechiffrer (-d | --dechiffrer) en même temps, utilise (-h | --help) pour plus d'aide.")
        exit()

elif not args.message and not args.file:
        print("Erreur : Tu dois specifier un message (-m | --message) ou un fichier (-f | --file), utilise (-h | --help) pour plus d'aide.")
        exit()

elif not args.chiffre and not args.dechiffre:
        print("Erreur : Tu dois specifier si tu veux chiffrer (-c | --chiffrer) ou dechiffrer (-d | --dechiffrer) un message, utilise (-h | --help) pour plus d'aide.")
        exit()

elif args.iv and args.chiffre:
        print("Erreur : Tu ne peux pas specifier l'IV (-i | --iv) et chiffrer (-c | --chiffrer) en meme temps, utilise (-h | --help) pour plus d'aide.")
        exit()

elif args.key and args.chiffre:
        print("Erreur : Tu ne peux pas specifier la clée secrète (-k | --key) et chiffrer (-c | --chiffrer) en meme temps, utilise (-h | --help) pour plus d'aide.")
        exit()


if args.chiffre:
        secret_key = GetStr(TAILLE_BLOC)
        IV = GetStr(TAILLE_BLOC)
        if args.file:
                fichier = open(args.file, "rb")
                contenu = fichier.read()
                fichier_chiffre = chiffrement_xor(contenu, TAILLE_BLOC, IV, secret_key)
                print(f"Fichier chiffré avec succès.\nVotre clée secrète est : {secret_key}\nVotre IV est : {IV}")
                if args.output:
                        output_file = open(args.output, "wb")
                        fichier_chiffre = output_file.write(fichier_chiffre)
                        print(f"Votre fichier chiffré est {fichier_chiffre}")
                else:
                        print(f"Voici le contenu du message chiffré en base(64): \n{fichier_chiffre.decode("utf-8")}")
        elif args.message:
                fichier_chiffre = chiffrement_xor(args.message, TAILLE_BLOC, IV, secret_key)
                print(f"Message chiffré avec succès.\nVotre clée secrète est : {secret_key}\nVotre IV est : {IV}")
                if args.output:
                        output_file = open(args.output, "wb")
                        output_file.write(fichier_chiffre)
                        print(f"Votre fichier chiffré est {fichier_chiffre}")
                else:
                        print(f"Voici le contenu du fichier chiffré en base(64): \n{fichier_chiffre.decode("utf-8")}")

elif args.dechiffre:
        if not args.key or not args.iv:
                print("Erreur : La clée (-k | --key) et l'IV (-i | --iv) sont requis pour déchiffrer.")
                exit()

        secret_key = args.key
        IV = args.iv

        if args.file:
                fichier = open(args.file, "rb")
                contenu = fichier.read()
                fichier_dechiffre = dechiffrement_xor(contenu, IV, secret_key, TAILLE_BLOC)
                if args.output:
                        output_file = open(args.output, "wb")
                        output_file.write(fichier_dechiffre)
                        print(f"Fichier dechiffré avec succès, votre fichier est: {args.output}")
                else:
                        print(f"Contenu déchiffré avec succès:\n {fichier_dechiffre}")

        elif args.message:
                fichier_dechiffre = dechiffrement_xor(args.message, IV, secret_key, TAILLE_BLOC)
                if args.output:
                        output_file = open(args.output, "w")
                        output_file.write(fichier_dechiffre.decode('utf-8', errors='ignore'))
                        print(f"Message déchiffré avec succès, voici votre fichier: {args.output}")
                else:
                        print(f"Contenu déchiffré avec succès:\n {fichier_dechiffre.decode('utf-8')}")
