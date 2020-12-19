import base64

def search_fii_reports(event, context):
  print('testando fução acionada via topico')
  data = base64.b64decode(event['data']).decode('utf-8')
  print(data)
  print('\n\n\n')
  return 'reading reports fro PLANTAO'