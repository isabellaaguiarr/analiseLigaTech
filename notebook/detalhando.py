# PROJETO: Análise de Imóveis - Samambaia
# Objetivo:
# Explorar dados reais de imóveis e gerar insights sobre preços,
# metragem e características dos imóveis.
# ========================================= #
# 1. Importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 2. Carregando os dados
import os

caminho = os.path.join("..", "data", "imoveis_anapolis_sem_limpeza.csv")
df = pd.read_csv(caminho)

# 3. Entendimento inicial dos dados
print(df.head())
print(df.info())
print(df.describe())
print(df.dtypes)
print(df.columns)

# 4. Limpeza de dados
df.isnull().sum()

# Removendo valores nulos
df = df.dropna().copy()
print(df.isnull().sum())

# Tratamento da coluna metragem (remover "m²")
print(df['metragem'].head()) # Antes da limpeza

df['metragem'] = (
    df['metragem']
    .str.replace(" m²", "", regex=False)
    .astype(float)
)

# df['metragem'].dtype # Depois da limpeza

# Tratamento da coluna vagas (remover "Vagas" / "Vaga")
# Ver os 5 primeiros valores da coluna metragem antes da limpeza
print(df['vagas'].head()) 

df['vagas'] = (
    df['vagas']
    .str.extract(r'(\d+)')[0]
    .astype(int)
)
# df['vagas'].head(5)

# Garantindo tipo numérico do preço
print(df['preco'].head())

df['preco'] = pd.to_numeric(df['preco'], errors='coerce')

# df['preco'].head(5)

# Análises básicas
print("Preço médio:", df['preco'].mean())
print("Metragem média:", df['metragem'].mean())
print("Média de quartos:", df['quartos'].mean())

# 6. Criando nova variável (ESSENCIAL)
# # Exemplo de dados fictícios (transformando valores absolutos em uma métrica comparável)
# df_explicacao = pd.DataFrame({
#     "preco": [400000, 800000, 300000],
#     "metragem": [100, 200, 75],
#     "quartos": [2, 3, 1]
# })

# # Antes de criar a nova variável
# print("Antes:")
# print(df_explicacao.head())

# # Criando a variável essencial: preço por metro quadrado
# df_explicacao['preco_m2'] = df_explicacao['preco'] / df_explicacao['metragem'] # (quanto custa CADA metro quadrado)

# # Depois da criação
# print("\nDepois:")
# print(df_explicacao.head())

df['preco_m2'] = df['preco'] / df['metragem']
df.head(2)

# 7. Visualizações
# Distribuição de preços
plt.figure()
sns.histplot(df['preco'], bins=30)
plt.title("Distribuição de Preços")
plt.xlabel("Preço")
plt.show()

# Preço por m²
plt.figure()
sns.histplot(df['preco_m2'], bins=30)
plt.title("Distribuição do Preço por m²")
plt.xlabel("Preço por m²")
plt.show()

# Relação metragem vs preço
plt.figure()
sns.scatterplot(x='metragem', y='preco', data=df)
plt.title("Preço vs Metragem")
plt.show()

# Quartos vs preço
plt.figure()
sns.boxplot(x='quartos', y='preco', data=df)
plt.title("Preço por Número de Quartos")
plt.show()

# outros
# # Imóveis com menor preço por m² (possíveis boas oportunidades)
# df.sort_values(by='preco_m2').head(10)

# # Imóveis mais caros por m²
# df.sort_values(by='preco_m2', ascending=False).head(10)


