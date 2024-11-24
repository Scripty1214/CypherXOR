# CypherXOR project (Careful now, I know exactly where you are)

## Installation
**Clone the repo** : `git clone https://github.com/Scripty1214/CypherXOR.git`


## Example
**Encrypt a message** : `python3 main.py -c -m 'Hello world !'`
**Decrypt a message** : `python3 main.py -d -m 'RXNzY2kmcm11Y3M9Jnh8Bg==' -i "fzghavmsbdrztvpo" -k "klxggphqekegsexj"`

## Usage

usage: main.py [-h] [-c] [-d] [-k KEY] [-i IV] [-f FILE] [-m MESSAGE] [-o OUTPUT]

Programme de chiffrement et déchiffrement XOR.

options:
  -h, --help            show this help message and exit
  -c, --chiffre         Message ou fichier à chiffrer.
  -d, --dechiffre       Message ou fichier à déchiffrer.
  -k KEY, --key KEY     Clé secrète pour déchiffrer un message ou un fichier.
  -i IV, --iv IV        Vecteur initial pour déchiffrer un message ou un fichier.
  -f FILE, --file FILE  Nom du fichier à chiffrer ou déchiffrer.
  -m MESSAGE, --message MESSAGE
                        Message texte à chiffrer ou déchiffrer.
  -o OUTPUT, --output OUTPUT
                        Nom du fichier de sortie pour le résultat.
