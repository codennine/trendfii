import base64
from scripts.plantao_b3_v2 import list_news

def search_fii_reports(event, context):
  # PubSub event ->  {'@type': 'type.googleapis.com/google.pubsub.v1.PubsubMessage', 'attributes': None, 'data': 'eyJzdG9ja3MiOiBbIkFCQ1AiXX0='}
  print('testando fução acionada via pubsub')
  data = base64.b64decode(event['data']).decode('utf-8')
  print(data)
  print('news')
  print(list_news())
  return 'reading reports fro PLANTAO'