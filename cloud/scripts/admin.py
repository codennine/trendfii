import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('codesilva-blog-firebase-adminsdk-61qwi-cc13c2227e.json')
default_app = firebase_admin.initialize_app(cred)