import streamlit as st
import pandas as pd
import numpy as np
import time

st.write("Bonjour !")
st.title("Bienvenue sur :red[streamlit]")
st.header(':blue[Nous vous aidons à analyser vos données]')
st.subheader("Tableau de bord")
st.text("Analyse des données")

# Affichage de l'uploader dans l'application Streamlit
file = st.file_uploader("Importer vos données ici", type=["csv"])

# Vérification si un fichier a été téléchargé
if file is not None:
    # Traitement du fichier téléchargé  et affichage
    df = pd.read_csv(file)
    # Simuler une tâche en cours
    progress_bar = st.progress(0)

    for i in range(100):
        # Mise à jour de la barre de progression
        progress_bar.progress(i + 1)

        # Simuler une pause pour représenter une tâche en cours
        time.sleep(0.1)

    # Fin de la tâche
    st.success('Tâche terminée!')
    st.dataframe(df)

    # Affichage du graphique en ligne avec st.line_chart
    st.line_chart(df)
    # Affichage du graphique à barres avec st.bar_chart
    st.bar_chart(df)
    # # Création d'un graphique à barres avec Plotly Express
    # fig = px.bar(df, title='Graphique à Barres avec Plotly Express')

    # # Affichage du graphique avec st.plotly_chart
    # st.plotly_chart(fig)


