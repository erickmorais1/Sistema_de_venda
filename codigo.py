# Passo a passo do projeto
# Passo 1: Criar a tela do sistema
# Passo 2: Criar o formulário de cadastro
# Passo 3: Salvar a venda na base de dados
# Passo 4: Mostrar a base de dados na tela
# Passo 5: Criar o dashboard com os gráficos

import streamlit as st
import pandas as pd
import plotly.express as px

    # Titulo
st.write("# Sistema de Vendas")

    # Abrir base de dados
tabela_vendas = pd.read_csv("vendas.csv")

    # Criar o formulario de cadastro de vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data",max_value="today")
vendedor = st.sidebar.selectbox("Vendedor",["Ana Cristina","Erick","Cristiel"])
produto = st.sidebar.selectbox("Produto",["Notebook","Celular","Fone"])
quantidade = st.sidebar.number_input("Quantidade", step = 1)
valor = st.sidebar.number_input("Valor")
botao = st.sidebar.button("Cadastrar Venda")

    # Salvar venda na base de dados
if (botao):
    if(quantidade<=0.0) or (valor<=0.0):
                st.warning("Algo deu errado nos valores escolhidos")
    else:
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        tabela_vendas.loc[len(tabela_vendas)]=nova_venda #.loc para informar que vai add uma linha
        tabela_vendas.to_csv("vendas.csv",index=False)
        st.success("Venda Cadastrada!")
    

    # Mostrar a base de dados na tela
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

    # Criar o dashboard
st.write("## Dashboard")
soma = tabela_vendas["valor"].sum()
st.metric("Faturamento total",f"R${soma}")

    # Criar grafico de barra de vendas
grafico = px.bar(tabela_vendas,x="vendedor",y="valor",color="produto")
    # Mostrar grafico
st.plotly_chart(grafico)

    # Criar grafico de rosca de produtos
grafico2 = px.pie(tabela_vendas,names="produto",values="valor",hole=0.5)
    # Mostrar grafico
st.plotly_chart(grafico2)


