import streamlit as st

st.set_page_config(
    page_title="IEM-Consultoria",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.title('Convertidor de Estados de Cuenta PDF a Excel')
st.markdown("---")

# Python logo image

st.image("IEM_Logo.png", width=300)
st.text('Podrás fácilmente convertir los Estados de Cuenta de diferentes bancos a un archivo Excel (.csv) de manera rápida.')
