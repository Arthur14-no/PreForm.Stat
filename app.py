import streamlit as st
import pandas as pd
import os

# Configuration de la page
st.set_page_config(
    page_title="PréForm.Stat - Suivi des joueurs",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé forcé
st.markdown("""
    <style>
    /* Fond principal noir */
    .stApp {
        background-color: #0D0D0D !important;
    }
    
    /* Texte en blanc */
    body, .stMarkdown, p, div, span {
        color: #FFFFFF !important;
    }
    
    /* Titres en orange */
    h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #F39C12 !important;
    }
    
    /* Boutons orange */
    .stButton button {
        background-color: #F39C12 !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: none !important;
    }
    
    .stButton button:hover {
        background-color: #E67E22 !important;
        color: #FFFFFF !important;
    }
    
    /* Sidebar sombre */
    [data-testid="stSidebar"] {
        background-color: #1A1A1A !important;
    }
    </style>
""", unsafe_allow_html=True)

# CSS personnalisé pour le thème noir/orange
st.markdown("""
    <style>
    .stApp {
        background-color: #0D0D0D;
        
    }
    h1, h2, h3 {
        color: #F39C12 !important;
        font-family: 'Cinzel';
    }
    .stButton button {
        background-color: #F39C12;
        color: black;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #E67E22;
    }
    </style>
""", unsafe_allow_html=True)

# Initialisation du fichier CSV
DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR, "joueurs.csv")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

if not os.path.exists(CSV_FILE):
    df_empty = pd.DataFrame(columns=[
        "Date_saisie", "Nom", "Date_naissance", "Age", "Poste", "Numero_maillot",
        "Pied_fort", "Taille_cm", "Poids_kg", "Nationalite", "Matchs_joues",
        "Buts", "Passes_decisives", "Note_moyenne", "Minutes_jouees", "Commentaires"
    ])
    df_empty.to_csv(CSV_FILE, index=False)

# Sidebar commune à toutes les pages
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3095/3095129.png", width=80)
    st.markdown("# ⚽ PréForm.Stat")
    st.markdown("---")
    st.page_link("app.py", label=" Accueil", icon="🏠")
    st.page_link("pages/2_Ajouter_Joueur.py", label=" Ajouter un joueur", icon="📝")
    st.page_link("pages/3_Liste_Joueurs.py", label=" Liste des joueurs", icon="📋")
    st.page_link("pages/4_Statistiques.py", label=" Statistiques", icon="📊")
    st.markdown("---")
    st.caption("© 2025 - PréForm.Stat")
    st.caption("Version 2.0 | Thème Noir & Orange")

# Page d'accueil (contenu direct dans app.py)
st.title("⚽ PréForm.Stat")
st.markdown("## Bienvenue dans l'application de suivi des joueurs")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ###      À propos
    **PréForm.Stat** est une application professionnelle conçue pour :
    -  **Collecter** les données des joueurs (personnelles, physiques, performances)
    -  **Analyser** les statistiques en temps réel
    -  **Exporter** les données pour des analyses approfondies
    
    ###      Objectif
    Aider les entraîneurs et staff technique à suivre l'évolution des joueurs,
    identifier les talents et prendre des décisions basées sur des données concrètes.
    """)

with col2:
    st.markdown("""
    ###  Navigation rapide
    - **Ajouter un joueur** → Remplir le formulaire
    - **Liste des joueurs** → Consulter et exporter
    - **Statistiques** → Visualiser les graphiques
    """)

st.markdown("---")
st.info(" **Conseil** : Utilisez le menu latéral pour naviguer entre les pages.")