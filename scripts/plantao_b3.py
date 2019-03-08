#coding=utf8
import requests
from bs4 import BeautifulSoup


URL_FII = 'http://www2.bmfbovespa.com.br/Agencia-Noticias/ListarNoticias.aspx?idioma=pt-br&q=fii&tipoFiltro=3&periodoDe=2019-03-07&periodoAte=2019-03-07&pg='
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
	print(len(k))
	total = total - len(k)



# 

# print(links_noticias)
# print(k)
# print(k == links_noticias)
