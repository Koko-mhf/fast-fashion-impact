import logging
import sys
 
from src.extract import verify_raw_data
from src.transform import transform_and_load
from src.load import export_to_parquet
from src.config import PROCESSED_DIR

# Configuration globale du logger pour l'orchestrateur
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger("Orchestrateur_ETL")

def run_pipeline():
    logger.info("Démarrage du pipeline ETL Fast Fashion...")
    
    # ---------------------------------------------------------
    # ÉTAPE 1 : EXTRACT
    # ---------------------------------------------------------
    logger.info("=== Étape 1/3 : Extraction (Vérification des sources) ===")
    if not verify_raw_data():
        logger.error(" Échec critique de l'étape Extract. Arrêt du pipeline.")
        sys.exit(1) # Code 1 signifie qu'il y a eu une erreur
        
    # ---------------------------------------------------------
    # ÉTAPE 2 : TRANSFORM
    # ---------------------------------------------------------
    logger.info("=== Étape 2/3 : Transformation et intégration DuckDB ===")
    try:
        transform_and_load()
    except Exception as e:
        logger.error(f" Échec de l'étape Transform : {e}")
        sys.exit(1)
        
    # ---------------------------------------------------------
    # ÉTAPE 3 : LOAD
    # ---------------------------------------------------------
    logger.info("=== Étape 3/3 : Load (Export vers Parquet) ===")
    try:
        # On s'assure que le dossier d'export existe avant d'écrire
        PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
        export_to_parquet()
    except Exception as e:
        logger.error(f" Échec de l'étape Load : {e}")
        sys.exit(1)
        
    logger.info(" Pipeline ETL terminé avec succès ! Les données (Couche Gold) sont prêtes.")

if __name__ == "__main__":
    run_pipeline()