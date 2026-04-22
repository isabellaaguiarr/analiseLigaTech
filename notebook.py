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

# 2. Carregando os dados
df = pd.read_csv("imoveis_samambaia.csv")
df.head()

# 3. Entendimento inicial dos dados
df.info()
df.describe()

# ========================================= #
# Perguntas iniciais:
# - Quantos imóveis existem?
# - Existem valores nulos?
# - Qual a faixa de preços?
# ========================================= #

# 4. Limpeza de dados
df.isnull().sum()

# Removendo valores nulos
df = df.dropna()

# Convertendo tipos (se necessário)
df['metragem'] = df['metragem'].astype(float)
df['quartos'] = df['quartos'].astype(float)

# Análises básicas
print("Preço médio:", df['preco'].mean())
print("Metragem média:", df['metragem'].mean())
print("Média de quartos:", df['quartos'].mean())

# 6. Criando nova variável (ESSENCIAL)
df['preco_m2'] = df['preco'] / df['metragem']
df.head()

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

# ==================== AVANÇADO ===================== #
# 8. Correlação
corr = df[['preco', 'metragem', 'quartos', 'preco_m2']].corr()
plt.figure()
sns.heatmap(corr, annot=True)
plt.title("Mapa de Correlação")
plt.show()

# 9. Identificando oportunidades
# Imóveis com menor preço por m² (possíveis boas oportunidades)
df.sort_values(by='preco_m2').head(10)

# Imóveis mais caros por m²
df.sort_values(by='preco_m2', ascending=False).head(10)
# ========================================= #
