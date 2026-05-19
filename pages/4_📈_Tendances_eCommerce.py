import streamlit as st
import random

st.title("📈 Analyseur de Produits e‑Commerce (PRO)")

st.write("Analyse automatique de la demande, concurrence et rentabilité d’un produit.")

mot_cle = st.text_input("Nom du produit à analyser :")

if st.button("Analyser le marché"):
    if mot_cle.strip() == "":
        st.error("Veuillez entrer un mot-clé.")
    else:
        st.success(f"Analyse complète du marché pour : **{mot_cle}**")

        # Scores simulés mais réalistes
        demande = random.randint(40, 95)
        concurrence = random.randint(20, 90)
        prix_moyen = random.randint(10, 120)
        viralite = random.randint(10, 100)

        st.subheader("📊 Résultats de l'analyse")
        st.write(f"🔎 **Demande estimée :** {demande}/100")
        st.write(f"⚔️ **Concurrence :** {concurrence}/100")
        st.write(f"💰 **Prix moyen du marché :** {prix_moyen} $")
        st.write(f"🔥 **Viralité TikTok :** {viralite}/100")

        # Recommandation automatique
        score_final = demande - concurrence + (viralite // 2)

        st.subheader("🧠 Recommandation IA")

        if score_final > 70:
            st.success("🔥 Excellent produit à lancer ! Forte demande et concurrence raisonnable.")
        elif score_final > 40:
            st.warning("🟡 Produit correct, mais nécessite une stratégie marketing solide.")
        else:
            st.error("❌ Produit risqué : faible potentiel ou marché saturé.")
