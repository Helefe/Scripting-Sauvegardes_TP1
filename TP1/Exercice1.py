chemin_entree = "C:\\Users\\helef\\Desktop\\Nouveau Document texte.txt"
chemin_sortie = "C:\\Users\\helef\\Desktop\\Nouveau Document texte2.txt"
from cryptography.fernet import Fernet


# Lire un fichier texte
def lire_fichier(chemin):
    with open(chemin, 'r', encoding='utf-8') as f:
        contenu = f.read()
    return contenu


# Écrire du contenu
def ecrire_fichier(chemin, contenu):
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write(contenu)
        
        
def lire_fichier_binaire(chemin):
    #Lit un fichier en mode binaire
    with open(chemin, 'rb') as f:  # ??? mode?
        contenu = f.read()
    return contenu


def obtenir_taille_fichier(chemin):
    #Retourne la taille en octets
    import os
    return os.path.getsize(chemin)  # ??? utiliser os


def chiffrer_message(message, cle):
    #Chiffre un message avec la clé fournie
    f = Fernet(cle)
    message_bytes = message.encode()  # string -> bytes
    ciphertext = f.encrypt(message_bytes)
    return ciphertext


def dechiffrer_message(ciphertext, cle):
    #Déchiffre un ciphertext
    f = Fernet(cle)
    plaintext_bytes = f.decrypt(ciphertext)
    plaintext = plaintext_bytes.decode()  # bytes -> string
    return plaintext


def chiffrer_fichier(chemin_entree, chemin_sortie, cle):
    """Lit un fichier, le chiffre et l'enregistre"""
    # 1. Lire le fichier en binaire
    contenu = lire_fichier(chemin_entree)  # ??? fonction Partie A
    # 2. Chiffrer le contenu
    ciphertext = chiffrer_message(contenu, cle)  # ??? fonction Partie B
    # 3. Écrire le fichier chiffré en binaire
    #print(ciphertext)
    with open(chemin_sortie, 'wb') as f:  # ??? mode?
        f.write(ciphertext)

def dechiffrer_fichier(chemin_entree, cle):
    contenu = lire_fichier(chemin_entree)
    return dechiffrer_message(contenu,cle)



key = Fernet.generate_key()     
chiffrer_fichier(chemin_entree,chemin_sortie,key)
print(lire_fichier(chemin_entree))
print(lire_fichier(chemin_sortie))
print(dechiffrer_fichier(chemin_sortie,key))

