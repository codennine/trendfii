#coding=utf8
import requests
from bs4 import BeautifulSoup
import sys
import re
import time


def codigo_ativo(title):
	found = re.findall('\(\w+\)', title)
	if len(found) > 0:
		return found[0].replace('(', '').replace(')', '')
	return None

start = time.time()

# recuperando data para pesquisar
# o formato deve ser yyyy-mm-dd
try:
	data = sys.argv[1]
except IndexError:
	print('Informe uma data para pesquisar')
	exit();


PREFIX = 'http://www2.bmfbovespa.com.br/Agencia-Noticias/'
URL_FII = 'http://www2.bmfbovespa.com.br/Agencia-Noticias/ListarNoticias.aspx?idioma=pt-br&q=fii&tipoFiltro=3&periodoDe=%s&periodoAte=%s&pg='%(data, data)
QTD_PER_PAGE = 20
PAGE = 1
_URL = URL_FII+str(PAGE)
page = requests.get(_URL)

print('Requesting page %d'%(PAGE))
print(_URL)

soup = BeautifulSoup(page.content, 'html.parser')
total_encontrado = int(soup.find('p', {'class': 'dadosFiltro'}).b.text)
links_noticias = soup.find('ul', {'id': 'linksNoticias'}).find_all('li')
print(len(links_noticias))
total = total_encontrado - len(links_noticias)
print('-'*50)
while total > 0:
	PAGE += 1
	_URL = URL_FII+str(PAGE)
	print('Requesting page %d'%(PAGE))
	print(_URL)
	page = requests.get(_URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	k = soup.find('ul', {'id': 'linksNoticias'}).find_all('li')
	links_noticias = links_noticias + k
	print(len(k))
	total = total - len(k)


# 

sources = []
count = 0
for link in links_noticias:
	print('Buscando[%d] %s | Ativo %s11'%(count, link.text, codigo_ativo(link.text)))
	href = link.find('a')['href']
	page = requests.get(PREFIX+href)

	soup = BeautifulSoup(page.content, 'html.parser')
	link_documento = soup.find('div', {'id': 'contentNoticia'}).find('pre')
	index = link_documento.text.find('&flnk')

	if index != -1:
		h = link_documento.text[0:index]
		h = h.replace('visualizar', 'exibir')
		sources.append({
			'title': link.text,
			'doc' : h
		})
	count += 1


sources.reverse()

[print(a) for a in sources]

end = time.time()

print('-'*50)
print('Execution time: %f'%((end-start)))



	
