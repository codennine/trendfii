import base64
from scripts.plantao_b3_v2 import list_news
from datetime import datetime

def search_fii_reports(event, context):
  # PubSub event ->  {'@type': 'type.googleapis.com/google.pubsub.v1.PubsubMessage', 'attributes': None, 'data': 'eyJzdG9ja3MiOiBbIkFCQ1AiXX0='}
  data = base64.b64decode(event['data']).decode('utf-8')
  news = list_news()
  today = datetime.utcnow()
  content = '<ul>'
  # {'IdAgencia': 18, 'content': None, 'dateTime': '2020-12-14 09:10:30', 'headline': 'FII OURI FOF (OUFF) Informe Mensal - 11/2020', 'id': 1319258, 'view_doc': 'https://fnet.bmfbovespa.com.br/fnet/publico/exibirDocumento?id=1319258'}
  for new in news:
    content += '<li><a href="{view_doc}">{headline}</a></li>'.format_map(new)
  content += '</ul>'

  message = '''\
    <html>
      <body>
        <h1>Plantão de FIIs - {formatted_today}</h1>
        {content}
        <footer style="text-align:center;">
          <p>Dados coletados do <a href="https://sistemasweb.b3.com.br/PlantaoNoticias/Noticias/Index?agencia=18">Plantão da B3</a></p>
        </footer>
      </body>
    </html>
  '''.format_map({
    'formatted_today': today.strftime('%d/%m/%Y'),
    'content': content
  })

  return 'reading reports fro PLANTAO'