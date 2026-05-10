import pandas as pd
import streamlit as st

from utils.constantes import CULTURES, TYPES_SEMENCES, SEXES
from utils.prediction import (
    predire_rendement,
    classer_rendement,
    commenter_prediction
)


def afficher_simulateur(modele, variables_modele, references):
    st.markdown(
        '<div class="main-title">Simulateur interactif</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Estimer le rendement d’une parcelle à partir de quelques caractéristiques simples.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">
        Renseignez les informations disponibles sur la parcelle et le responsable.
        L’application calcule automatiquement les variables nécessaires au modèle.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        culture_affichage = st.selectbox(
            "Culture",
            list(CULTURES.keys())
        )

        nom_culture = CULTURES[culture_affichage]

        ha_culture = st.number_input(
            "Superficie cultivée (ha)",
            min_value=0.01,
            value=1.00,
            step=0.10
        )

        semence_utilisee_kg = st.number_input(
            "Quantité totale de semence utilisée (kg)",
            min_value=0.00,
            value=20.00,
            step=1.00
        )

    with col2:
        type_semence = st.selectbox(
            "Type de semence",
            TYPES_SEMENCES
        )

        age_exploitant = st.number_input(
            "Âge du responsable",
            min_value=15,
            max_value=100,
            value=50,
            step=1
        )

        sexe_exploitant = st.selectbox(
            "Sexe du responsable",
            SEXES
        )

    semence_par_ha = semence_utilisee_kg / ha_culture
    interaction_surface_semence = ha_culture * semence_par_ha

    entrees = {
        "ha_culture": ha_culture,
        "semence_par_ha": semence_par_ha,
        "interaction_surface_semence": interaction_surface_semence,
        "age_exploitant": age_exploitant,
        "sexe_exploitant": sexe_exploitant,
        "nom_culture": nom_culture,
        "type_semence": type_semence
    }

    if st.button("Prédire le rendement", use_container_width=True):
        prediction, ligne_prediction = predire_rendement(
            modele,
            entrees,
            variables_modele
        )

        classe = classer_rendement(
            prediction,
            references["q33_rendement"],
            references["q66_rendement"]
        )

        commentaire = commenter_prediction(
            prediction,
            nom_culture,
            references
        )

        st.markdown("---")

        st.success(f"Rendement prédit : {prediction:.3f} t/ha")

        st.info(f"Classe estimée : {classe}")

        st.write(commentaire)

        st.markdown("### Données utilisées pour la prédiction")

        tableau_saisie = pd.DataFrame([{
            "Culture": culture_affichage,
            "Superficie cultivée (ha)": ha_culture,
            "Semence utilisée (kg)": semence_utilisee_kg,
            "Semence par hectare": round(semence_par_ha, 3),
            "Interaction surface-semence": round(interaction_surface_semence, 3),
            "Type de semence": type_semence,
            "Âge du responsable": age_exploitant,
            "Sexe du responsable": sexe_exploitant
        }])

        st.dataframe(
            tableau_saisie,
            use_container_width=True
        )

        st.markdown(
            """
            <div class="warning-box">
            Cette prédiction est une estimation statistique basée sur les données EAC disponibles.
            Elle doit être interprétée comme un outil d’aide à la décision, et non comme une valeur certaine.
            </div>
            """,
            unsafe_allow_html=True
        )