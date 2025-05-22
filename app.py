import streamlit as st
from pages.login import login
from pages.logica import logica
from pages.infra import infra
from pages.segurança import segurança
from pages.prova import prova

st.set_page_config(page_title="Curso Completo", page_icon="📚" , layout="wide", initial_sidebar_state="collapsed")

# Inicializa a página padrão
if "page" not in st.session_state:
    st.session_state.page = "login"

# Navegação entre páginas via session_state["page"]
if st.session_state.page == "login":
    login()
elif st.session_state.page == "logica":
    logica()
elif st.session_state.page == "infra":
    infra()
elif st.session_state.page == "segurança":
    segurança()
elif st.session_state.page == "prova":
    prova()
