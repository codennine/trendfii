#coding=utf-8
import os 
from bs4 import BeautifulSoup

files = []

gestores = {
    'EDY11': {'fiis': [], 'vacancia':0}
}

for r,d,f in os.walk('../gestores_ifix'):
    for file in f:
        handle = open(os.path.join(r, file), 'r')
        html = handle.read()
        soup = BeautifulSoup(html, 'html.parser')
        handle.close()
        gestor = u'%s'%(soup.find('div').text)
        print(gestor)

        if(not gestor in gestores):
            gestores[gestor] = {
                'fiis': [],
                'vacancia': 0
            }
        gestores[gestor]['fiis'].append(file.replace('.html', ''))
           
        files.append(file)

print(gestores)