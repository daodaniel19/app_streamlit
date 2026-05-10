import streamlit as st
import plotly.express as px


def trouver_colonne(df, noms_possibles):
    for nom in noms_possibles:
        if nom in df.columns:
            return nom
    return None


def filtrer_modeles_initiaux(resultats_modeles):
    colonne_modele = trouver_colonne(resultats_modeles, ["Modèle", "Modele", "model"])

    if colonne_modele is None:
        return resultats_modeles

    noms_a_garder = [
        "Régression linéaire",
        "Régression Linéaire",
        "Random Forest",
        "Random Forest initial",
        "XGBoost",
        "XGBoost initial"
    ]

    resultats = resultats_modeles[
        resultats_modeles[colonne_modele].isin(noms_a_garder)
    ].copy()

    return resultats


def afficher_tableau_bord(resultats_modeles, importance_variables, references):
    st.markdown(
        '<div class="main-title">Tableau de bord global</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Synthèse des rendements et des performances du modèle</div>',
        unsafe_allow_html=True
    )

    resultats_initiaux = filtrer_modeles_initiaux(resultats_modeles)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Observations utilisées", references["nombre_observations"])

    with col2:
        st.metric("Rendement moyen global", f"{references['rendement_moyen_global']:.2f} t/ha")

    with col3:
        st.metric("Algorithme retenu", "XGBoost")

    with col4:
        st.metric("Performance R²", "52,4 %")

    st.markdown("---")

    col5, col6 = st.columns([1.1, 1])

    with col5:
        st.markdown(
            '<div class="section-title">Performance des modèles</div>',
            unsafe_allow_html=True
        )

        st.dataframe(resultats_initiaux, use_container_width=True)

        colonne_modele = trouver_colonne(resultats_initiaux, ["Modèle", "Modele", "model"])
        colonne_r2 = trouver_colonne(resultats_initiaux, ["R²", "R2", "r2"])
        colonne_rmse = trouver_colonne(resultats_initiaux, ["RMSE", "rmse"])

        if colonne_modele and colonne_r2:
            fig_r2 = px.bar(
                resultats_initiaux,
                x=colonne_modele,
                y=colonne_r2,
                title="Comparaison des modèles selon le R²",
                text_auto=".3f"
            )
            st.plotly_chart(fig_r2, use_container_width=True)

        if colonne_modele and colonne_rmse:
            fig_rmse = px.bar(
                resultats_initiaux,
                x=colonne_modele,
                y=colonne_rmse,
                title="Comparaison des modèles selon le RMSE",
                text_auto=".3f"
            )
            st.plotly_chart(fig_rmse, use_container_width=True)

    with col6:
        fig_imp = px.bar(
            importance_variables.head(15).sort_values("Importance"),
            x="Importance",
            y="Variable",
            orientation="h",
            title="Top 15 des variables importantes — XGBoost"
        )

        st.plotly_chart(fig_imp, use_container_width=True)

        st.markdown(
            """
            <div class="info-box">
            Le type de culture apparaît comme l’un des principaux facteurs de prédiction du rendement.
            Les variables liées aux semences, à la superficie et au responsable contribuent aussi au modèle.
            </div>
            """,
            unsafe_allow_html=True
        )