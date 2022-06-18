from bs4 import BeautifulSoup

import requests

site = requests.get('https://www.climatempo.com.br/').content
#Objeto site recebendo o conteudo da requisição http do site...

soup = BeautifulSoup(site, 'html.parser')
# objeto soup baixando do site o html
print(soup.prettify())
# transforma html em string html