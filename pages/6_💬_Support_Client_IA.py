import streamlit as st
import random

st.title("💬 Support Client Automatisé IA")

st.write("Répondez automatiquement aux clients grâce à une IA simple et rapide.")

question = st.text_area("Message du client :")

reponses = [
    "Merci pour votre message ! Nous regardons cela immédiatement.",
    "Nous sommes désolés pour l’inconvénient. Nous revenons vers vous sous peu.",
    "Bonne nouvelle ! Votre demande est en cours de traitement.",
    "Merci pour votre patience, nous faisons le nécessaire."
]

if st.button("Générer une réponse IA"):
    if question.strip() == "":
        st.error("Veuillez entrer un message client.")
    else:
        st.success("Réponse générée :")
        st.info(random.choice(reponses))
