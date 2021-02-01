import time
import glob
import os.path
import re
import subprocess
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pathlib import Path

# PARAMETRICO
EXTENSION = '.mp4'
PATHAFSA = './AFSA/'
PATHGOLES = PATHAFSA + 'DESTACADOS/'
PATHTEMP = PATHGOLES + 'temporary.mp4'
DURACION = 10

def convertirHora(segundos):
    return time.strftime('%H:%M:%S', time.gmtime(int(segundos)))

def listarPartidos():
    c=0
    listado = [(0, 'Indefinido')]
    # dir = PATHAFSA
    videos = glob.glob(os.path.join(PATHAFSA, 'Partido*.mp4'))
    for nombre in videos:
        archivo = nombre.split('\\')
        video = archivo[1].split('.')
        c+=1
        item = (c, video[0])
        listado.append(item)
    return listado

def obtenerDuracionVideo(video):
    if video:
        clip = VideoFileClip(video)
        return clip.duration
    return 0

def siguienteDestacado(juego):
    videos = glob.glob(os.path.join(PATHGOLES, 'Partido'+str(juego)+'*.mp4'))
    return str(len(videos)+1)

def siguientePartido():
    videos = glob.glob(os.path.join(PATHAFSA, 'Partido*.mp4'))
    return str(len(videos)+1)

def definirParametrosDestacado(juego, minuto, segundo):
    partido = 'Partido'+juego
    entrada = PATHAFSA+partido+'.mp4'
    salida = PATHGOLES+partido+'-Destacado'+siguienteDestacado(juego)+'.mp4'
    final = (int(minuto) * 60) + int(segundo)
    inicio = final - DURACION
    try:
        cortarVideo (entrada, salida, inicio, final)
    except Exception as e:
        return 'ERROR!! Al compilar: ' + str(e)
    return 'VIDEO CREADO: '+salida+' ('+str(obtenerDuracionVideo(salida))+' segs.)'

def cortarVideo(entrada, salida, inicio, fin):
    # print(entrada, salida, inicio, fin)
    ffmpeg_extract_subclip(entrada, inicio, fin, targetname=salida)

def verificarDirectorios():
    Path(PATHAFSA).mkdir(parents=True, exist_ok=True)
    Path(PATHGOLES).mkdir(parents=True, exist_ok=True)

def definirParametrosPartido(inicio, final):
    partido = 'Partido'+siguientePartido()
    entrada = PATHAFSA+'output.mp4'
    salida = PATHAFSA+partido+'.mp4'
    desde = (int(inicio[0]) * 3600) + (int(inicio[1]) * 60) + int(inicio[2])
    hasta = (int(final[0]) * 3600) + (int(final[1]) * 60) + int(final[2])
    try:
        cortarVideo (entrada, salida, desde, hasta)
    except Exception as e:
        return 'ERROR!! Al compilar: ' + str(e)
    return 'VIDEO CREADO: '+salida+' ('+str(obtenerDuracionVideo(salida))+' segs.)'
