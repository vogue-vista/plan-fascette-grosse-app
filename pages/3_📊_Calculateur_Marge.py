import streamlit as st

# 1. INITIALISATION DE LA SÉCURITÉ GLOBALE (Obligatoire avant tout affichage)
if "connecte" not in st.session_state or not st.session_state.connecte:
    st.error("⚠️ Accès refusé. Veuillez vous abonner et vous connecter sur la page d'accueil.")
    if st.button("⬅️ Aller à la page de paiement"):
        st.switch_page("app.py")
    st.stop() # Bloque définitivement l'exécution du reste du code

# 2. CONFIGURATION DE LA PAGE (S'exécute uniquement si l'utilisateur est connecté)
st.set_page_config(page_title="Calculateur de Marge", page_icon="📊", layout="centered")

# Bouton de retour au Hub Friv
if st.button("⬅️ Retour au Hub Principal"):
    st.switch_page("app.py")

st.title("📊 Calculateur de Marges & Bénéfices")
st.write("Vérifiez la viabilité financière de vos produits e-commerce.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    cout_achat = st.number_input("Coût d'achat ou de fabrication ($) :", min_value=0.0, value=10.0)
    frais_expedition = st.number_input("Frais de livraison et logistique ($) :", min_value=0.0, value=5.0)

with col2:
    prix_vente = st.number_input("Prix de vente final au client ($) :", min_value=0.0, value=30.0)

# Calculs logiques en Python
cout_total = cout_achat + frais_expedition
profit_brut = prix_vente - cout_total

if prix_vente > 0:
    marge_pourcentage = (profit_brut / prix_vente) * 100
else:
    marge_pourcentage = 0.0

st.subheader("📈 Résultats de rentabilité :")

res_col1, res_col2 = st.columns(2)
with res_col1:
    st.metric(label="Profit Net par Vente", value=f"{profit_brut:.2f} $")
with res_col2:
    st.metric(label="Marge Bénéficiaire", value=f"{marge_pourcentage:.1f} %")

if marge_pourcentage >= 30:
    st.success("🔥 Ce produit est hautement rentable pour votre entreprise !")
elif 0 < marge_pourcentage < 30:
    st.warning("⚠️ Attention, la marge est correcte mais le profit reste faible après taxes.")
else:
    st.error("❌ Ce produit se vend à perte. Ajustez vos coûts ou augmentez le prix de vente.")

