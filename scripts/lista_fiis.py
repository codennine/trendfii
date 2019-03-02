#coding=utf8
import requests
from bs4 import BeautifulSoup

URL_LIST_FIIS = 'http://bvmf.bmfbovespa.com.br/Fundos-Listados/FundosListados.aspx?tipoFundo=imobiliario&Idioma=pt-br'

page = requests.get(URL_LIST_FIIS)
soup = BeautifulSoup(page.content, 'html.parser')
trs = soup.find_all('tr')
table = [
	['Razão Social', 'Fundo', 'Segmento', 'Código']
]


# loop em cada linha que não for cabeçalho
for tr in trs[1:]:
	row = []
	for td in tr.find_all('td'):
		if td.a != None:
			data = {'link': 'http://bvmf.bmfbovespa.com.br/Fundos-Listados/' + td.a['href'], 'text': td.a.text}
		else:
			data = td.text
		row.append(data)
	table.append(row)

for fii in table[1:]:
	print(fii[3]+'11')