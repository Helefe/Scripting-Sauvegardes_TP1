import hashlib
import json
import os
from datetime import datetime

chemin = "C:\\Users\\helef\\Desktop\\data.bin"

def calculer_hash_fichier(chemin):
    # le SHA-256 d'un fichier
    hasher = hashlib.sha256()
    
    # Lire par bloc de 4KB (économe en mémoire)
    with open(chemin, 'rb') as f:
        for bloc in iter(lambda: f.read(4096), b''):
            hasher.update(bloc)
    
    return hasher.hexdigest()  # Retourne hex string


def fichiers_identiques(chemin1, chemin2):
    #Vérifie si deux fichiers sont identiques
    hash1 = calculer_hash_fichier(chemin1)
    # ??? fonction précédente ?
    hash2 = calculer_hash_fichier(chemin2)
    if hash1 == hash2:
        return True
    return False






def creer_manifeste(dossier_source, fichiers_liste):
    manifeste = {
        "timestamp": (datetime.now().isoformat()),  # ??? ISO format ?
        "total_fichiers": len(fichiers_liste),                                 # ??? len(fichiers_liste) ?
        "fichiers": []
    }
    total_octets = 0
    for fichier in fichiers_liste:
        chemin_complet = f"{dossier_source}/{fichier}"
        hash_val = calculer_hash_fichier(chemin_complet)        # ??? fonction B1 ?
        taille   = os.path.getsize(chemin_complet)      # ??? os.path.getsize ?
        manifeste["fichiers"].append({
            "chemin": fichier, "hash": hash_val, "taille": taille
        })
        total_octets += taille
    manifeste["total_octets"] = total_octets
    with open("backup.manifest", "w") as f:
        json.dump(manifeste, f, indent=2)         # ??? json.dump ?
        
        
def verifier_manifeste(dossier, manifeste_path):
    with open(manifeste_path, 'r') as f:
        manifeste = json.load(f)
    resultats = []
    for fichier_info in manifeste["fichiers"]:
        chemin       = f"{dossier}/{fichier_info['chemin']}"
        hash_calcule = calculer_hash_fichier(chemin)             # ??? fonction B1 ?
        hash_attendu = fichier_info['hash']
        est_valide   = fichiers_identiques               # ??? comparer les deux hash ?
        resultats.append({"fichier": fichier_info['chemin'],
                          "valide": est_valide})
    return resultats

for item in verifier_manifeste('/data', 'backup.manifest'):
    statut = "✓ OK" if item['valide'] else "✗ CORROMPU"
    print(f"{item['fichier']}: {statut}")
        

# Test
hash_resultat = calculer_hash_fichier(chemin)
#print(f"SHA-256: {hash_resultat}")
#print(fichiers_identiques(chemin,chemin))

#https://gamma.app/docs/TP-2-Hash-SHA-256-Verification-dIntegrite-psm1604hrx3nkbm?mode=doc