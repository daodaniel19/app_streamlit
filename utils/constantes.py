from pathlib import Path

# Dossier racine de l'application
RACINE = Path(__file__).resolve().parent.parent

# Dossiers
DOSSIER_ARTIFACTS = RACINE / "artifacts"
DOSSIER_STYLE = RACINE / "style"

# Fichiers artifacts
FICHIER_MODELE = DOSSIER_ARTIFACTS / "modele_xgboost_initial.joblib"
FICHIER_VARIABLES = DOSSIER_ARTIFACTS / "variables_modele.joblib"
FICHIER_REFERENCES = DOSSIER_ARTIFACTS / "statistiques_reference.joblib"
FICHIER_RESULTATS = DOSSIER_ARTIFACTS / "resultats_modeles.csv"
FICHIER_IMPORTANCE = DOSSIER_ARTIFACTS / "importance_variables_xgboost.csv"

# Fichier CSS
FICHIER_CSS = DOSSIER_STYLE / "style.css"

# Modalités utilisées dans l'interface
CULTURES = {
    "Maïs": "mais",
    "Mil": "mil",
    "Sorgho": "sorgho",
    "Riz": "riz",
    "Niébé": "niebe",
    "Arachide": "arachide"
}

TYPES_SEMENCES = [
    "locales",
    "améliorées pour la 1ère année",
    "améliorées pour la 2ème année",
    "améliorées pour la 3ème année",
    "améliorées. âge inconnu"
]

SEXES = ["Masculin", "Féminin"]