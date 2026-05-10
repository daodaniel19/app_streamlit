import pandas as pd
import streamlit as st
import plotly.express as px

from utils.constantes import CULTURES, TYPES_SEMENCES, SEXES
from utils.prediction import predire_rendement


def formulaire_scenario(nom, cle):
    st.markdown(f"### {nom}")

    culture_affichage = st.selectbox(
        f"Culture {nom}",
        list(CULTURES.keys()),
        key=f"{cle}_culture"
    )

    nom_culture = CULTURES[culture_affichage]

    ha_culture = st.number_input(
        f"Superficie cultivée {nom} (ha)",
        min_value=0.01,
        value=1.00,
        step=0.10,
        key=f"{cle}_ha"
    )

    semence_utilisee_kg = st.number_input(
        f"Semence utilisée {nom} (kg)",
        min_value=0.00,
        value=20.00,
        step=1.00,
        key=f"{cle}_semence"
    )

    type_semence = st.selectbox(
        f"Type de semence {nom}",
        TYPES_SEMENCES,
        key=f"{cle}_type_semence"
    )

    age_exploitant = st.number_input(
        f"Âge du responsable {nom}",
        min_value=15,
        max_value=100,
        value=50,
        step=1,
        key=f"{cle}_age"
    )

    sexe_exploitant = st.selectbox(
        f"Sexe du responsable {nom}",
        SEXES,
        key=f"{cle}_sexe"
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

    affichage = {
        "Scénario": nom,
        "Culture": culture_affichage,
        "Superficie cultivée (ha)": ha_culture,
        "Semence utilisée (kg)": semence_utilisee_kg,
        "Semence par hectare": semence_par_ha,
        "Type de semence": type_semence,
        "Âge": age_exploitant,
        "Sexe": sexe_exploitant
    }

    return entrees, affichage


def afficher_scenarios(modele, variables_modele):
    st.markdown(
        '<div class="main-title">Comparateur de scénarios</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Comparer deux hypothèses de production selon la culture, les semences et la superficie.</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        entrees_a, affichage_a = formulaire_scenario("Scénario 1", "scenario_a")

    with col2:
        entrees_b, affichage_b = formulaire_scenario("Scénario 2", "scenario_b")

    if st.button("Comparer les scénarios", use_container_width=True):
        prediction_a, _ = predire_rendement(modele, entrees_a, variables_modele)
        prediction_b, _ = predire_rendement(modele, entrees_b, variables_modele)

        affichage_a["Rendement prédit (t/ha)"] = prediction_a
        affichage_b["Rendement prédit (t/ha)"] = prediction_b

        tableau = pd.DataFrame([affichage_a, affichage_b])

        st.markdown("### Résultats comparatifs")
        st.dataframe(tableau, use_container_width=True)

        fig = px.bar(
            tableau,
            x="Scénario",
            y="Rendement prédit (t/ha)",
            color="Culture",
            title="Comparaison des rendements prédits"
        )

        st.plotly_chart(fig, use_container_width=True)

        difference = prediction_b - prediction_a

        if difference > 0:
            st.success(f"Le scénario 2 présente un rendement estimé supérieur de {difference:.3f} t/ha.")
        elif difference < 0:
            st.warning(f"Le scénario 1 présente un rendement estimé supérieur de {abs(difference):.3f} t/ha.")
        else:
            st.info("Les deux scénarios présentent le même rendement estimé.")

        st.markdown(
            """
            <div class="warning-box">
            Cette comparaison est une simulation statistique. Elle permet d’explorer des hypothèses,
            mais ne constitue pas une recommandation agronomique définitive.
            </div>
            """,
            unsafe_allow_html=True
        )