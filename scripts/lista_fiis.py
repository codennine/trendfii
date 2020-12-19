#coding=utf8
import requests
from bs4 import BeautifulSoup

URL_LIST_FIIS = 'http://bvmf.bmfbovespa.com.br/Fundos-Listados/FundosListados.aspx?tipoFundo=imobiliario&Idioma=pt-br'

headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}


page = requests.get(URL_LIST_FIIS,headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

trs = soup.find_all('tr')


table = [
	['Razão Social', 'Fundo', 'Segmento', 'Código']
]

fundo = {}


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
else:
	print('SEM ELEMENTOS')


URL = 'https://www.clubefii.com.br/fundo_basico?cod='
for fii in table[1:]:
	cod = fii[3]+'11'
	req_url = URL + cod

	print('Requesting...')
	print(req_url)

	page = requests.get(req_url, headers=headers)
	if page.status_code == 200:
		soup = BeautifulSoup(page.content, 'html.parser')
		table = soup.find('table', {'id': 'secundaryTable'})
		primary = soup.find('table', {'id': 'primaryTable'})

		handle = open('gestores/'+cod+'.html', 'w+')
		print('SALVANDO ARQUIVO\n')
		handle.write(str(primary))
		handle.write('\n\r')
		handle.write(str(table))
		handle.close()

	# break


	# print('Requesting ...')
	# print(fii[0]['link'])
	# page = requests.get(fii[0]['link'],headers=headers)
	# print(page.__dict__)
	# soup = BeautifulSoup(page.content, 'html.parser')
	# panel1a = soup.find('div', {'id': 'panel1a'})
	# if not panel1a is None:
	# 	tr = panel1a.find_all('tr')
	# 	td = tr[2].find_all('td')
	# 	cnpj_fundo = td[1].text
	# 	print(cnpj_fundo)
	# else:
	# 	print('PANEL 1 A is none')
	# 	print(panel1a)
	# c += 1
	
	
