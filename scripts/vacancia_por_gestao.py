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
	cod = fii[3]+'11'
	url = 'https://www.clubefii.com.br/fundo_descricao?cod=%s'%(cod)
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	td = soup.find_all('td')

	print('GETTING %s\n'%(cod))
	print(td)
	print('\n\n\n')

	handle = open('gestores/'+cod+'.html', 'a+')
	if len(td) >= 11:
		print('SALVANDO ARQUIVO\n')
		handle.write(str(td[10]))
	else:
		handle.write(str(td))
	handle.close()


	# for x in td:
	# 	print('%d -> %s'%(c, x))
	# 	c += 1

