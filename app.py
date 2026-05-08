import streamlit as st

# Configuration de la page pour le TNI
st.set_page_config(page_title="Denise-Dojo", layout="wide")

st.title("🍎 Le Tableau de Denise - 5e Année")

# Liste de tes élèves
if 'eleves' not in st.session_state:
    st.session_state.eleves = {
        "Sam": 0, "Laurence": 0, "Khloé": 0, "Nizar": 0, "Maélie": 0,
        "Félicia": 0, "Brayan": 0, "Émy-Rose": 0, "Soli": 0, "Arielle": 0,
        "Abel": 0, "Kenza": 0, "Mélodie": 0, "Maxim": 0, "Sofia": 0,
        "Suzanne": 0, "Jayke": 0, "Nathan": 0, "Maély": 0
    }

# Affichage sous forme de colonnes (4 par ligne pour le TNI)
cols = st.columns(4)

for i, (nom, points) in enumerate(st.session_state.eleves.items()):
    with cols[i % 4]:
        st.subheader(f"{nom}")
        st.write(f"Points : **{points}**")
        
        # Boutons côte à côte
        btn_col1, btn_col2 = st.columns(2)
        if btn_col1.button(f"➕", key=f"add_{nom}"):
            st.session_state.eleves[nom] += 1
            st.rerun()
        if btn_col2.button(f"➖", key=f"sub_{nom}"):
            st.session_state.eleves[nom] -= 1
            st.rerun()
        
        # Option récompense (ex: 10 points)
        if points >= 10:
            if st.button(f"🎁 Récompense", key=f"gift_{nom}"):
                st.session_state.eleves[nom] -= 10
                st.success(f"Bravo {nom} !")
                st.rerun()

st.divider()
if st.button("Réinitialiser tous les points"):
    for nom in st.session_state.eleves:
        st.session_state.eleves[nom] = 0
    st.rerun()
