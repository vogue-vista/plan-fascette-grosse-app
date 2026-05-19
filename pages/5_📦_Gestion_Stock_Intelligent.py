import streamlit as st
import pandas as pd

st.title("📦 Gestionnaire de Stock Intelligent")

st.write("Ajoutez, suivez et optimisez vos stocks automatiquement.")

if "stock" not in st.session_state:
    st.session_state.stock = pd.DataFrame(columns=["Produit", "Quantité", "Seuil"])

st.subheader("➕ Ajouter un produit")
nom = st.text_input("Nom du produit")
quantite = st.number_input("Quantité", min_value=0)
seuil = st.number_input("Seuil d’alerte", min_value=0)

if st.button("Ajouter au stock"):
    st.session_state.stock.loc[len(st.session_state.stock)] = [nom, quantite, seuil]
    st.success("Produit ajouté !")

st.subheader("📋 Stock actuel")
st.dataframe(st.session_state.stock)

st.subheader("⚠️ Alertes automatiques")
alertes = st.session_state.stock[st.session_state.stock["Quantité"] <= st.session_state.stock["Seuil"]]

if len(alertes) > 0:
    st.error("Certains produits nécessitent un réapprovisionnement :")
    st.dataframe(alertes)
else:
    st.success("Aucune alerte pour le moment.")
