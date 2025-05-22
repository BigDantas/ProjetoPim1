import streamlit as st

def segurança():

    # Título principal
    st.title("🔐 Introdução à Cibersegurança e LGPD")

    # Seção 1 - Conceito de Cibersegurança
    st.header("🛡️ O que é Cibersegurança?")
    st.markdown("""
    Cibersegurança é o conjunto de práticas, tecnologias e processos usados para proteger sistemas, redes, programas e dados contra ataques digitais.

    Esses ataques podem ter diferentes objetivos, como roubo de dados, espionagem ou até paralisação de sistemas.

    ### Principais ameaças:
    - **Phishing**: tentativas de enganar o usuário para roubar informações.
    - **Malware**: programas maliciosos como vírus, ransomware e spyware.
    - **Ataques DDoS**: sobrecarregam servidores para tirá-los do ar.
    - **Roubo de credenciais**: obtenção de senhas e dados pessoais.

    > ⚠️ A segurança digital começa com pequenos cuidados: senhas fortes, backups e desconfiança de links suspeitos.
    """)

    # Seção 2 - Boas práticas de segurança
    st.header("🔐 Boas práticas de segurança digital")
    st.markdown("""
    Aqui estão algumas atitudes simples que ajudam a manter a segurança dos seus dados:

    - Use **senhas longas e diferentes** para cada site.
    - Ative a **autenticação em duas etapas**.
    - Não clique em links de e-mails ou mensagens suspeitas.
    - Faça **backup** dos seus arquivos com frequência.
    - Instale um bom **antivírus** e mantenha o sistema atualizado.
    """)

    # Seção 3 - Introdução à LGPD
    st.header("📜 O que é a LGPD?")
    st.markdown("""
    A **LGPD (Lei Geral de Proteção de Dados)** é a lei brasileira que regula o uso, coleta e tratamento de **dados pessoais**.  

    Entrou em vigor em **setembro de 2020** e obriga empresas e órgãos públicos a protegerem a privacidade dos cidadãos.

    ### O que são dados pessoais?
    São informações que permitem identificar uma pessoa, como:
    - Nome, CPF, RG
    - E-mail, telefone, endereço
    - Localização, IP, hábitos de consumo

    ### Princípios da LGPD:
    - **Transparência**: o usuário deve saber como seus dados serão usados.
    - **Finalidade**: os dados só podem ser coletados para um objetivo específico.
    - **Consentimento**: o usuário deve autorizar o uso dos dados.
    - **Segurança**: a empresa deve proteger os dados contra vazamentos.

    > 🧠 A LGPD protege os seus dados e dá a você o controle sobre como eles são utilizados.
    """)

    # Seção 4 - Relação entre Cibersegurança e LGPD
    st.header("🔗 Qual a relação entre Cibersegurança e LGPD?")
    st.markdown("""
    A cibersegurança é **fundamental para cumprir a LGPD**.  

    Sem medidas de proteção digital, os dados podem vazar ou ser acessados indevidamente, o que gera **multas e danos à imagem** da empresa.

    Por isso, proteger informações com antivírus, criptografia, firewalls e backups é parte essencial da **responsabilidade legal com os dados pessoais**.
    """)

    # Conclusão com destaque
    st.header("✅ Conclusão")
    st.markdown("""
    Tanto a **cibersegurança** quanto a **LGPD** são temas essenciais na era digital.  
    Elas trabalham juntas para garantir **privacidade, integridade e segurança** dos dados pessoais e corporativos.

    > 💡 Estar informado e aplicar boas práticas protege você e ajuda a construir um ambiente digital mais seguro para todos.
    """)

    # Dica final
    st.success("🔒 Dica: Estude também engenharia social, criptografia, políticas de privacidade e como identificar golpes virtuais!")
    if st.button("👉 Ir para próxima etapa: Curso: Lógica de Programação"):
        st.session_state.page = "prova"