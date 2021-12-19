import os
from pathlib import Path
import shutil
# chegar na pasta area de trabalho
desktop = r'C:\Users\Victor\Desktop'
os.chdir(desktop)

# ler os arquivos da pasta
caminho = Path(desktop)
pastapdf = r"C:\Users\Victor\Desktop\pdf's"
pastacdr = r"C:\Users\Victor\Desktop\corel's"
pastapng = r"C:\Users\Victor\Desktop\png's"
arquivos = os.listdir(desktop)


# verificar a extensão dos arquivos
for nomearquivo in caminho.glob('*'):
    extensao = nomearquivo.suffix
    for arquivo in arquivos:
        if extensao == '.pdf':
            shutil.move(caminho+arquivo, pastapdf)
            print('Arquivo pdf movido')
        elif extensao == '.cdr':
            shutil.move(caminho+arquivo, pastacdr)
            print('arquivo .cdr')
        elif extensao == '.png' or '.PNG' or '.jpg' or '.JPG':
            shutil.move(caminho+arquivo, pastapng)
            print('arquivo .jpg ou .png')
# mover os arquivos de cada extensão pra pasta definida