import streamlit as st
import json
import bcrypt
import os
def login():
    # Caminho do arquivo onde os usuários são salvos
    USERS_FILE = "users.json"

    # Função para carregar os usuários do arquivo JSON
    def load_users():
        if not os.path.exists(USERS_FILE):
            return {}
        with open(USERS_FILE, "r") as f:
            return json.load(f)

    # Função para salvar os usuários no arquivo JSON
    def save_users(users):
        with open(USERS_FILE, "w") as f:
            json.dump(users, f)

    # Função para registrar novo usuário
    def register_user(username, password):
        users = load_users()
        if username in users:
            return False  # Usuário já existe
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        users[username] = hashed_pw
        save_users(users)
        return True

    # Função para verificar login
    def login_user(username, password):
        users = load_users()
        if username not in users:
            return False
        hashed_pw = users[username].encode()
        return bcrypt.checkpw(password.encode(), hashed_pw)

    # Interface Streamlit
    
    st.title("🔐 Sistema de Login")

    menu = st.selectbox("Escolha uma opção", ["Login", "Registrar"])

    if menu == "Login":
        st.subheader("Acessar Conta")
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if login_user(username, password):
                st.success(f"Bem-vindo, {username}!")
            else:
                st.error("Usuário ou senha inválidos.")

    elif menu == "Registrar":
        st.subheader("Criar Conta")
        new_user = st.text_input("Novo Usuário")
        new_pass = st.text_input("Nova Senha", type="password")
        if st.button("Registrar"):
            if register_user(new_user, new_pass):
                st.success("Usuário registrado com sucesso!")
            else:
                st.warning("Usuário já existe.")
    if st.button("👉 Ir para próxima etapa: Curso: Lógica de Programação"):
        st.session_state.page = "logica"