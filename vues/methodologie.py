import streamlit as st


def afficher_methodologie():
    st.markdown(
        '<div class="main-title">Méthodologie et limites</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Comprendre comment l’IA raisonne et quelles sont ses contraintes.</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-title">Interprétation générale</div>', unsafe_allow_html=True)

        st.write(
            """
            Le modèle XGBoost identifie principalement l’influence :
            
            - de la culture pratiquée ;
            - de l’intensité de semis ;
            - de la superficie ;
            - du type de semence ;
            - de certaines caractéristiques simples du responsable.
            """
        )

        st.write(
            """
            L’explication affichée repose sur l’importance globale des variables.
            Elle ne constitue pas une preuve de causalité.
            """
        )

    with col2:
        st.markdown('<div class="section-title">Limites du modèle</div>', unsafe_allow_html=True)

        st.write(
            """
            Le modèle repose uniquement sur les données EAC disponibles.
            Il n’intègre pas encore :
            
            - la pluviométrie ;
            - les caractéristiques du sol ;
            - les engrais et pesticides détaillés ;
            - les chocs climatiques ou sanitaires ;
            - la géolocalisation précise des parcelles.
            """
        )

    st.markdown("### Fonctionnement simplifié de l’algorithme")

    st.markdown(
        """
        <div class="info-box">
        XGBoost est un algorithme basé sur des arbres de décision successifs.
        Chaque nouvel arbre cherche à corriger les erreurs commises par les arbres précédents.
        Cette méthode permet de capter des relations non linéaires entre les variables.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Utilisation potentielle")

    with st.expander("Partenaires et utilisation possible"):
        st.write(
            """
            Cette application peut être mobilisée comme prototype d’aide à la décision pour :
            
            - les services techniques de l’État ;
            - les ONG et projets de développement ;
            - les institutions de financement agricole ;
            - les conseillers agricoles de terrain.
            """
        )