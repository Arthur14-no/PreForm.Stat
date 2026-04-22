import streamlit as st
import pandas as pd
from datetime import datetime, date
import os

DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR, "joueurs.csv")

st.title(" Ajouter un nouveau joueur")
st.markdown("Remplissez tous les champs ci-dessous pour enregistrer un joueur.")

with st.form("player_form", clear_on_submit=True):
    st.markdown("###  Informations personnelles")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nom = st.text_input("Nom complet *", placeholder="Ex: Vincent Aboubakar")
        date_naissance = st.date_input("Date de naissance *", min_value=date(1980, 1, 1), max_value=date.today())
        poste = st.selectbox("Poste *", [
            "Gardien", "Défenseur central", "Latéral droit", "Latéral gauche",
            "Milieu défensif", "Milieu relayeur", "Milieu offensif", "Ailier droit",
            "Ailier gauche", "Attaquant", "Avant-centre"
        ])
    
    with col2:
        numero = st.number_input("Numéro de maillot", min_value=1, max_value=99, step=1)
        pied_fort = st.selectbox("Pied fort", ["Droit", "Gauche", "Les deux"])
        nationalite = st.text_input("Nationalité", placeholder="Ex: Camerounaise")
    
    st.markdown("###  Caractéristiques physiques")
    
    col3, col4 = st.columns(2)
    with col3:
        taille = st.number_input("Taille (cm)", min_value=140, max_value=230, step=1)
    with col4:
        poids = st.number_input("Poids (kg)", min_value=40, max_value=150, step=1)
    
    st.markdown("### ⚽ Performances (cette saison)")
    
    col5, col6, col7 = st.columns(3)
    with col5:
        matchs = st.number_input("Matchs joués", min_value=0, step=1)
        buts = st.number_input("Buts", min_value=0, step=1)
    with col6:
        passes = st.number_input("Passes décisives", min_value=0, step=1)
        note = st.slider("Note moyenne sur 10", 0.0, 10.0, 5.0, 0.5)
    with col7:
        minutes = st.number_input("Minutes jouées", min_value=0, step=1)
    
    st.markdown("###  Autres")
    commentaires = st.text_area("Commentaires du coach", placeholder="Points forts, axes d'amélioration, remarques...", height=100)
    
    st.markdown("---")
    submitted = st.form_submit_button(" Enregistrer le joueur", use_container_width=True)
    
    if submitted:
        if not nom:
            st.error(" Le nom du joueur est obligatoire !")
        else:
            # Calcul de l'âge
            today = date.today()
            age = today.year - date_naissance.year - ((today.month, today.day) < (date_naissance.month, date_naissance.day))
            
            new_data = pd.DataFrame([{
                "Date_saisie": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Nom": nom,
                "Date_naissance": date_naissance.strftime("%Y-%m-%d"),
                "Age": age,
                "Poste": poste,
                "Numero_maillot": numero,
                "Pied_fort": pied_fort,
                "Taille_cm": taille,
                "Poids_kg": poids,
                "Nationalite": nationalite,
                "Matchs_joues": matchs,
                "Buts": buts,
                "Passes_decisives": passes,
                "Note_moyenne": note,
                "Minutes_jouees": minutes,
                "Commentaires": commentaires
            }])
            
            existing_data = pd.read_csv(CSV_FILE)
            updated_data = pd.concat([existing_data, new_data], ignore_index=True)
            updated_data.to_csv(CSV_FILE, index=False)
            
            st.success(f"✅ {nom} a été enregistré avec succès !")
            st.balloons()