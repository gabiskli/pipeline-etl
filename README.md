# Pipeline de ETL com Python
🧶 Construindo um banco de dados com informações sobre linhas de crochê / tricô🧶

✅ Status: Concluído ✅


## Tabela de conteúdos
* [Sobre o Projeto](#-sobre-o-projeto)
* [Tabela de Conteúdos](#tabela-de-conteúdos)
* [Como utilizar o Projeto](#-como-utilizar-o-projeto)
	* [Etapas do Processo ETL](#etapas-do-processo)
	* [Arquivos](#arquivos-do-projeto)
	* [Instruções de Uso](#instruções-de-uso)
* [Tecnologias](#%EF%B8%8F-tecnologias-utilizadas)
* [Próximos Passos](#-próximos-passos-)
* [Licença](#-licença)

## 💻 Sobre o Projeto

O projeto consiste em uma Pipeline ETL (Extração, Transformação e Carregamento) com o objetivo de obter um banco de dados de linhas de crochê e tricô presentes no mercado internacional.

Projeto desenvolvido durante o Bootcamp Santander 2023 - Ciência de Dados com Python.

## 🔍 Como utilizar o projeto


### Etapas do Processo

#### 1.  Extração:
Será feita usando web scraping com python retirando dados do site [YarnSubs](https://.yarnsub.com/).

A extração foi dividida em duas etapas por causa da configuração do site. A primeira parte envolve a extração dos links de cada linha. E a segunda parte utilizará esse arquivo para extrair as informações de cada linha, que montará o banco de dados.
#### 2.  Transformação: 
Serão criadas novas colunas, assim como reclassificação e normalização dos dados.
#### 3.  Carregamento:
A saída do pipeline será dada por um arquivo csv final, com as informações limpas.

### Arquivos do Projeto

- ``extracao-1.py``: Contém o código em Python da primeira parte da extração dos dados.
- ``extracao-2.py``: Contém o código da segunda parte da extração dos dados.
- ``tranformacao-carregamento.py``: Contém o código da parte final do processo de ETL.
- ``Yarn_Links.csv``: Arquivo de saída da primeira parte da extração que será usada como input para a segunda parte.
- ``Yarn_Information.csv``: Arquivo de saída final da extração que será usado como input na fase de transformação dos dados.
- ``Yarn_Info_Clean.csv``: Arquivo final do programa que contém o banco de dados limpo.

### Instruções de Uso
- Certifique-se de ter Pyhton 3.x instalado.
- Instale as seguintes bibliotecas
(código)
- Execute o arquivo ``extracao-parte-1.py``
- Com o arquivo final de links (``Yarn_Links.csv``) , execute o arquivo ``extração-parte-2.py`` 
- Por fim, utilizando o arquivo csv com as informações brutas (``Yarn_Information.csv``), execute o arquivo ``tranformacao-carregamento.py`` para obter o arquivo csv final.

##  🛠️ Tecnologias Utilizadas

Nesse projeto foram utilizadas as seguintes tecnologias:

* [Python 3.x](https://docs.python.org/3/)

* [Pandas](https://pandas.pydata.org/docs/)

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

* [Regex](https://docs.python.org/3/library/re.html)

## 🚧 Próximos Passos 🚧

A ideia de criar essa pipeline ETL faz parte de um projeto pessoal maior onde os dados extraído aqui serão utilizados para criar um programa em Python para comparação de fios. O programa será baseado no próprio site [YarnSubs](https://yarnsub.com/), onde a etapa de web scraping foi realizada.

## 📋 Licença
Este projeto está sob a licença [MIT License](/LICENSE)

💜Feito por Gabriela Klitzke. 
[Entre em contato!](https://www.linkedin.com/in/gabrielaklitzke/)
