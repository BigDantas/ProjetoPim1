import streamlit as st

def prova():

    # Título da prova
    st.title("📝 Mini Prova de Conhecimentos Básicos em TI")

    # Explicação inicial
    st.markdown("""
    Essa prova cobre os seguintes temas:

    - Lógica de Programação e Python Básico  
    - Infraestrutura Computacional (Hardware e Software)  
    - Cibersegurança e LGPD  

    Responda às questões com atenção. Sua nota será calculada ao final!
    """)

    # Variável para armazenar a pontuação do usuário
    score = 0

    # Questão 1 - Lógica de Programação
    st.subheader("1. O que é um algoritmo?")
    q1 = st.radio(
        "Selecione a alternativa correta:",
        [
            "Um tipo de software que faz cálculos matemáticos.",
            "Um conjunto de instruções organizadas para resolver um problema.",
            "Um hardware específico usado em programação.",
            "Uma linguagem de programação."
        ],
        key="q1"
    )
    if q1 == "Um conjunto de instruções organizadas para resolver um problema.":
        score += 1

    # Questão 2 - Python Básico
    st.subheader("2. Em Python, o que a função 'print()' faz?")
    q2 = st.radio(
        "Escolha a alternativa correta:",
        [
            "Recebe dados digitados pelo usuário.",
            "Finaliza o programa.",
            "Imprime valores na tela.",
            "Declara uma variável."
        ],
        key="q2"
    )
    if q2 == "Imprime valores na tela.":
        score += 1

    # Questão 3 - Infraestrutura
    st.subheader("3. Qual das opções abaixo é um exemplo de hardware de entrada?")
    q3 = st.radio(
        "Escolha a alternativa correta:",
        [
            "Monitor",
            "Teclado",
            "Impressora",
            "Alto-falante"
        ],
        key="q3"
    )
    if q3 == "Teclado":
        score += 1

    # Questão 4 - Hardware x Software
    st.subheader("4. Qual a principal diferença entre hardware e software?")
    q4 = st.radio(
        "Escolha a alternativa correta:",
        [
            "Hardware é visível e físico, enquanto software é lógico e invisível.",
            "Software é mais caro que hardware.",
            "Hardware é opcional, software é obrigatório.",
            "Software funciona sozinho, sem precisar de hardware."
        ],
        key="q4"
    )
    if q4 == "Hardware é visível e físico, enquanto software é lógico e invisível.":
        score += 1

    # Questão 5 - Cibersegurança
    st.subheader("5. Qual das alternativas abaixo é uma boa prática de segurança digital?")
    q5 = st.radio(
        "Escolha a alternativa correta:",
        [
            "Usar a mesma senha para todos os sites.",
            "Compartilhar sua senha com pessoas de confiança.",
            "Manter o sistema desatualizado para evitar erros.",
            "Ativar autenticação em duas etapas sempre que possível."
        ],
        key="q5"
    )
    if q5 == "Ativar autenticação em duas etapas sempre que possível.":
        score += 1

    # Questão 6 - LGPD
    st.subheader("6. De acordo com a LGPD, o que são considerados dados pessoais?")
    q6 = st.radio(
        "Escolha a alternativa correta:",
        [
            "Somente número de CPF e RG.",
            "Informações genéricas de internet.",
            "Dados que identificam uma pessoa, como nome, telefone e endereço.",
            "Arquivos de empresas e organizações públicas."
        ],
        key="q6"
    )
    if q6 == "Dados que identificam uma pessoa, como nome, telefone e endereço.":
        score += 1

    # Quando o botão for pressionado, calcula a nota
    if st.button("Ver resultado"):
        nota_final = (score / 6) * 10  # Escala de 0 a 10
        st.success(f"🎉 Parabéns! Sua nota final é: **{nota_final:.1f}/10**")

        # Mensagem de acordo com o desempenho
        if nota_final == 10:
            st.balloons()
            st.info("Você acertou tudo! Excelente trabalho!")
        elif nota_final >= 7:
            st.info("Muito bem! Você dominou boa parte do conteúdo.")
        elif nota_final >= 5:
            st.warning("Você teve um desempenho razoável. Que tal revisar um pouco?")
        else:
            st.error("Você acertou poucas questões. Revise os conteúdos e tente novamente!")

        # Agradecimento
        st.markdown("---")
        st.markdown("🙏 Obrigado por participar da mini prova! Continue estudando e evoluindo no mundo da tecnologia.")
