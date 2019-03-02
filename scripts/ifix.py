#coding=utf8
import requests
from bs4 import BeautifulSoup

URL_IFIX = 'http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=IFIX&idioma=pt-br'

page = requests.get(URL_IFIX)
soup = BeautifulSoup(page.content, 'html.parser')

table = [
	['Cód', 'Participação (%)']
]

trs = soup.find_all('tr')
soma=0.0
for tr in trs[2:]:
	td = tr.find_all('td')
	table.append([td[0].text, float(td[4].text.replace(',', '.'))])
	soma += float(td[4].text.replace(',', '.'))

print('\n')
print(table)
print('\n')
print('SOMA TOTAL: %.2f%%'%(soma))
