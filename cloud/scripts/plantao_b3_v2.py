import requests, time
from bs4 import BeautifulSoup
from datetime import datetime

def find_docs_news(news):
  for new in news:
    r = requests.get(new['view_doc'])
    content_type = r.headers['Content-Type']

def list_news(start_date='2020-12-14', end_date='2020-12-14'):
  import sys
  import re
  import json

  URL = 'https://sistemasweb.b3.com.br/PlantaoNoticias/Noticias/ListarTitulosNoticias?agencia=18&palavra={q}&dataInicial={start_date}&dataFinal={end_date}'.format_map({
    'start_date': start_date,
    'end_date': end_date,
    'q': 'fii'
  })
  URL_VIEWER = 'https://fnet.bmfbovespa.com.br/fnet/publico/exibirDocumento?id='
  URL_DETAIL = 'https://sistemasweb.b3.com.br/PlantaoNoticias/Noticias/Detail?idNoticia=1327214&agencia=18&dataNoticia=2020-12-18%2019:40:06'

  page = requests.get(URL, verify=False)
  items = [x['NwsMsg'] for x in json.loads(page.content) if not '(C)' in x['NwsMsg']['headline']]
  for item in items:
    if '(C)' in str(item['headline']).upper():
      continue
    item['view_doc'] = URL_VIEWER + str(item['id'])

  return items


if __name__ == '__main__':
  print('Loading....')
  today = datetime.utcnow().strftime('%Y-%m-%d')
  print(today)
  start = time.time()
  find_docs_news(list_news(start_date='2020-12-14', end_date=today))
  end = time.time()

  print('-'*50)
  print('Execution time: %f'%((end-start)))