import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Análise de previsão de renda",
     page_icon="https://e7.pngegg.com/pngimages/998/957/png-clipart-black-dollar-sign-illustration-dollar-sign-united-states-dollar-icon-currency-symbol-dollar-sign-number-dollar-thumbnail.png",
     layout="wide",
)

st.write('# Análise exploratória da previsão de renda')

renda = pd.read_csv('C:\\Users\\Desktop\\Desktop\\Licao EBAC\\M_16\\original\\projeto 2\\input\\New folder\\previsao_de_renda.csv')

#plots
st.write('<h2 style="font-size:30px;"> Ut </h2>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
renda[['posse_de_imovel', 'renda']].plot(kind='hist', ax=ax)
st.pyplot(fig)
st.markdown('---')

# Gráfico 2
st.markdown('<h2 style="font-size:30px;">* Gráfico de linha por posse de imóvel</h2>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='data_ref', y='renda', hue='posse_de_imovel', data=renda, ax=ax)
ax.tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(fig)
st.markdown('---')

# Gráfico 3
st.markdown('<h2 style="font-size:30px;">* Gráfico de linha por posse de veículo</h2>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='data_ref', y='renda', hue='posse_de_veiculo', data=renda, ax=ax)
ax.tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(fig)
st.markdown('---')

# Gráfico 4
st.markdown('<h2 style="font-size:30px;">* Gráfico de linha por quantidade de filhos</h2>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='data_ref', y='renda', hue='qtd_filhos', data=renda, ax=ax)
ax.tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(fig)
st.markdown('---')

# Gráfico 5
st.markdown('<h2 style="font-size:30px;">* Gráfico de linha por tipo de renda</h2>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='data_ref', y='renda', hue='tipo_renda', data=renda, ax=ax)
ax.tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(fig)
st.markdown('---')

# Gráfico 6
st.markdown('<h2 style="font-size:30px;">* Gráfico de linha por educação</h2>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='data_ref', y='renda', hue='educacao', data=renda, ax=ax)
ax.tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(fig)
st.markdown('---')

# Gráfico 7
st.markdown('<h2 style="font-size:30px;">* Gráfico de linha por estado civil</h2>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='data_ref', y='renda', hue='estado_civil', data=renda, ax=ax)
ax.tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(fig)
st.markdown('---')

# Gráfico 8
st.markdown('<h2 style="font-size:30px;">* Gráfico de linha por tipo de residência</h2>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='data_ref', y='renda', hue='tipo_residencia', data=renda, ax=ax)
ax.tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(fig)
st.markdown('---')

st.write('## Gráficos bivariados')

# Gráfico 9
st.markdown('<h2 style="font-size:30px;">* Gráfico de barras por posse de imóvel</h2>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='posse_de_imovel', y='renda', data=renda, ax=ax)
sns.despine()
st.pyplot(fig)
st.markdown('---')

# Gráfico 10
st.markdown('<h2 style="font-size:30px;">* Gráfico de barras por posse de veículo</h2>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='posse_de_veiculo', y='renda', data=renda, ax=ax)
sns.despine()
st.pyplot(fig)
st.markdown('---')

# Gráfico 11
st.markdown('<h2 style="font-size:30px;">* Gráfico de barras por quantidade de filhos</h2>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='qtd_filhos', y='renda', data=renda, ax=ax)
sns.despine()
st.pyplot(fig)
st.markdown('---')

# Gráfico 12
st.markdown('<h2 style="font-size:30px;">* Gráfico de barras por tipo de renda</h2>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='tipo_renda', y='renda', data=renda, ax=ax)
sns.despine()
st.pyplot(fig)
st.markdown('---')

# Gráfico 13
st.markdown('<h2 style="font-size:30px;">* Gráfico de barras por educação</h2>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='educacao', y='renda', data=renda, ax=ax)
sns.despine()
st.pyplot(fig)
st.markdown('---')

# Gráfico 14
st.markdown('<h2 style="font-size:30px;">* Gráfico de barras por estado civil</h2>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='estado_civil', y='renda', data=renda, ax=ax)
sns.despine()
st.pyplot(fig)
st.markdown('---')

# Gráfico 15
st.markdown('<h2 style="font-size:30px;">* Gráfico de barras por tipo de residência</h2>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='tipo_residencia', y='renda', data=renda, ax=ax)
sns.despine()
st.pyplot(fig)
st.markdown('---')




