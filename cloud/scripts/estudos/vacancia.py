#https://fiis.com.br/rngo11/?aba=geral

import requests
import re
from bs4 import BeautifulSoup

def vacancia(cod):
    url = 'https://fiis.com.br/%s/?aba=geral'%(cod)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table')
    return table


x = vacancia('ABCP11')
c = 0

td = x.find_all('tr')[14].find_all('td')[1]
textos = td.text.split('.')

index = None

for t in textos:
    if('Vacância' in t):
        index = c
    c += 1

if not index is None:
    vacancia = textos[index]
    print(vacancia)

#.replace(',', '.').replace('Vacância', '').replace('%', '').replace(' ', '')
# regex = re.compile(r'\(\d{2}\/\d{2}\)')
# vacancia = regex.sub('', vacancia)

# valor_vacancia = float(vacancia)
# print(valor_vacancia)

# for tr in x.find_all('tr'):
#     print(c)
#     print(tr)
#     print('\n\n')
#     c += 1

