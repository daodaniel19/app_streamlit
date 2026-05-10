import joblib
import pandas as pd
import streamlit as st

from utils.constantes import (
    FICHIER_MODELE,
    FICHIER_VARIABLES,
    FICHIER_REFERENCES,
    FICHIER_RESULTATS,
    FICHIER_IMPORTANCE,
    FICHIER_CSS
)


@st.cache_resource
def charger_modele():
    return joblib.load(FICHIER_MODELE)


@st.cache_resource
def charger_variables():
    return joblib.load(FICHIER_VARIABLES)


@st.cache_resource
def charger_references():
    return joblib.load(FICHIER_REFERENCES)


@st.cache_data
def charger_resultats():
    return pd.read_csv(FICHIER_RESULTATS)


@st.cache_data
def charger_importance():
    return pd.read_csv(FICHIER_IMPORTANCE)


def charger_css():
    with open(FICHIER_CSS, "r", encoding="utf-8") as fichier:
        css = fichier.read()

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )