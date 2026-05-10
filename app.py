import streamlit as st

from utils.chargement import (
    charger_modele,
    charger_variables,
    charger_references,
    charger_resultats,
    charger_importance,
    charger_css
)

from vues.accueil import afficher_accueil
from vues.tableau_bord import afficher_tableau_bord
from vues.simulateur import afficher_simulateur
from vues.scenarios import afficher_scenarios
from vues.methodologie import afficher_methodologie


# =========================
# CONFIGURATION GÉNÉRALE
# =========================

st.set_page_config(
    page_title="AgriYield Sikasso",
    page_icon="🌾",
    layout="wide"
)


# =========================
# CHARGEMENT DU STYLE
# =========================

charger_css()


# =========================
# CHARGEMENT DES RESSOURCES
# =========================

modele = charger_modele()
variables_modele = charger_variables()
references = charger_references()
resultats_modeles = charger_resultats()
importance_variables = charger_importance()


# =========================
# BARRE LATÉRALE
# =========================

st.sidebar.markdown("## 🌾 AgriYield Sikasso")

page = st.sidebar.radio(
    label="",
    options=[
        "Accueil",
        "Tableau de bord",
        "Simulateur",
        "Scénarios",
        "Méthodologie"
    ],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.caption("Mémoire — Prédiction du rendement agricole à Sikasso")


# =========================
# ROUTAGE DES PAGES
# =========================

if page == "Accueil":
    afficher_accueil(references)

elif page == "Tableau de bord":
    afficher_tableau_bord(
        resultats_modeles,
        importance_variables,
        references
    )

elif page == "Simulateur":
    afficher_simulateur(
        modele,
        variables_modele,
        references
    )

elif page == "Scénarios":
    afficher_scenarios(
        modele,
        variables_modele
    )

elif page == "Méthodologie":
    afficher_methodologie()
