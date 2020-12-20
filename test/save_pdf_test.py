def save_pdf_from_web():
  import requests, base64

  # Retorna o conteúdo do pdf em base64
  url = 'https://fnet.bmfbovespa.com.br/fnet/publico/exibirDocumento?id=134344'
  r = requests.get(url, stream=True)

  content_type = r.headers['Content-Type']

  if content_type == 'application/pdf':
    with open('134344.pdf', 'wb') as fd:
      pdf_content = base64.b64decode(r.content)
      fd.write(pdf_content)



if __name__ == '__main__':
  save_pdf_from_web()