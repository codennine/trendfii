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

fiis = []


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
	fiis.append(cod)

	print('REQUISITANDO FII '+cod+'\n')
	# page_ativos = requests.get('https://clubefii.com.br/fiis/'+cod+'#ativos')
	page_ativos = requests.post('https://clubefii.com.br/fundo_ativo_listagem?modo_adm=', data={'cod_neg':cod})
	print('Status: '+str(page_ativos.status_code))

	if page_ativos.ok:
		handle = open('ativos_fiis/'+cod+'.html', 'a+')
		handle.write(str(page_ativos.content))
		handle.close()

	print('-'*30)
	print('\n')


print(fiis)