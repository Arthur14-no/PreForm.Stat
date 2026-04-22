import streamlit as st
import pandas as pd
import os
import plotly.express as px

DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR, "joueurs.csv")

st.title(" Tableau de bord statistique")
st.markdown("Visualisez les performances et caractéristiques de votre effectif.")

if os.path.exists(CSV_FILE):
    data = pd.read_csv(CSV_FILE)
else:
    data = pd.DataFrame()

if len(data) == 0:
    st.info(" Pas assez de données pour afficher des statistiques. Ajoutez d'abord des joueurs.")
else:
    # Indicateurs clés
    st.markdown("###  Indicateurs clés")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🏃 Total joueurs", len(data))
    with col2:
        st.metric(" Total buts", data["Buts"].sum())
    with col3:
        st.metric(" Total passes décisives", data["Passes_decisives"].sum())
    with col4:
        st.metric(" Note moyenne", round(data["Note_moyenne"].mean(), 1))
    
    st.markdown("---")
    
    # Graphiques
    col5, col6 = st.columns(2)
    
    with col5:
        st.markdown("####  Meilleurs buteurs")
        top_buts = data.nlargest(5, "Buts")[["Nom", "Buts"]]
        st.bar_chart(top_buts.set_index("Nom"))
    
    with col6:
        st.markdown("####  Meilleurs passeurs")
        top_passes = data.nlargest(5, "Passes_decisives")[["Nom", "Passes_decisives"]]
        st.bar_chart(top_passes.set_index("Nom"))
    
    # Répartition par poste
    st.markdown("####  Répartition par poste")
    poste_counts = data["Poste"].value_counts()
    fig_poste = px.pie(values=poste_counts.values, names=poste_counts.index, title="Effectif par poste")
    st.plotly_chart(fig_poste, use_container_width=True)
    
    # Note moyenne par poste
    st.markdown("####  Note moyenne par poste")
    note_poste = data.groupby("Poste")["Note_moyenne"].mean().sort_values(ascending=False)
    st.bar_chart(note_poste)
    
    # Âge moyen par poste
    st.markdown("####  Âge moyen par poste")
    age_poste = data.groupby("Poste")["Age"].mean().sort_values(ascending=False)
    st.bar_chart(age_poste)
    
    # Taille vs Poids
    st.markdown("####  Relation Taille vs Poids")
    fig_scatter = px.scatter(data, x="Taille_cm", y="Poids_kg", color="Poste", hover_name="Nom", title="Taille et poids des joueurs")
    st.plotly_chart(fig_scatter, use_container_width=True)