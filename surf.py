import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


lista_praia = ['torrefacao', 'espanhol', 'paciencia', 'farol-da-barra', 'barravento', 'tonys', 'praia-da-onda', 'pescador', 'secret-2', 'stella', 'aleluia',]

for praia in lista_praia:
    url = f'https://www.waves.com.br/surf/ondas/condicao/bahia/{praia}'

option = Options()
option.headless = True
driver = webdriver.Chrome()

driver.get(url)
time.sleep(5)

for praia in lista_praia:
    htmldata = requests.get(
        f'https://www.waves.com.br/surf/ondas/condicao/bahia/{praia}').content
    soup = BeautifulSoup(htmldata, "html.parser")
    vento_direcao = soup.find("td", {"id": "forecast_wind_direction"})
    vento_intensidade = soup.find("td", {"id": "forecast_wind_intensity"})
    onda_tamanho = soup.find("td", {"id": "forecast_wave_size"})
    print('~*' *20)
    print(f'{praia.capitalize()}:')
    print(f'Direção do vento: {vento_direcao.text.strip()}')
    print(f'Intensidade do Vento: {vento_intensidade.text.strip()}')
    texto_onda_tam = str(onda_tamanho.span.text.strip())
    if texto_onda_tam == "Flat":
        print(f'Tamanho da onda: {onda_tamanho.text.strip()}')
    else:
        print(f'Tamanho da onda: {onda_tamanho.text.strip()[:4]}m')

element_wave_size = driver.find_element_by_id('forecast_wave_size')
html_content = element_wave_size.get_attribute('outerHTML')
print(html_content)
       
