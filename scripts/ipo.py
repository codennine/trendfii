#coding=utf8
import requests
from bs4 import BeautifulSoup


# URL_IPO = 'http://www.b3.com.br/pt_br/produtos-e-servicos/solucoes-para-emissores/ofertas-publicas/ofertas-em-andamento/'
URL_IPO = 'http://www.bmfbovespa.com.br/pt_br/servicos/ofertas-publicas/ofertas-em-andamento/'

CATEGORIA_ACAO = '8A828D294E3198DA014E645F573C7152'
CATEGORIA_FUNDOS = '8A828D294E3198DA014E645F32F37128'
CATEGORIA_OUTROS_EMISSORES = '8A828D294E3198DA014E645F9060717C'
 
#CAT = CATEGORIA_OUTROS_EMISSORES
CAT = CATEGORIA_FUNDOS

post_data = {
	'lumNewParams': '<parameters destId="8A6A8C244DD3046D014DD37C86E83402" destType="lumII"><p n="lumFromForm">Form_8A6A8C244DD3046D014DD37C86E83402</p><p n="lumFormAction">http://www.b3.com.br/main.jsp?lumPageId=8A6A8C244DB963B9014DB9C68F3D02A8&amp;lumA=1&amp;lumII=8A6A8C244DD3046D014DD37C86E83402</p><p n="doui_renderAction">filter</p><p n="doui_fromForm">Form_8A6A8C244DD3046D014DD37C86E83402</p><p n="doui_storedValues">doui_SourceParameter.default.category=8A828D294E3198DA014E645F32F37128;doui_SourceParameter.default.status=1</p><p n="lumII">8A6A8C244DD3046D014DD37C86E83402</p><p n="filters.category.value">'+ CAT +'</p><p n="filters.status.value">1</p><p n="bvmf-locales-content">pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,</p></parameters>',
	'lumPrinting': '',
	'lumToggleModeOriginUrl': '',
	'lumSafeRenderMode': '',
	'lumPageOriginalUrl': 'main.jsp?lumPageId=8A6A8C244DB963B9014DB9C68F3D02A8',
	'lumS': '',
	'lumSI': '',
	'lumI': '',
	'lumII': '8A6A8C244DD3046D014DD37C86E83402',
	'lumReplIntfState': '',
	'lumPrevParams': '<allParameters><parameters destType="lumII" destId="8A6A8C244DD3046D014DD37C86E83402"><p n="lumFromForm">Form_8A6A8C244DD3046D014DD37C86E83402</p><p n="filters.category.value">8A828D294E3198DA014E645F32F37128</p><p n="lumFormAction">http://www.b3.com.br/main.jsp?lumPageId=8A6A8C244DB963B9014DB9C68F3D02A8&amp;lumA=1&amp;lumII=8A6A8C244DD3046D014DD37C86E83402</p><p n="doui_renderAction">filter</p><p n="doui_fromForm">Form_8A6A8C244DD3046D014DD37C86E83402</p><p n="bvmf-locales-content">pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,pt_BR,</p><p n="lumII">8A6A8C244DD3046D014DD37C86E83402</p><p n="doui_storedValues">doui_SourceParameter.default.status=1</p><p n="filters.status.value">1</p></parameters><parameters></parameters></allParameters>',
	'lumA': '',
	'lumDataPreviewMode': '',
	'lumClientMessage': ''
}


page = requests.post(URL_IPO, data=post_data)
soup = BeautifulSoup(page.content, 'html.parser')

ipos = list(map(
		lambda a: {'link': 'http://www.b3.com.br/' + a['href'].replace('../', ''), 'texto': a.text}, 
		[row.find('a') for row in soup.find_all('div', {'class': 'list-avatar-row'})]
))

print(ipos)

