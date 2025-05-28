import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:\Projetos\Python\Data\AnaliseDePadaria\dados\clientes_padaria.csv')

#APP STREAMLIT
st.title('Projeto Simples de Análise de Dados de uma Padaria fictícia')

#Grafico da media e estatisticas descritivas - Media
st.write(f"Média da frequencia de compras dos produtos da padaria: ")
statics1 = df.groupby('Produto_Preferido')['Frequência_Compra'].agg(['mean', 'std', 'count'])
plt.bar(statics1.index, statics1['mean']) #grafico de barras
plt.xlabel('Produto Preferido')
plt.ylabel('Frequencia Media da Compra (vezes/semana)')
plt.title('Frequencia Media de Compra por Produto')
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(plt.gcf())
plt.clf()

st.write('-------------------------------------------------')

st.write('Gasto médio por faixa etária dos clientes da padaria')
faixas = [18, 25, 35, 45, 55, 65, 80]
labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']
df['Faixa_Etária'] = pd.cut(df['Idade'], bins=faixas, labels=labels, include_lowest=True)
gasto_p_idade = df.groupby('Faixa_Etária')['Gasto_Médio'].agg(['mean', 'std', 'count'])

dados_boxplot = [df[df['Faixa_Etária'] == faixas]['Gasto_Médio'] for faixas in labels]

plt.boxplot(dados_boxplot, labels=labels)
plt.xlabel('Faixa Etária')
plt.ylabel('Gasto Médio (R$)')
plt.title('Gasto Médio por Faixa Etária')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt.gcf())
plt.clf()
