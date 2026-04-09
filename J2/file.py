import os
import json
from datetime import datetime, timedelta
from cryptography import Fernet 
import logger

cle=""

 # ===========================

class BackupManager:
    def __init__(self, dossier_source, nom_backup, cle=None):
        self.cle = cle if cle else Fernet.generate_key()
        self.archive_name  = f"{nom_backup}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
        self.manifeste_name = f"{self.archive_name}.manifest"
        self.chiffre_name   = f"{self.archive_name}.enc"

    def executer_sauvegarde(self):
        etapes = [("Archivage", self.archiver),
                  ("Manifeste", self.generer_manifeste),
                  ("Vérification", self.verifier_integrite),
                  ("Chiffrement", self.chiffrer)]
        for nom, fn in etapes:
            if not fn():
                logger.error(f"✗ Échec à l'étape: {nom}")
                return False
        return True

 # ===========================

def creer_cle_mensuelle(annee, mois):
    key = Fernet.generate_key()
    # TODO: Générer clé Fernet
    """cle = backup.key"""
    # TODO: Créer cles/backup_YYYY_MM.key

    # TODO: Permissions 0o600

    # TODO: Mettre à jour rotation.json
    return cle

def archiver_cle_ancienne(nom_cle):

    # TODO: Vérifier âge fichier

    # TODO: Si > 90j: déplacer archive/

    # TODO: Mettre à jour JSON + logger
    return True


def charger_cle_active():
    # TODO: Lire rotation.json
    # TODO: Récupérer clé active
    # TODO: Retourner bytes
    return True

 # ===========================


# Test
cle_jan = creer_cle_mensuelle(2024, 1)
cle_chargee = charger_cle_active()


assert cle_jan == cle_chargee #Vérification