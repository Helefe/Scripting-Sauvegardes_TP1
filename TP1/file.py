chemin = "C:\Users\helef\Desktop\Nouveau Document texte.txt"

# Lire un fichier texte
def lire_fichier(chemin):
    with open(chemin, 'r', encoding='utf-8') as f:
        contenu = f.read()
    return contenu

# Écrire du contenu
def ecrire_fichier(chemin, contenu):
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write(contenu)