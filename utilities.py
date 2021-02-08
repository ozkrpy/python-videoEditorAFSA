import time
import glob
import os.path
import re
import subprocess
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from parametricos import PATHAFSA, PATHGOLES, DURACION, VIDEO_COMPLETO
from models import db, Videos
from datetime import datetime


def convertirHora(segundos):
    return time.strftime('%H:%M:%S', time.gmtime(int(segundos)))

def listarPartidos():
    c=0
    listado = [(0, 'Indefinido')]
    # dir = PATHAFSA
    videos = glob.glob(os.path.join(PATHAFSA, '*Partido*.mp4'))
    for nombre in videos:
        archivo = nombre.split('\\')
        video = archivo[1].split('.')
        c+=1
        item = (video[0], video[0])
        listado.append(item)
    return listado

def obtenerDuracionVideo(video):
    if video:
        clip = VideoFileClip(video)
        return clip.duration
    return 0

def siguienteDestacado(juego):
    videos = glob.glob(os.path.join(PATHGOLES, '*'+str(juego)+'*.mp4'))
    return str(len(videos)+1)

def siguientePartido():
    videos = glob.glob(os.path.join(PATHAFSA, '*Partido*.mp4'))
    return str(len(videos)+1)

def definirParametrosDestacado(juego, minuto, segundo):
    partido = juego
    entrada = PATHAFSA+partido+'.mp4'
    salida = PATHGOLES+partido+'-Destacado'+siguienteDestacado(juego)+'.mp4'
    final = (int(minuto) * 60) + int(segundo)
    inicio = final - DURACION
    try:
        if verificar_duplicacion(entrada, inicio, DURACION):
            return 'YA FUE CREADO UN VIDEO CON ESTOS PARAMETROS!!'
        else:
            cortarVideo (entrada, salida, inicio, DURACION)
    except Exception as e:
        return 'ERROR!! Al compilar: ' + str(e)
    return 'VIDEO CREADO: '+salida+' ('+str(obtenerDuracionVideo(salida))+' segs.)'

def cortarVideo(entrada, salida, inicio, fin):
    # print(entrada, salida, inicio, fin)
    # ffmpeg_extract_subclip(entrada, inicio, fin, targetname=salida)
    comando_corte = 'ffmpeg -loglevel error -y -ss ' + convertirHora(inicio) + \
                        ' -i ' + entrada + ' -t ' + convertirHora(fin) + ' -c copy ' + \
                        salida
    subprocess.call(comando_corte, shell=True)

def definirParametrosPartido(inicio, final):
    partido = 'Partido'+siguientePartido()
    origen = os.path.join(PATHAFSA, VIDEO_COMPLETO+'.mp4')
    nombre_lista = origen.split('/')
    nombre_video = nombre_lista[2].split('.')
    # entrada = PATHAFSA+'output.mp4'
    # salida = PATHAFSA+datetime.utcnow().strftime('%Y%m%d')+'-'+partido+'.mp4'
    salida = PATHAFSA+nombre_video[0]+'-'+partido+'.mp4'
    desde = (int(inicio[0]) * 3600) + (int(inicio[1]) * 60) + int(inicio[2])
    hasta = (int(final[0]) * 3600) + (int(final[1]) * 60) + int(final[2])
    duracion = hasta - desde
    try:
        if verificar_duplicacion(origen, desde, duracion):
            return 'YA FUE CREADO UN VIDEO CON ESTOS PARAMETROS!!'
        else:
            cortarVideo (origen, salida, desde, duracion)
    except Exception as e:
        return 'ERROR!! Al compilar: ' + str(e)
    return 'VIDEO CREADO: '+salida+' ('+str(obtenerDuracionVideo(salida))+' segs.)'

def verificar_duplicacion(origen, inicio, duracion):
    existe = Videos.query.get((origen, inicio, duracion))
    if existe:
        return True
    v = Videos(origen=origen, inicio=inicio, duracion=duracion, date=datetime.utcnow())
    db.session.add(v)
    db.session.commit()
    return False

