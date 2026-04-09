import hashlib
import json
import os
from datetime import datetime

chemin = "C:\\Users\\Helefe\\OneDrive\\Bureau\\data.bin"

def calculer_hash_fichier(chemin):
    """Calcule le SHA-256 d'un fichier."""
    hasher = hashlib.sha256()
    with open(chemin, 'rb') as f:
        for bloc in iter(lambda: f.read(4096), b''):
            hasher.update(bloc)
    return hasher.hexdigest()


def fichiers_identiques(chemin1, chemin2):
    """Vérifie si deux fichiers sont identiques via leur hash."""
    hash1 = calculer_hash_fichier(chemin1)
    hash2 = calculer_hash_fichier(chemin2)
    return hash1 == hash2  # simplifié


def creer_manifeste(dossier_source, fichiers_liste):
    manifeste = {
        "timestamp": datetime.now().isoformat(),
        "total_fichiers": len(fichiers_liste),
        "fichiers": []
    }
    total_octets = 0
    for fichier in fichiers_liste:
        chemin_complet = os.path.join(dossier_source, fichier)  # ✅ os.path.join
        hash_val = calculer_hash_fichier(chemin_complet)
        taille   = os.path.getsize(chemin_complet)
        manifeste["fichiers"].append({
            "chemin": fichier,
            "hash": hash_val,
            "taille": taille
        })
        total_octets += taille
    manifeste["total_octets"] = total_octets
    with open("backup.manifest", "w") as f:
        json.dump(manifeste, f, indent=2)


def verifier_manifeste(dossier, manifeste_path):
    with open(manifeste_path, 'r') as f:
        manifeste = json.load(f)
    resultats = []
    for fichier_info in manifeste["fichiers"]:
        chemin_complet = os.path.join(dossier, fichier_info['chemin']) 
        hash_calcule   = calculer_hash_fichier(chemin_complet)
        hash_attendu   = fichier_info['hash']
        est_valide     = (hash_calcule == hash_attendu)  
        resultats.append({
            "fichier": fichier_info['chemin'],
            "valide": est_valide
        })
    return resultats


# --- Tests ---
hash_resultat = calculer_hash_fichier(chemin)
print(f"SHA-256: {hash_resultat}")
print(f"Fichiers identiques (même fichier) : {fichiers_identiques(chemin, chemin)}")

# Pour tester creer_manifeste + verifier_manifeste :
# creer_manifeste("C:\\Users\\helef\\Desktop", ["data.bin"])
# for item in verifier_manifeste("C:\\Users\\helef\\Desktop", "backup.manifest"):
#     statut = "✓ OK" if item['valide'] else "✗ CORROMPU"
#     print(f"{item['fichier']}: {statut}")