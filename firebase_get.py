#Pegar dados da nuvem
#Inseri no banco local
#Admim

import pyrebase

Config = {
    "apiKey": "AIzaSyCoehDyB7CxJqcqT25oWb0r8M6LVhCuLF0",
    "authDomain": "systemprojet-65aae.firebaseapp.com",
    "projectId": "systemprojet-65aae",
    "storageBucket": "systemprojet-65aae.appspot.com",
    "messagingSenderId": "986551460631",
    "databaseURL": "https://systemprojet-65aae-default-rtdb.firebaseio.com/" ,
    "appId": "1:986551460631:web:eb52e97215b08adea08d52",
    "measurementId": "G-4T3KZ57PF1"
}

firebase = pyrebase.initialize_app(Config)
dados = firebase.database()

res = dados.child("chave").get()

print(res.val())
