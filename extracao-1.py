#Pipeline de ETL com Python
## Obejtivo do projeto é extrair dados de composição, tamanho do novelo, e outras das linhas presentes no site YarnSubs.
## O projeto foi dividido em arquivos diferentes Extracao partes 1 e 2 e Transformacao e Carregamento. Para melhorar a experiencia e poder dar a possibilidade de aplicar etapas distintas separadamente.

# Extração parte 1
## O site foi feito de forma hierarquica contendo links para cada marca e cada marca contendo links das linhas ativas e desativadas da respectiva marca.
## Nesse arquivo sera feita a extracao do URL das marcas de linhas e o URL das linhas ativas presentes em cada marca.
## O output desse arquivo será um arquivo csv com os links das linhas ativas de cada marca dentro do site.

#Importing libraries
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import pandas as pd

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}

brand_links = []
yarn_links = []

#Pegando os links de cada marca
brand_page = requests.get("https://yarnsub.com/yarns", headers= headers)
brand_soup = BeautifulSoup(brand_page.text, 'html.parser')
levels = brand_soup.find_all('div', {'class':'brandName'})

for url in levels:
  brand_names = url.find('a').get('href') #Vai pegar o final da URL relativa a cada marca de fios
  brand_links.append(brand_names)


#Pegando os links de cada linha dentro dos links de cada marca
## Verificando o tamanho do arquivo de brand links, para definir quantas iterações serao necessarias para a proxima etapa
print(len(brand_links))

## Recomendo fazer esse processo em etapas, com intervalos de 100 ou 200 links por vez até atingir o valor de tamanho de arquivo do brand link gerado acima.
for numero in range(0,10): 
  yarn_page = requests.get(f'https://yarnsub.com{brand_links[numero]}', headers= headers)
  yarn_soup = BeautifulSoup(yarn_page.text, 'html.parser')
  if yarn_soup.find (class_ = 'yarnList popularYarns') is not None: #Para evitar o erro de não possuir linhas ativas dentro da marca
    yarn_list = yarn_soup.find(class_ = 'yarnList popularYarns').find_all(class_ = 'yarn')
  sleep(randint(2,6))
  for yarn_url in yarn_list:
    yarn_names = yarn_url.find('a').get('href') #Pegando a URL referente a cada linha de cada marca dentro de brand_links
    yarn_links.append(yarn_names)


#Exportando o arquivo de links das linhas
yarn_links = pd.DataFrame({"Yarn Links":yarn_links})
yarn_links.to_csv('Yarn_Links.csv', na_rep="NaN",index=None)