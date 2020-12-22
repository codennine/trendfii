import base64, json
from scripts.plantao_b3_v2 import list_news
from datetime import datetime
from scripts.mailer import send_mail
from datetime import datetime, timedelta

def search_fii_reports(event, context):
  import pytz, re
  # PubSub event ->  {'@type': 'type.googleapis.com/google.pubsub.v1.PubsubMessage', 'attributes': None, 'data': 'eyJzdG9ja3MiOiBbIkFCQ1AiXX0='}
  today = datetime.utcnow().replace(tzinfo=pytz.timezone('America/Sao_Paulo')) - timedelta(hours=3)
  find_date = today.strftime('%Y-%m-%d')
  data = json.loads(base64.b64decode(event['data']).decode('utf-8'))
  news = list_news(start_date=find_date, end_date=find_date)
  print('event.data')
  print(data)
  expression = '|'.join(data['stocks'])
  content = '<ul>'
  # {'IdAgencia': 18, 'content': None, 'dateTime': '2020-12-14 09:10:30', 'headline': 'FII OURI FOF (OUFF) Informe Mensal - 11/2020', 'id': 1319258, 'view_doc': 'https://fnet.bmfbovespa.com.br/fnet/publico/exibirDocumento?id=1319258'}
  for new in news:
    if len(re.findall(expression, new['headline'])) == 0:
      continue
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

  subject = 'Plantão de FIIs - {formatted_today}'.format_map({'formatted_today': today.strftime('%d/%m/%Y')})
  print(news)
  print(subject)
  
  send_mail('projetoscodesilva@gmail.com', 'edigleyssonsilva@gmail.com', subject, message, 'Edigleysson Silva')

  return 'reading reports fro PLANTAO'