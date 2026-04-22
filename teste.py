# Importacao de Bibliotecas
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from geopy.distance import geodesic
from statsmodels.stats.outliers_influence import variance_inflation_factor
import matplotlib.pyplot as plt 
import statsmodels.api as sm
import seaborn as sns
import pandas as pd
import numpy as np
import requests
import re 
import os 


# Configuracao do WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors") 
options.add_argument("--disable-blink-features=AutomationControlled") 

driver = webdriver.Chrome(options=options)
driver.delete_all_cookies() 

url = 'https://www.dfimoveis.com.br/'
driver.get(url)

wait = WebDriverWait(driver, 10)


# Parametros da Busca
tipo = "VENDA"
tipos = "APARTAMENTO"
estado = "GO"
cidade = "ANAPOLIS"


# Funcoes Auxiliares
def preencher_filtro(by, value, texto):
    """Preenche os filtros de busca no site."""
    try:
        element = wait.until(EC.element_to_be_clickable((by, value)))
        element.click()
        search_field = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "select2-search__field")))
        search_field.send_keys(texto)
        search_field.send_keys(Keys.ENTER)
    except Exception as e:
        print(f"Erro ao preencher filtro: {e}")
        raise e 


# Execucao da Busca
print("\nIniciando busca de imóveis...")
driver.get(url) 
sleep(2) 

preencher_filtro(By.ID, 'select2-negocios-container', tipo)
preencher_filtro(By.ID, 'select2-tipos-container', tipos)
preencher_filtro(By.ID, 'select2-estados-container', estado)
preencher_filtro(By.ID, 'select2-cidades-container', cidade)

busca = wait.until(EC.element_to_be_clickable((By.ID, "botaoDeBusca")))
busca.click()


# Coleta de Dados
lst_imoveis = []

while True:
    print("   Coletando dados da página...")
    try:
        elementos = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@id='resultadoDaBuscaDeImoveis']//a[contains(@href, '/imovel/')]")))
    except Exception as e:
        print(f"   Fim da busca ou erro: {e}")
        break

    if not elementos:
        break

    for elem in elementos:
        try:
            titulo = elem.find_element(By.CLASS_NAME, 'ellipse-text').text
            preco = elem.find_element(By.CLASS_NAME, 'body-large').text

            # Quartos
            quartos_elem = elem.find_element(
                By.XPATH, ".//div[contains(text(), 'Quarto') and contains(@class, 'rounded-pill')]"
            )
            quartos_num = int(quartos_elem.text.split(' ')[0])

            # Metragem
            metragem_texto = np.nan
            try:
                metragem_elem = elem.find_element(
                    By.XPATH, ".//div[contains(@class, 'web-view') and contains(text(), 'm²')]"
                )
                metragem_texto = metragem_elem.text
            except:
                pass 

            # Vagas
            vagas_texto = np.nan
            try:
                vagas_elem = elem.find_element(
                    By.XPATH, ".//div[contains(@class, 'rounded-pill') and (contains(text(), 'Vaga') or contains(text(), 'Vagas'))]"
                )
                vagas_texto = vagas_elem.text
            except:
                pass 

            # Registro do imovel
            imovel = {
                'titulo': titulo,
                'preco': preco,
                'quartos': quartos_num,
                'metragem': metragem_texto, 
                'vagas': vagas_texto        
            }
            lst_imoveis.append(imovel)
        except:
            continue

    # Proxima pagina
    try:
        botao_proximo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.btn.next')))
        if "disabled" in botao_proximo.get_attribute("class"):
            break
        driver.execute_script("arguments[0].click();", botao_proximo)
        sleep(2) 
    except:
        break


# Finalizacao
driver.quit()
df_total = pd.DataFrame(lst_imoveis)

output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

csv_path = os.path.join(output_dir, "imoveis_total_anapolis_sem_limpeza.csv")
df_total.to_csv(csv_path, index=False, encoding="utf-8")

print(f"Arquivo salvo em: {csv_path}")

# ----------------------------------------------- #
# PARTE 2 - Tratando os dados  
# Trasformando vaga em booleano 
df_total['vaga'] = df_total['vaga'].str.contains(r'\b1\s*VAGA\b|\bVAGA\b', flags=re.IGNORECASE, regex=True).astype(int)

# Convertendo o preco para numero
df_total["preco"] = pd.to_numeric(
    df_total["preco"].str.extract(r"(\d[\d\.,]*)")[0].str.replace(".", "").str.replace(",", "")
)
# Aparecer apenas a metragem 
df_total['metragem'] = df_total['metragem'].str.extract(r'(\d+)[^a-zA-Z]*')

# Aparecer apenas o numero de quartos 
df_total['quartos'] = df_total['quartos'].str.extract(r'(\d+)')

# Padronizando e completando os enderecos
df_total["endereco"] = df_total["endereco"].str.upper().str.strip()
df_total["endereco"] = df_total["endereco"].apply(
    lambda x: x if "SAMAMBAIA" in x else f"{x}, SAMAMBAIA SUL, SAMAMBAIA"
)

# Extraindo padroes validos de endereco
padrao_endereco = r"(Q[RN]\s?\d{3}(?:\s?CONJUNTO\s?\d+)?(?:,\s?SAMAMBAIA (?:SUL|NORTE), SAMAMBAIA)?)"
df_total["endereco"] = df_total["endereco"].str.extract(padrao_endereco)

# Removendo enderecos invalidos e ruidos
df_total = df_total.dropna(subset=["endereco"])
df_total["endereco"] = df_total["endereco"].str.replace(r",\s?\d+[\.,]?\d*", "", regex=True)

# Transformando espacos vazios em NaN
df_total.replace(r'^\s*$', np.nan, regex=True, inplace=True)

# Removendo duplicatas e ordenando por preco
df_total = df_total.drop_duplicates().sort_values(by="preco", ascending=False)

