#Pipeline de ETL com Python
## Obejtivo do projeto é extrair dados de composição, tamanho do novelo, e outras das linhas presentes no site YarnSubs.
## O projeto foi dividido em arquivos diferentes Extracao partes 1 e 2 e Transformacao e Carregamento. Para melhorar a experiencia e poder dar a possibilidade de aplicar etapas distintas separadamente.

# Extração parte 2
## O site foi feito de forma hierarquica contendo links para cada marca e cada marca contendo links das linhas ativas e desativadas da respectiva marca.
## Nesse arquivo sera feita a extracao das informacoes de cada linha. 
## O input será o arquivo csv criado na etapa anterior ou o arquivo csv com as URLs das linhas ativas de cada marca.


#Importing libraries
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import pandas as pd

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}


#Importando arquivo base
data = pd.read_csv('Yarn_Links.csv')
yarn_links_data = data['Yarn Links'].tolist()

## Verificando a quantidade de links presentes no arquivo
print(len(yarn_links_data))

#Informações sobre as linhas que serão retiradas do site.
yarn_name = []
brand_name = []
weight = []
texture = []
fiber = []
needles = []
gauge = []
balls = []

#Pegando as infomações de cada linha

## Recomendo fazer esse processo em etapas, com intervalos de 100 a 300 links por vez até atingir a quantidade de links gerada acima.
## O processo será demorado, por isso tambem deixei abaixo informacoes de como fazer a paginacao das informacoes.
for numero in range (0,15):
  page = requests.get(f'https://yarnsub.com{yarn_links_data[numero]}', headers= headers)
  soup = BeautifulSoup(page.text, 'html.parser')
  details = soup.find(class_='details').find_all('td')
  th = soup.find(class_='details').find_all('th')
  brand = soup.find('div', {'class':'mainBrand'}).find_all('a')
  sleep(randint(2,5))
  for i, info in enumerate(th):
    if info.text == "Weight:":
      weight_index = i
  for i, info in enumerate(th):
    if info.text == "Texture:":
      texture_index = i
  for i, info in enumerate(th):
    if info.text == "Fiber:":
      fiber_index = i
  for i, info in enumerate(th):
    if info.text == "Needles:":
      needles_index = i
  for i, info in enumerate(th):
    if info.text == "Gauge:":
      gauge_index = i
  for i, info in enumerate(th):
    if info.text == "Balls:":
      balls_index = i
  for name in brand:
    brand_name.append((name.text).title())
  name = soup.find('h1').text
  yarn_weight = details[weight_index].text
  yarn_texture = details[texture_index].text
  yarn_fiber = details[fiber_index].text
  yarn_needles = details[needles_index].text
  yarn_gauge = details[gauge_index].text
  yarn_balls = details[balls_index].text

#Fazendo uma limpeza inicial dos dados durante a extração
  yarn_name.append(name.replace("\n",""))
  weight.append(yarn_weight.replace("\n",""))
  texture.append(yarn_texture[1:(len(yarn_texture)-3)])
  fiber.append(yarn_fiber.replace("\n",""))
  needles.append(yarn_needles.replace("\n",""))
  gauge.append(yarn_gauge.replace("\n",""))
  balls.append(yarn_balls.replace('\n',""))


#Código para baixar os arquivos parciais de informação das linhas
## Temos mais de 5 mil links a serem processados, recomendo fazer a paginação dos resultados salvando em arquivos csv parciais a cada mil links retornados.

info_data = pd.DataFrame({"Brand Names": brand_name, "Yarn Names" : yarn_name, "Weight": weight, "Texture": texture, "Fiber":fiber, "Needles": needles, "Gauge" : gauge, 'Balls': balls})
info_data.to_csv("Yarn_Info_v1.csv", index = None)

##Para juntar todos os arquivos antes da etapa de transformação
#info_data_v1 = pd.read_csv('Yarn_Info_v1.csv') #Insira uma versão (v1, v2,...) para cada arquivo parcial criado anteriormente
#info_data_v2 = pd.read_csv('Yarn_Info_v2.csv')
#yarn_info = pd.concat([info_data_v1, info_data_v2])

#Exportando o arquivo final com as informações de cada linha
#yarn_info.to_csv("Yarn_Information.csv")