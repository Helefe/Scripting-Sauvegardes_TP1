chemin = "C:\\Users\\helef\\Desktop\\Nouveau Document texte.txt"

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
    """Lit un fichier en mode binaire"""
    with open(chemin, 'rb') as f:  # ??? mode?
        contenu = f.read()
    return contenu

def obtenir_taille_fichier(chemin):
    """Retourne la taille en octets"""
    import os
    return os.path.getsize(chemin)  # ??? utiliser os


print(lire_fichier(chemin))