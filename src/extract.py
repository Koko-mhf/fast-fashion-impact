import logging
from src.config import RAW_FILES

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

def verify_raw_data() -> bool:
    """Vérifie que tous les fichiers bruts listés dans RAW_FILES existent."""
    logging.info("Extract")
    tous_fichiers_ok = True
    for nom_fichier, chemin in RAW_FILES.items():
        if chemin.exists():
            logging.info(f"OK : Le fichier '{nom_fichier}' est présent à l'emplacement : {chemin}")
        else:
            logging.error(f"ERREUR : Le fichier '{nom_fichier}' est INTROUVABLE à l'emplacement : {chemin}")
            tous_fichiers_ok = False
            
    if tous_fichiers_ok:
        logging.info("L'étape EXTRACT est un succès. Les données brutes sont disponibles.")
    else:
        logging.critical("L'étape EXTRACT a échoué. Des fichiers sont manquants.")
        
    return tous_fichiers_ok

if __name__ == "__main__":
    verify_raw_data()