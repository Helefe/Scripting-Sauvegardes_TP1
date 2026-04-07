"""

from cryptography.fernet import Fernet

def chiffrer_message(message, cle):
    #Chiffre un message avec la clé fournie
    chiffre = Fernet(cle)       # ??? quel objet?
    print(chiffre)
    message_bytes = chiffre.encode(message)  # ??? convertir en bytes
    print(message_bytes)
    ciphertext = chiffre.encrypt(message_bytes)  # ??? méthode?
    return ciphertext

def dechiffrer_message(ciphertext, cle):
    #Déchiffre un ciphertext
    chiffre = Fernet(cle)
    plaintext = chiffre.decrypt(ciphertext)  # ??? méthode?
    return chiffre.decode(plaintext)        # ??? convertir en string  



key = Fernet.generate_key()

print(chiffrer_message("Bonjour",key))
"""

from cryptography.fernet import Fernet

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


# Génération de clé
key = Fernet.generate_key()

# Test
cipher = chiffrer_message("Bonjour", key)
print("Chiffré :", cipher)

message = dechiffrer_message(cipher, key)
print("Déchiffré :", message)