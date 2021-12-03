import requests
from bs4 import BeautifulSoup



lista_praia = ['torrefacao', 'espanhol', 'paciencia', 'farol-da-barra', 'barravento', 'tonys', 'praia-da-onda', 'pescador', 'secret-2', 'stella', 'aleluia',]



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
       
