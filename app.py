import streamlit as st
import pandas as pd
import os
from datetime import datetime, date

st.set_page_config(
    page_title="PréForm.Stat - Suivi des joueurs",
    page_icon="⚽",
    layout="wide"
)

# CSS personnalisé
st.markdown("""
    <style>
    .stApp { background-color: #0D0D0D; }
    h1, h2, h3 { color: #F39C12 !important; }
    .stButton button { background-color: #F39C12; color: black; font-weight: bold; }
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

# Sidebar
with st.sidebar:
    st.markdown("# ⚽ PréForm.Stat")
    st.markdown("---")
    menu = st.radio("Menu", ["🏠 Accueil", "📝 Ajouter", "📋 Liste", "📊 Stats"])

# Menu Accueil
if menu == "🏠 Accueil":
    st.title("⚽ PréForm.Stat")
    st.markdown("## Bienvenue !")
    data = pd.read_csv(CSV_FILE)
    st.metric("🏃 Joueurs enregistrés", len(data))

# Menu Ajouter
elif menu == "📝 Ajouter":
    st.title("Ajouter un joueur")
    
    with st.form("form"):
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom")
            poste = st.selectbox("Poste", ["Gardien", "Défenseur", "Milieu", "Attaquant"])
        with col2:
            buts = st.number_input("Buts", min_value=0)
            note = st.slider("Note", 0.0, 10.0, 5.0)
        
        if st.form_submit_button("Enregistrer"):
            new_row = pd.DataFrame([{
                "Date_saisie": datetime.now().strftime("%Y-%m-%d"),
                "Nom": nom, "Poste": poste, "Buts": buts, "Note_moyenne": note
            }])
            df = pd.read_csv(CSV_FILE)
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv(CSV_FILE, index=False)
            st.success("✅ Enregistré !")

# Menu Liste
elif menu == "📋 Liste":
    st.title("Liste des joueurs")
    data = pd.read_csv(CSV_FILE)
    st.dataframe(data)

# Menu Stats
elif menu == "📊 Stats":
    st.title("Statistiques")
    data = pd.read_csv(CSV_FILE)
    if len(data) > 0:
        st.bar_chart(data["Buts"].value_counts())