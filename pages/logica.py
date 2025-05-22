import streamlit as st

def logica():
   
   st.title("💡 Curso Básico de Lógica de Programação e Python")

   st.header("🧠 Introdução à Lógica de Programação")
   st.markdown("""
   Lógica de programação é a base de todo desenvolvimento de software. Ela permite que você:
   - Organize suas ideias
   - Resolva problemas de forma estruturada
   - Escreva algoritmos eficientes

   ### Conceitos principais:
   - **Variáveis**: armazenam valores.
   - **Condicionais**: tomam decisões (`if`, `else`).
   - **Laços de repetição**: executam ações repetidamente (`for`, `while`).
   - **Funções**: organizam blocos de código reutilizáveis.
   """)

   st.header("🐍 Introdução ao Python")
   st.markdown("Vamos aprender com exemplos simples:")

   # Explicações com exemplos comentados
   with st.expander("📌 Variáveis e Tipos de Dados"):
      st.code("""
   nome = "Maria"         # String
   idade = 20             # Int
   altura = 1.65          # Float
   tem_carteira = True    # Boolean
   print(nome, idade, altura, tem_carteira)
   """, language="python")

   with st.expander("📌 Condicionais"):
      st.code("""
   idade = 18
   if idade >= 18:
      print("Você é maior de idade.")
   else:
      print("Você é menor de idade.")
   """, language="python")

   with st.expander("📌 Laços de Repetição"):
      st.code("""
   for i in range(5):
      print("Repetição número", i)
   """, language="python")

      st.code("""
   contador = 0
   while contador < 3:
      print("Contando:", contador)
      contador += 1
   """, language="python")

   with st.expander("📌 Funções"):
      st.code("""
   def saudacao(nome):
      print("Olá", nome)

   saudacao("João")
   """, language="python")

   # ======================
   # EXERCÍCIOS INTERATIVOS
   # ======================

   st.header("🧪 Exercícios Interativos")

   # Exercício 1 - Variáveis
   st.subheader("Exercício 1 - Variáveis")
   res1 = st.text_input("Digite o tipo da variável: nome = 'Ana'")

   if res1:
      if res1.lower().strip() in ["string", "str", "texto"]:
         st.success("✅ Correto! 'Ana' é uma string.")
      else:
         st.error("❌ Tente novamente. Dica: está entre aspas.")

   # Exercício 2 - Condicionais
   st.subheader("Exercício 2 - Condicional simples")
   res2 = st.text_input("O que será exibido?\nidade = 15\nif idade >= 18:\n    print('Maior de idade')\nelse:\n    print('Menor de idade')")

   if res2:
      if "menor" in res2.lower():
         st.success("✅ Correto! A idade é 15, então entra no else.")
      else:
         st.error("❌ Tente novamente. A idade é menor que 18.")

   # Exercício 3 - Repetição
   st.subheader("Exercício 3 - Quantas vezes será exibido?\nfor i in range(3):\n    print(i)")
   res3 = st.text_input("Digite o número de vezes que será exibido:")

   if res3:
      if res3.strip() in ["3", "três", "tres"]:
         st.success("✅ Correto! O loop repete 3 vezes: i = 0, 1, 2.")
      else:
         st.error("❌ Lembre-se que o `range(3)` vai até 2.")

   # Exercício 4 - Função
   st.subheader("Exercício 4 - Função")
   res4 = st.text_input("Qual será a saída do código?\ndef ola():\n    print('Oi')\nola()")

   if res4:
      if "oi" in res4.lower():
         st.success("✅ Correto! A função `ola()` imprime 'Oi'.")
      else:
         st.error("❌ Tente novamente. Veja o que a função faz com `print`.")

   # Encerramento motivacional
   st.success("🚀 Muito bem! Continue praticando para se tornar um programador cada vez melhor!")
   if st.button("👉 Ir para próxima etapa: Curso: Lógica de Programação"):
      st.session_state.page = "infra"