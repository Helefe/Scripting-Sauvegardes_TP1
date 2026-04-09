import zipfile

def creer_archive_simple(nom_archive, fichiers_liste):
    """Crée une archive ZIP"""
    with zipfile.ZipFile(nom_archive, 'w',zipfile.ZIP_DEFLATED) as zf: # ??? classe zipfile / mode écriture ?
        for fichier in fichiers_liste:
            zf.write(fichier)   # ??? méthode pour ajouter ?

def lister_archive(nom_archive):
    """Affiche la liste des fichiers"""
    with zipfile.ZipFile(nom_archive, 'r') as zf: # ??? mode lecture ?
        zf.printdir()               # ??? objet ?