import time
import glob
import os.path
import re
import subprocess
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# PARAMETRICO
EXTENSION = '.mp4'
PATHAFSA = './AFSA/'
PATHGOLES = PATHAFSA + 'DESTACADOS/'
PATHTEMP = PATHGOLES + 'temporary.mp4'
DURACION = 10
project_dir = os.path.dirname(os.path.abspath(__file__))
video_dir = os.path.join(project_dir, PATHAFSA)
    

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

def obtenerDuracionVideo(juego):
    if juego!='0':
        partido = PATHAFSA+'Partido'+juego+'.mp4'
        clip = VideoFileClip(partido)
        return clip.duration
    return 0

def siguienteDestacado(juego):
    videos = glob.glob(os.path.join(PATHGOLES, 'Partido'+str(juego)+'*.mp4'))
    print(len(videos))
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
        return 'Error al compilar el video: ' + str(e)
    return salida

def cortarVideo(entrada, salida, inicio, fin):
    print(entrada, salida, inicio, fin)
    try:
        ffmpeg_extract_subclip(entrada, inicio, fin, targetname=salida)
    except Exception as e:
        return str(e)
