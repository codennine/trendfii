#coding=utf8
import requests
from bs4 import BeautifulSoup
from google.cloud import firestore

def ifix(event):
	DB = firestore.Client.from_service_account_json('Projetos-Web-fea153234a67.json')
	ifix_collection = DB.collection('ifix')


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
		cod = td[0].text
		part = float(td[4].text.replace(',', '.'))

		doc_ref = ifix_collection.document(cod)
		doc_ref.set({'part': part})

		# ifix_collection.add({u'cod': cod})

		# ifix_collection.document(cod).set({
		# 	'participacao': part
		# })

		table.append([td[0].text, float(td[4].text.replace(',', '.'))])
		soma += float(td[4].text.replace(',', '.'))

	print('\n')
	print(table)
	print('\n')

	resp = 'SOMA TOTAL: %.2f%%'%(soma)

	print(resp)
	return resp




