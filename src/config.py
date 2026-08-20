from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
DB_PATH = BASE_DIR / "data" / "fast_fashion.duckdb"

RAW_FILES = {
    "fast_fashion_composition":"fastFashionCompDim.csv",
    "items_fast_fashion":"fastFashionItemsDim.csv",
    "trends2024":"sustainable_fashion_trends_2024.csv",
    "cost":"true_cost_fast_fashion.csv",
}

COLUMN_MAPPING = {
    "fast_fashion_composition": { 
        "Item Code": "item_code", 
        "Part Name": "partie_vetement", 
        "Material": "matiere", 
        "Percent": "pourcentage" 
    },
    "items_fast_fashion": {
        "item_code": "id_produit",
        "item_name": "nom_produit",
        "item_desc": "description_produit",
        "join_life": "est_eco_concu",
        "joinlife_title": "label_eco",
        "joinlife_desc": "description_label_eco",
        "item_price": "prix_usd"
    },
    "trends2024": {
        "Brand_ID": "id_marque",
        "Brand_Name": "nom_marque",    
        "Country": "pays",
        "Year": "annee",
        "Sustainability_Rating": "note_durabilite",
        "Material_Type": "type_materiel_dominant",
        "Eco_Friendlyc_Manufacturing": "fabrication_eco",
        "Carbon_Footprint_MT": "empreinte_carbone_mt",
        "Water_Usage_Liters": "consommation_eau_litres",
        "Waste_Production_KG": "production_dechets_kg",
        "Recycling_Programs": "programmes_recyclage",
        "Product_Lines": "lignes_produits",
        "Average_Price_USD": "prix_moyen_usd",
        "Market_Trend": "tendance_marche",
        "Certifications": "certifications"
    },
    "cost": {
       "Brand": "nom_marque",         
        "Country": "pays",
        "Year": "annee",
        "Monthly_Production_Tonnes": "production_mensuelle_tonnes",
        "Avg_Item_Price_USD": "prix_moyen_article_usd",
        "Release_Cycles_Per_Year": "cycles_collection_par_an",
        "Carbon_Emissions_tCO2e": "emissions_carbone_tco2e",
        "Water_Usage_Million_Litres": "consommation_eau_millions_litres",
        "Landfill_Waste_Tonnes": "dechets_enfouis_tonnes",
        "Avg_Worker_Wage_USD": "salaire_moyen_ouvrier_usd",
        "Working_Hours_Per_Week": "heures_travail_hebdo",
        "Child_Labor_Incidents": "incidents_travail_infantile",
        "Return_Rate_Percent": "taux_retour_pourcentage",
        "Avg_Spend_Per_Customer_USD": "depense_moyenne_client_usd",
        "Shopping_Frequency_Per_Year": "frequence_achat_par_an",
        "Instagram_Mentions_Thousands": "mentions_instagram_k",
        "TikTok_Mentions_Thousands": "mentions_tiktok_k",
        "Sentiment_Score": "score_sentiment",
        "Social_Sentiment_Label": "label_sentiment_social",
        "GDP_Contribution_Million_USD": "contribution_pib_millions_usd",
        "Env_Cost_Index": "indice_cout_environnemental",
        "Sustainability_Score": "score_durabilite",
        "Transparency_Index": "indice_transparence",
        "Compliance_Score": "score_conformite",
        "Ethical_Rating": "note_ethique"
    }
}

SCORE_WEIGHTS = {
    "empreinte_carbone_mt": 0.4,
    "consommation_eau_litres": 0.3,
    "production_dechets_kg": 0.3,

}