# Roteiro de análise simples 
# Etapa 1 — Entendimento dos dados
df.head()
df.info()
df.describe()

## Perguntas:
- Quantos imóveis temos?
- Tem valores faltando?
- Qual a faixa de preço?

# Etapa 2 — Limpeza leve 
df.isnull().sum()
df = df.dropna()

## Insight:
Dados incompletos impactam análise

# Etapa 3 — Análises básicas
## Pergunta:
* 1. Preço médio
df['preco'].mean()

* 2. Metragem média
df['metragem'].astype(float).mean()

* 3. Média de quartos
df['quartos'].astype(float).mean()

# Etapa 4 — Criar variável importante 
df['preco_m2'] = df['preco'] / df['metragem'].astype(float)

# Etapa 5 — Visualizações 
- Histograma de preços
sns.histplot(df['preco'], bins=30)
plt.title("Distribuição de Preços")
plt.show()

# ------------------------------------------ # 
Exemplos de perguntas:

Existe imóvel barato com metragem alta? (oportunidade)
Qual faixa de preço mais comum?
Imóveis com mais quartos realmente são mais caros?
Existe “outlier” (muito caro ou muito barato)?
Qual o melhor custo-benefício (menor preço/m²)?
# ------------------------------------------ # 
# Desafio:
## Cada grupo deve:
- Fazer 3 gráficos
- Criar 3 insights
- Apresentar uma conclusão

## Ideias de conclusão que eles podem chegar
- Imóveis grandes nem sempre têm melhor custo-benefício
- Existe concentração de preços entre x e y
- Preço por m² varia bastante → mercado ineficiente