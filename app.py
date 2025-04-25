import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Python em 5 Minutos",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Python em 5 Minutos")
st.subheader("Mini-desafio interativo para iniciantes")

# Desafio 1: Calculadora Simples
st.header("Desafio 1: Calculadora Simples")
st.write("Vamos criar uma calculadora simples! Digite dois números e escolha a operação.")

col1, col2, col3 = st.columns(3)

with col1:
    num1 = st.number_input("Primeiro número", value=0)
with col2:
    operacao = st.selectbox("Operação", ["+", "-", "*", "/"])
with col3:
    num2 = st.number_input("Segundo número", value=0)

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
else:
    resultado = num1 / num2 if num2 != 0 else "Erro: Divisão por zero!"

st.write(f"Resultado: {resultado}")

# Desafio 2: Lista de Compras
st.header("Desafio 2: Lista de Compras")
st.write("Vamos criar uma lista de compras interativa!")

item = st.text_input("Digite um item para adicionar à lista")
if st.button("Adicionar Item"):
    if 'lista_compras' not in st.session_state:
        st.session_state.lista_compras = []
    st.session_state.lista_compras.append(item)
    st.success(f"Item '{item}' adicionado!")

if 'lista_compras' in st.session_state:
    st.write("Sua lista de compras:")
    for i, item in enumerate(st.session_state.lista_compras, 1):
        st.write(f"{i}. {item}")

# Desafio 3: Jogo de Adivinhação
st.header("Desafio 3: Jogo de Adivinhação")
st.write("Tente adivinhar o número entre 1 e 100!")

if 'numero_secreto' not in st.session_state:
    st.session_state.numero_secreto = np.random.randint(1, 101)

palpite = st.number_input("Digite seu palpite", min_value=1, max_value=100, value=50)

if st.button("Verificar Palpite"):
    if palpite == st.session_state.numero_secreto:
        st.success("Parabéns! Você acertou!")
        st.session_state.numero_secreto = np.random.randint(1, 101)
    elif palpite < st.session_state.numero_secreto:
        st.warning("Tente um número maior!")
    else:
        st.warning("Tente um número menor!")

# Rodapé
st.markdown("---")
st.markdown("Criado com ❤️ para iniciantes em Python") 