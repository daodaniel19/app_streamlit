import numpy as np
import pandas as pd


def classer_rendement(valeur, seuil_bas, seuil_haut):
    if valeur <= seuil_bas:
        return "Faible"
    elif valeur <= seuil_haut:
        return "Moyen"
    else:
        return "Élevé"


def construire_ligne_prediction(entrees, variables_modele):
    ligne = {}

    for variable in variables_modele:
        ligne[variable] = entrees.get(variable, np.nan)

    return pd.DataFrame([ligne])


def predire_rendement(modele, entrees, variables_modele):
    ligne_prediction = construire_ligne_prediction(entrees, variables_modele)
    prediction = modele.predict(ligne_prediction)[0]

    return float(prediction), ligne_prediction


def commenter_prediction(prediction, culture, references):
    moyenne_culture = references["rendement_moyen_par_culture"].get(culture)
    moyenne_globale = references["rendement_moyen_global"]

    if moyenne_culture is not None:
        if prediction > moyenne_culture:
            return f"Le rendement prédit est supérieur à la moyenne observée pour la culture {culture}."
        elif prediction < moyenne_culture:
            return f"Le rendement prédit est inférieur à la moyenne observée pour la culture {culture}."
        else:
            return f"Le rendement prédit est proche de la moyenne observée pour la culture {culture}."

    if prediction > moyenne_globale:
        return "Le rendement prédit est supérieur à la moyenne globale."
    elif prediction < moyenne_globale:
        return "Le rendement prédit est inférieur à la moyenne globale."
    else:
        return "Le rendement prédit est proche de la moyenne globale."