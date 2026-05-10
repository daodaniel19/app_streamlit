import streamlit as st


def afficher_accueil(references):
    st.markdown(
        """
        <style>
            .stApp {
                background: #f8fdf5;
            }

            [data-testid="stAppViewContainer"] {
                background: #f8fdf5;
            }

            [data-testid="stToolbar"] {
                background: rgba(248, 253, 245, 0.92);
                border-bottom: 1px solid rgba(31, 92, 61, 0.08);
                backdrop-filter: blur(8px);
            }

            [data-testid="stToolbar"] button {
                border-radius: 8px !important;
                color: #374151 !important;
            }

            [data-testid="stAppDeployButton"] button {
                background: #ffffff !important;
                border: 1px solid #e5e7eb !important;
                box-shadow: none !important;
                color: #1f5c3d !important;
                font-size: 14px !important;
                font-weight: 700 !important;
                min-height: 34px !important;
            }

            [data-testid="stMainMenu"] button {
                color: #374151 !important;
            }

            .block-container {
                max-width: 1340px;
                padding-top: 4.75rem;
            }

            .home-hero {
                margin: 0 0 2.25rem;
                text-align: left;
            }

            .home-brand {
                align-items: center;
                display: flex;
                gap: 18px;
                justify-content: flex-start;
                margin-bottom: 18px;
            }

            .home-logo {
                height: 48px;
                position: relative;
                width: 58px;
            }

            .home-logo .stem {
                background: #266b55;
                border-radius: 999px;
                bottom: 1px;
                position: absolute;
                width: 6px;
            }

            .home-logo .stem::before,
            .home-logo .stem::after {
                background: #ffd044;
                border-radius: 999px;
                content: "";
                height: 5px;
                position: absolute;
                right: -15px;
                width: 22px;
            }

            .home-logo .stem::before {
                top: 2px;
            }

            .home-logo .stem::after {
                top: 13px;
                width: 17px;
            }

            .home-logo .leaf {
                background: linear-gradient(135deg, #9abd55, #28715b);
                border-radius: 18px 2px 18px 2px;
                bottom: 0;
                height: 22px;
                position: absolute;
                width: 11px;
            }

            .home-logo .leaf.left {
                left: 5px;
                transform: rotate(-24deg);
            }

            .home-logo .leaf.right {
                left: 28px;
                transform: rotate(22deg);
            }

            .home-logo .stem.one {
                height: 35px;
                left: 18px;
            }

            .home-logo .stem.two {
                height: 44px;
                left: 26px;
            }

            .home-logo .stem.three {
                height: 29px;
                left: 35px;
            }

            .home-hero .main-title {
                color: #184f36;
                font-size: 42px;
                font-weight: 900;
                line-height: 1.1;
                margin: 0;
            }

            .home-hero .subtitle {
                color: #3d8a62;
                font-size: 20px;
                font-weight: 500;
                line-height: 1.35;
                margin: 0;
            }

            .home-card {
                background: #ffffff;
                border: 1px solid #e5eadf;
                border-radius: 16px;
                box-shadow: 0 10px 22px rgba(31, 41, 55, 0.06);
                color: #26364d;
                min-height: 278px;
                padding: 26px 30px;
            }

            .home-card h2 {
                color: #19314f;
                font-size: 22px;
                font-weight: 800;
                margin: 0;
            }

            .home-rule {
                background: #2d7a52;
                height: 2px;
                margin: 14px 0 20px;
                width: 230px;
            }

            .home-card p,
            .home-card li {
                color: #26364d;
                font-size: 17px;
                line-height: 1.58;
            }

            .home-card p {
                margin: 0 0 18px;
            }

            .home-card ul {
                margin: 0;
                padding-left: 28px;
            }

            .home-card li {
                margin-bottom: 9px;
            }

            .home-after {
                margin-top: 20px;
            }

            .home-metric {
                background: #ffffff;
                border: 1px solid #e5eadf;
                border-radius: 12px;
                box-shadow: 0 6px 16px rgba(31, 41, 55, 0.045);
                padding: 16px 18px;
            }

            .home-metric span {
                color: #5b6678;
                display: block;
                font-size: 14px;
                font-weight: 700;
                margin-bottom: 6px;
            }

            .home-metric strong {
                color: #184f36;
                display: block;
                font-size: 24px;
                font-weight: 900;
                line-height: 1.2;
            }

            .home-warning {
                background: #fff8e5;
                border-left: 4px solid #d49b00;
                border-radius: 10px;
                color: #293647;
                font-size: 15px;
                line-height: 1.55;
                margin-top: 18px;
                padding: 14px 18px;
            }

            @media (max-width: 900px) {
                .block-container {
                    padding-top: 2.5rem;
                }

                .home-brand {
                    gap: 14px;
                }

                .home-hero .main-title {
                    font-size: 32px;
                }

                .home-hero .subtitle {
                    font-size: 17px;
                }

                .home-card,
                .home-metric {
                    margin-bottom: 16px;
                    min-height: auto;
                }

                .home-rule {
                    width: 180px;
                }
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="home-hero">
            <div class="home-brand">
                <div class="home-logo" aria-hidden="true">
                    <span class="leaf left"></span>
                    <span class="leaf right"></span>
                    <span class="stem one"></span>
                    <span class="stem two"></span>
                    <span class="stem three"></span>
                </div>
                <div class="main-title">AgriYield Sikasso</div>
            </div>
            <div class="subtitle">
                Intelligence artificielle au service de la prédiction de rendement agricole
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1.58, 1], gap="large")

    with col1:
        st.markdown(
            """
            <div class="home-card">
                <h2>Bienvenue sur AgriYield</h2>
                <div class="home-rule"></div>
                <p>
                    AgriYield est un prototype innovant d'aide à la décision conçu pour l'agriculture
                    malienne. En exploitant les données de l'Enquête Agricole de Conjoncture (EAC) et
                    des algorithmes de <strong>Machine Learning (XGBoost)</strong>, cet outil permet d'estimer
                    avec précision le rendement à l'échelle de la parcelle.
                </p>
                <p>
                    Il s'adresse aux <strong>conseillers agricoles, planificateurs, ONG et institutions
                    financières</strong> pour appuyer leurs décisions stratégiques et opérationnelles.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="home-card">
                <h2>Fonctionnalités</h2>
                <div class="home-rule"></div>
                <ul>
                    <li><strong>Tableau de Bord</strong> : Vue synthétique des rendements.</li>
                    <li><strong>Simulateur</strong> : prédiction personnalisée sur une parcelle</li>
                    <li><strong>Comparateur</strong> : Analyse d'impact des pratiques.</li>
                    <li><strong>Méthodologie</strong> : Explication du modèle IA.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="home-after"></div>', unsafe_allow_html=True)

    col3, col4, col5 = st.columns(3, gap="large")

    with col3:
        st.markdown(
            f"""
            <div class="home-metric">
                <span>Observations utilisées</span>
                <strong>{references["nombre_observations"]}</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="home-metric">
                <span>Rendement moyen global</span>
                <strong>{references['rendement_moyen_global']:.2f} t/ha</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col5:
        st.markdown(
            """
            <div class="home-metric">
                <span>Modèle final</span>
                <strong>XGBoost</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="home-warning">
            Cette application fournit une estimation statistique. Elle ne remplace pas l’expertise agronomique
            ni l’observation directe de la parcelle.
        </div>
        """,
        unsafe_allow_html=True
    )
