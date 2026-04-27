# Dicionário Rápido para Análise
#---------------------------------#
1. Estrutura dos dados
2. Limpeza de dados
3. Manipulação
4. Estatísticas rápidas
5. Visualizações
6. Relações entre dados
7. Exploração
8. Outros conceitos
9. Conectar projeto ao GitHub
#---------------------------------#

## 1. Estrutura dos dados
- df.head() → primeiras linhas
- df.info() → tipos + nulos
- df.describe() → estatísticas gerais
- df.dtypes → verificar o tipo
- df.columns → nome das colunas

## 2. Limpeza de dados
- df.isnull().sum() → contar total de nulos
- df.dropna() → remover nulos
- df.fillna(valor) → preencher nulos
- df.duplicated() / drop_duplicates() → remover duplicatas
- astype(float) → converter para número
* Exemplo: df['metragem'] = df['metragem'].astype(float)

# --------------------------------- #
OBSERVAÇÃO:  
-> str: Atalho para manipular strings
  - str.replace → remover texto específico
  - str.extract → extrair apenas números com regex
  - str.lower() → converter para minúsculo
  - str.upper() → converter para maiúsculo
-> Regex: usada para buscar, identificar e manipular textos
# --------------------------------- #

## 3. Manipulação
- Criar coluna:
df['preco_m2'] = df['preco'] / df['metragem']

- Filtrar:
df[df['preco'] > 300000]

- Selecionar colunas:
df[['preco', 'metragem']]

## 4. Estatísticas rápidas
- Média: mean()
- Mediana: median()
- Máximo/Mínimo: max() / min()
- Desvio padrão: std()
- Agrupamentos: df.groupby('quartos')['preco'].mean() -> (preço médio por quartos
métricas por grupo)

## 5. Visualizações
- Histograma: 
sns.histplot(df['preco'])

- Scatterplot (relação): 
sns.scatterplot(x='metragem', y='preco', data=df)

- Boxplot (comparação):
sns.boxplot(x='quartos', y='preco', data=df)

- Barplot (média por grupo):
sns.barplot(x='quartos', y='preco', data=df)

## 6. Relações entre dados
- Correlação -> Mede a relação entre variáveis (de -1 a 1) 
df.corr()
* Próximo de 1 → forte relação positiva
  Próximo de -1 → relação negativa
  
- Heatmap:
sns.heatmap(df.corr(), annot=True)

## 7. Exploração
- Ordenar -> dados por uma coluna
df.sort_values(by='preco_m2')

- Top valores:
df.nlargest(10, 'preco')

- Menores valores:
df.nsmallest(10, 'preco')

## 8. Outros conceitos
- Insight: conclusão baseada em dados
- Outlier: valor muito fora do padrão
- Distribuição: como os dados se espalham
- requirements.txt: arquivo que lista todas as bibliotecas
-> pip install -r requirements.txt 

## 9. Conectar projeto ao GitHub
- Passo 01:
git init

- Passo 02:
git remote add origin https://github.com/seu-usuario/meu-projeto.git

- Passo 03:
git add .

- Passo 04:

git commit -m "Primeiro commit"

- Passo 05:
git branch -M main

git push -u origin main

- Passo 06: Para novas atualizações
git status 
git add .
git commit -m "Primeiro commit"
git push
