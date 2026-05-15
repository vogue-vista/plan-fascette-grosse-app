import streamlit as st

st.set_page_config(page_title="Générateur de Fiches IA", page_icon="✍️", layout="centered")

if st.button("⬅️ Retour au Hub"):
    st.switch_page("app.py")

st.title("✍️ Générateur de Fiches Produits par IA")
st.write("Créez des descriptions marketing professionnelles en quelques secondes.")

nom_produit = st.text_input("Nom de l'article :", placeholder="Ex: Chaise de bureau ergonomique")
mots_cles = st.text_input("Mots-clés importants (séparés par des virgules) :", placeholder="Ex: confort, cuir, robuste, moderne")
ton = st.selectbox("Ton de la description :", ["Professionnel", "Vendeur / Persuasif", "Amusant", "Épuré / Luxe"])

if st.button("🪄 Générer le texte marketing"):
    if nom_produit:
        st.subheader("📝 Texte généré par l'IA :")
        # Structure de texte IA (plus tard connectée à l'API OpenAI)
        st.markdown(f"**Découvrez notre tout nouveau {nom_produit} !**")
        st.write(f"Conçu spécifiquement pour répondre à vos exigences de performance, cet article met en avant des caractéristiques uniques : {mots_cles}. Idéal pour booster vos ventes avec un positionnement {ton}.")
    else:
        st.error("Veuillez entrer au moins le nom d'un produit.")
