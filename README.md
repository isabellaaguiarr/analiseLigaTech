# Análise de Dados Imobiliários 

## Sobre o Projeto

Este projeto tem como objetivo explorar e analisar dados reais de imóveis, gerando insights sobre preços, metragem e características dos imóveis.

A análise foi desenvolvida utilizando Python e bibliotecas de ciência de dados, com foco em **limpeza de dados, análise exploratória e geração de insights relevantes para o mercado imobiliário**.

---

## Objetivos

* Entender a estrutura dos dados imobiliários
* Tratar inconsistências e valores ausentes
* Analisar a distribuição de preços
* Comparar imóveis com base em métricas padronizadas
* Identificar oportunidades de investimento

---

## Principais Insights Esperados

* Relação entre **preço e metragem**
* Impacto do número de quartos no preço
* Identificação de imóveis **subvalorizados (baixo preço por m²)**
* Distribuição dos preços no mercado

---

## Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## Etapas da Análise

### 1. Coleta de Dados

Leitura do dataset contendo informações de imóveis.

### 2. Limpeza de Dados

* Remoção de valores nulos
* Conversão de tipos (strings → números)
* Padronização de colunas

### 3. Feature Engineering

Criação da variável mais importante do projeto:

* **Preço por metro quadrado (`preco_m2`)**

Essa métrica permite comparar imóveis de forma mais justa.

### 4. Análise Exploratória

* Estatísticas descritivas (média, mediana, etc.)
* Distribuição de preços
* Análise de variáveis como metragem e quartos

### 5. Visualizações

* Histogramas (distribuição)
* Scatterplot (relações entre variáveis)
* Boxplot (comparações por grupo)
* Heatmap (correlação)

### 6. Identificação de Oportunidades

* Imóveis com menor preço por m²
* Imóveis com maior valorização

---

## Estrutura do Projeto

```
projeto-imoveis/
│
├── data/
│   └── imoveis.csv
│
├── notebooks/
│   └── analise.ipynb
│
├── dicionario.md
├── estrutura.md
├── webScraping.py
└── README.md
```

---

## Organização do Projeto (Equipe)

* **Data Cleaning:** tratamento de dados e preparação
* **Análise Exploratória:** estatísticas e entendimento dos dados
* **Visualização:** criação de gráficos
* **Insights:** interpretação dos resultados
* **Documentação:** organização e apresentação

---

## Apoio – Dicionário de Análise

O arquivo `dicionario.md` funciona como um guia rápido com comandos e conceitos utilizados durante o projeto, auxiliando na execução e entendimento das análises.


---

## Como Executar

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/projeto-imoveis.git
```

2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Execute o notebook:

```
jupyter notebook
```

---

## Conclusão

Este projeto demonstra a aplicação prática de técnicas de análise de dados em um contexto real, permitindo a geração de insights relevantes para tomada de decisão no mercado imobiliário.

---

## Autores

Projeto desenvolvido por membros da liga tech.

---
