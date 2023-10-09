#Pipeline de ETL com Python
## Obejtivo do projeto é extrair dados de composição, tamanho do novelo, e outras das linhas presentes no site YarnSubs.
## O projeto foi dividido em arquivos diferentes Extracao partes 1 e 2 e Transformacao e Carregamento. Para melhorar a experiencia e poder dar a possibilidade de aplicar etapas distintas separadamente.

# Transformacao
## O site foi feito de forma hierarquica contendo links para cada marca e cada marca contendo links das linhas ativas e desativadas da respectiva marca.
## Nesse arquivo sera feita a tranformacao dos dados coletados e a exportacao do arquivo final do projeto com os dados limpos, que equivale a etapa de carregamento.
## O input será o arquivo csv criado na etapa anterior ou o arquivo csv com os dados brutos das linhas.


#Importing libraries
import pandas as pd
import re

#Importando o arquivo base

yarn_info = pd.read_csv("Yarn_Information.csv") 

#yarn_info['Brand Names'] = yarn_info['Brand Names'].astype('str')

# Etapas da transformacao dos dados
# 1.Extraindo apenas os dados em milimetros das agulhas
yarn_info_needles = yarn_info['Needles'].str.extract(r'(\d+mm|\d.\d+mm)')
yarn_info_needles.rename(columns = {0 : 'needles'}, inplace=True)


# 2.Dividindo a coluna Balls em duas, uma com o peso do novelo (Ball Weight) e outra com a metragem do novelo (Ball Size) 
ball_weight = []
ball_size = []
yarn_info_balls = pd.DataFrame({'ball_weight_g':ball_weight , 'ball_size_m':ball_size})

yarn_info_balls['ball_weight_g'] = yarn_info['Balls'].str.extract('(\d+)')
yarn_info_balls['ball_size_m'] = yarn_info['Balls'].str.extract(r'( \d+)')


# 3.Dividindo a coluna Gauge em duas, uma com o numero de pontos necessario para uma amostra de 10 cm (Gauge Sts) e outra com a quantidade de linhas necessárias (Gauge rows)
gauge_sts = []
gauge_rows = []
yarn_info_gauge = pd.DataFrame({'gauge_sts':gauge_sts, 'gauge_rows':gauge_rows})

yarn_info_gauge['gauge_sts'] = yarn_info['Gauge'].str.extract(r'(\d+ sts)')
yarn_info_gauge['gauge_rows'] = yarn_info['Gauge'].str.extract(r'( \d+ rows)')


# 4. Dividindo a coluna Fiber por componente e depois dividindo cada componente em nome do componente e porcentagem do componente da composição final.
yarn_info_fiber = yarn_info['Fiber'].str.split(',',expand = True)
fiber_type = []
fiber_qty =[]

for i in range(0, len(yarn_info_fiber.columns)):
  ftype = yarn_info_fiber[i].str.extract(r'(\w+)')
  ftype.rename(columns = lambda x : f'fiber_type_{x+i+1}' , inplace=True)
  fqty = yarn_info_fiber[i].str.extract(r'(\d+)')
  fqty.rename(columns = lambda x : f'fiber_qty_{x+1+i}' , inplace=True)
  fiber_type.append(ftype)
  fiber_qty.append(fqty)
yarn_fiber_type = pd.concat(fiber_type, axis=1)
yarn_fiber_qty = pd.concat(fiber_qty, axis=1)

yarn_info_fiber_2 = pd.concat([yarn_fiber_type, yarn_fiber_qty], axis=1)

# 5.Classificando a coluna Weight conforme tabela do Raverly

## Getting only first occurence of the weight name
## Pegando apenas a primeira ocorrência do peso do fio
yarn_info_weight = yarn_info['Weight'].str.split('/', expand = True)[0]
yarn_info_weight = yarn_info_weight.str.rstrip()
yarn_info_weight = yarn_info_weight.to_frame('weight')

## Replacing names to standardize the categories
## Padronizando as categorias
yarn_info_weight.replace('Heavy Worsted', 'Aran', inplace= True)
yarn_info_weight.replace('Carry-along', 'Decorative', inplace= True)
yarn_info_weight.replace('Ruffle', 'Meshed', inplace= True)


# 6.Retirando as colunas que não serao utilizadas e juntando com as novas colunas criadas.
yarn_info_2 = yarn_info 
yarn_info_2 = yarn_info_2.drop(columns= ['Weight','Fiber','Needles','Gauge','Balls']) 
yarn_info_2 = pd.concat([yarn_info_2,yarn_info_weight,yarn_info_fiber_2, yarn_info_needles, yarn_info_gauge, yarn_info_balls], axis=1)

yarn_info_2 = yarn_info_2.rename(columns = {'Brand Names' : 'brand_name','Yarn Names': 'yarn_name', 'Texture': 'texture'})


# 7.Replacing brand name 'Knit One, Crochet Too'
# Adicionando aspas ao nome da marca 'Knit One, Crochet Too' para evitar problemas posteriores com o arquivo csv.
yarn_info_2['brand_name'].replace('Knit One, Crochet Too','"Knit One, Crochet Too"',inplace=True)


# Carregamento : Exportando o arquivo final para csv.
## Essa já se caracteriza como a etapa de Carregamento dentro do pipeline de ETL proposto durante o projeto.
yarn_info_2.to_csv('Yarn_Information_Clean.csv', na_rep="NaN",index=None)