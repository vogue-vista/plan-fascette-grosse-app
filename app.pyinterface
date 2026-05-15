import streamlit as st

# 1. Configuration de la page du Hub Principal
st.set_page_config(
    page_title="Stark Enterprise Suite", 
    page_icon="🎛️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Style CSS personnalisé pour donner un look moderne aux tuiles (style Friv)
st.markdown("""
    <style>
    div.stButton > button:first-child {
        height: 120px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 15px;
        background-color: #1E1E1E;
        color: #FFFFFF;
        border: 2px solid #333333;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #FF4B4B;
        color: white;
        border-color: #FF4B4B;
        transform: translateY(-5px);
    }
    </style>
""", unsafe_allowed_html=True)

# 2. En-tête du tableau de bord B2B
st.title("🎛️ Tableau de Bord - Stark Enterprise Suite")
st.write("Bienvenue. Sélectionnez l'outil automatisé dont vous avez besoin pour votre entreprise.")
st.markdown("---")

# 3. Création de la grille d'applications (2 lignes x 3 colonnes)
row1_col1, row1_col2, row1_col3 = st.columns(3)
row2_col1, row2_col2, row2_col3 = st.columns(3)

# --- LIGNE 1 ---
with row1_col1:
    if st.button("🤖\n\nRobot Comparateur\nde Prix", use_container_width=True):
        st.switch_page("pages/1_🤖_Comparateur.py")

with row1_col2:
    if st.button("✍️\n\nGénérateur de\nFiches IA", use_container_width=True):
        st.switch_page("pages/2_✍️_Generateur_IA.py")

with row1_col3:
    if st.button("📊\n\nCalculateur de\nMarge & Profits", use_container_width=True):
        st.switch_page("pages/3_📊_Calculateur_Marge.py")

# --- LIGNE 2 (Outils en développement pour tes futures entreprises) ---
with row2_col1:
    if st.button("📈\n\nSuivi des Tendances\ne-Commerce", use_container_width=True):
        st.info("Cet outil est en cours de déploiement sur les serveurs.")

with row2_col2:
    if st.button("📦\n\nGestionnaire de\nStock Intelligent", use_container_width=True):
        st.info("Cet outil est en cours de déploiement sur les serveurs.")

with row2_col3:
    if st.button("💬\n\nSupport Client\nAutomatisé IA", use_container_width=True):
        st.info("Cet outil est en cours de déploiement sur les serveurs.")

st.markdown("---")
st.caption("Abonnement Professionnel B2B - Protégé par chiffrement local.")
