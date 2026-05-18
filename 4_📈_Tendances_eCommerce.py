import streamlit as st
import pandas as pd
import requests

st.title("📈 Suivi des Tendances e-Commerce")

st.write("Analyse automatique des tendances Google Shopping, Amazon et TikTok.")

mot_cle = st.text_input("Entrez un mot-clé produit :")

if st.button("Analyser la tendance"):
    if mot_cle.strip() == "":
        st.error("Veuillez entrer un mot-clé.")
    else:
        st.success(f"Tendance détectée pour : {mot_cle}")

        # Simulation de tendance
        tendance = {
            "Popularité Google": "⬆️ Forte hausse",
            "Popularité Amazon": "⬆️ En progression",
            "Popularité TikTok": "🔥 Produit viral"
        }

        st.subheader("📊 Résultats")
        st.json(tendance)

        st.line_chart(pd.DataFrame({
            "Popularité": [20, 40, 60, 80, 95],
            "Temps": [1, 2, 3, 4, 5]
        }))
