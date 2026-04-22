import streamlit as st
import pandas as pd
import os

DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR, "joueurs.csv")

st.title(" Liste des joueurs")
st.markdown("Consultez, filtrez et exportez les données des joueurs.")

# Chargement des données
if os.path.exists(CSV_FILE):
    data = pd.read_csv(CSV_FILE)
else:
    data = pd.DataFrame()

if len(data) == 0:
    st.info(" Aucun joueur enregistré pour le moment. Allez dans 'Ajouter un joueur' pour commencer.")
else:
    # Filtres
    st.markdown("###  Filtres")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        poste_filter = st.multiselect("Filtrer par poste", options=data["Poste"].unique())
    with col2:
        pied_filter = st.multiselect("Filtrer par pied fort", options=data["Pied_fort"].unique())
    with col3:
        search = st.text_input("Rechercher un joueur", placeholder="Nom...")
    
    # Application des filtres
    filtered_data = data.copy()
    if poste_filter:
        filtered_data = filtered_data[filtered_data["Poste"].isin(poste_filter)]
    if pied_filter:
        filtered_data = filtered_data[filtered_data["Pied_fort"].isin(pied_filter)]
    if search:
        filtered_data = filtered_data[filtered_data["Nom"].str.contains(search, case=False)]
    
    st.markdown(f"###  {len(filtered_data)} joueur(s) trouvé(s)")
    
    # Affichage du tableau
    st.dataframe(filtered_data, use_container_width=True)
    
    # Export
    st.markdown("###  Export des données")
    csv_export = filtered_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=" Télécharger en CSV",
        data=csv_export,
        file_name="joueurs_preformstat.csv",
        mime="text/csv"
    )