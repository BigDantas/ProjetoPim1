import streamlit as st

def infra():

    
    st.title("🧠 Fundamentos de Hardware e Software")

    st.header("🔍 O que é Hardware?")
    st.markdown("""
    **Hardware** é a parte **física** do computador, ou seja, tudo aquilo que você pode **ver e tocar**.

    ### Exemplos:
    - **Processador (CPU)**: responsável por executar comandos e cálculos.
    - **Memória RAM**: armazena temporariamente dados usados no momento.
    - **HD/SSD**: armazena os dados permanentemente (fotos, documentos, programas).
    - **Placa-mãe**: conecta todos os componentes entre si.
    - **Periféricos**: teclado, mouse, monitor, impressora, etc.

    > 💡 O hardware **sem o software** é como um corpo sem mente: está presente, mas não pode agir por conta própria.
    """)

    st.header("💾 O que é Software?")
    st.markdown("""
    **Software** é a parte **lógica e invisível** do computador. São os programas, sistemas e instruções que dizem ao hardware **o que fazer**.

    ### Tipos principais de software:

    #### 1. **Sistema Operacional (SO)**
    - Controla o hardware e permite a execução de programas.
    - Exemplos: Windows, Linux, macOS, Android.

    #### 2. **Aplicativos**
    - São programas que usamos para tarefas específicas.
    - Exemplos: navegador (Chrome), editor de texto (Word), jogos.

    #### 3. **Drivers**
    - São softwares que fazem a ponte entre o sistema operacional e o hardware.
    - Exemplo: driver de vídeo que permite o uso da placa gráfica corretamente.

    > 💡 O software depende do hardware para funcionar. É como o cérebro enviando comandos para o corpo.
    """)

    st.header("🔁 Como Hardware e Software trabalham juntos?")
    st.markdown("""
    O computador funciona corretamente quando **hardware e software atuam em conjunto**:

    - O usuário **dá um comando** (ex: clicar em um botão).
    - O **software interpreta** esse comando.
    - O **hardware executa** a ação (ex: mostrar uma imagem, reproduzir um som).
    """)

    st.header("🧱 Classificação do Hardware")
    st.markdown("""
    ### 1. **Hardware de Entrada**
    - Permite enviar dados para o computador.
    - Exemplos: teclado, mouse, microfone, scanner.

    ### 2. **Hardware de Saída**
    - Exibe os resultados para o usuário.
    - Exemplos: monitor, impressora, caixas de som.

    ### 3. **Hardware de Processamento**
    - Realiza o trabalho "por trás dos panos".
    - Exemplos: processador (CPU), placa de vídeo (GPU), memória RAM.

    ### 4. **Hardware de Armazenamento**
    - Guarda os dados de forma temporária ou permanente.
    - Exemplos: HD, SSD, pen drive, cartão de memória.
    """)

    st.header("📊 Diferença entre Hardware e Software")
    st.markdown("""
    | Característica       | Hardware                         | Software                           |
    |----------------------|----------------------------------|-------------------------------------|
    | Natureza             | Físico, palpável                 | Lógico, digital                     |
    | Exemplos             | CPU, teclado, HD, monitor        | Windows, Word, Chrome, antivírus    |
    | Substituição         | Mais difícil e caro              | Mais fácil e rápido                 |
    | Danos                | Sofre desgaste físico            | Sofre falhas lógicas ou bugs        |
    """)

    st.header("📘 Conclusão")
    st.markdown("""
    Entender os conceitos de **hardware e software** é essencial para qualquer pessoa que deseja iniciar na área da tecnologia.

    - O **hardware** fornece a estrutura e a capacidade de executar tarefas.
    - O **software** dá as ordens, processa dados e oferece as funções que utilizamos no dia a dia.

    > 💡 Pense no computador como um corpo (hardware) com uma mente (software). Um depende do outro para funcionar bem.
    """)

    st.success("🚀 Continue explorando o mundo da tecnologia e você dominará cada peça desse quebra-cabeça digital!")
    if st.button("👉 Ir para próxima etapa: Curso: Lógica de Programação"):
        st.session_state.page = "segurança"