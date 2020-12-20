#coding=utf8
""""
	author: Edigleysson Silva
	Description: Esse script faz a busca de dados sobre fiis. Para tal são utilizadas duas fontes
	uma das fontes é a BMF onde é feita a listagem de fiis existentes.

	Após isso os detalhes do fundo são buscados no clubefii que já tem os dados sintetizados
"""

import requests
from bs4 import BeautifulSoup
import json

URL_LIST_FIIS = 'http://bvmf.bmfbovespa.com.br/Fundos-Listados/FundosListados.aspx?tipoFundo=imobiliario&Idioma=pt-br'

page = requests.get(URL_LIST_FIIS)
soup = BeautifulSoup(page.content, 'html.parser')
trs = soup.find_all('tr')
table = [
	['Razão Social', 'Fundo', 'Segmento', 'Código']
]

headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}


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

fii_data = [
	['CODIGO', 'GESTOR', 'CNPJ', 'DATA IPO', 'ABL']
]

for fii in table[1:]:
	cod = fii[3]+'11'
	url = 'https://www.clubefii.com.br/fundo_descricao?cod=%s'%(cod)
	page = requests.get(url, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	table = soup.find('table')
	td = soup.find_all('td')

	print('GETTING %s\n'%(cod))

	# handle = open('../static/gestores/'+cod+'.html', 'a+')
	# handle_fund = open('../static/funds/'+cod+'.html', 'a+')
	# handle.truncate()
	if len(td) >= 11:
		gestor = str( td[10].find('div').text )
		cnpj = str( td[7].find('div').text )
		data_ipo = str( td[1].find('div').text )
		abl = str( td[3].find('div').text )
		fii_data.append([cod, gestor, cnpj, data_ipo, abl])
		# table.append
		# handle.write(str(td[10]))
		# handle_fund.write(str(table))
	else:
		pass
		# handle.write(str(td))
	# handle.close()
	# handle_fund.close()

	# break

json_content = json.dumps({'heading': fii_data[0],'data': fii_data[1:]})
handle = open('../static/data.json', 'a+')
handle.write(json_content)
handle.close()

print('Arquivo data.json criado com sucesso')
print('{0} fiis encontrados e registrados no arquivo'.format(len(fii_data)-1))