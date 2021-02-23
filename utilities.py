import time
import glob
import os.path
import re
import subprocess
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from parametricos import PATHAFSA, PATHGOLES, DURACION
from models import db, Videos
from datetime import datetime

def insertar_video(video, inicio, duracion, goleador, asistente):
    if goleador=='':
        goleador=0
        asistente=0
    try:
        v = Videos(origen=video, inicio=inicio, duracion=duracion, date=datetime.utcnow(), id_destacado=goleador, id_asistente=asistente)
        db.session.add(v)
        db.session.commit()
    except:
        raise Exception('Error al guardar en la base de datos.') 

def video_unedited():
    videos = glob.glob(os.path.join(PATHAFSA, '*[0-9].mp4'))
    for video in videos:
        if re.search(r'\d{4}\d{2}\d{2}\.mp4', video):
            nombre = video.split('\\')
            fecha = nombre[1].split('.')
            return fecha[0]
    raise Exception('No se encuentra el video sin editar.')

def convertirHora(segundos):
    return time.strftime('%H:%M:%S', time.gmtime(int(segundos)))

def listarPartidos():
    c=0
    listado = [(0, 'Indefinido')]
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

def definirParametrosDestacado(juego, minuto, segundo, goleador, asistente):
    print ('entro a destacado utility')
    partido = str(juego)
    entrada = PATHAFSA+partido+'.mp4'
    salida = PATHGOLES+partido+'-Destacado'+siguienteDestacado(juego)+'.mp4'
    final = (int(minuto) * 60) + int(segundo)
    inicio = final - DURACION
    try:
        if verificar_duplicacion(entrada, inicio, DURACION):
            return 'YA FUE CREADO UN VIDEO CON ESTOS PARAMETROS!!'
        else:
            cortarVideo(entrada, salida, inicio, DURACION)
            insertar_video(entrada, inicio, DURACION, goleador, asistente)
    except Exception as e:
        return 'DESTACADO ERROR!!: ' + str(e)
    return 'VIDEO CREADO: '+salida+' ('+str(obtenerDuracionVideo(salida))+' segs.)'

def cortarVideo(entrada, salida, inicio, fin):
    comando_corte = 'ffmpeg -loglevel error -y -ss ' + convertirHora(inicio) + \
                        ' -i ' + entrada + ' -t ' + convertirHora(fin) + ' -c copy ' + \
                        salida
    subprocess.call(comando_corte, shell=True)

def definirParametrosPartido(inicio, final):
    partido = 'Partido'+siguientePartido()
    try:
        VIDEO_COMPLETO = video_unedited()
    except Exception as e:
        return 'PARTIDO ERROR!!: ' + str(e)
    origen = os.path.join(PATHAFSA, VIDEO_COMPLETO+'.mp4')
    salida = PATHAFSA+VIDEO_COMPLETO+'-'+partido+'.mp4'
    desde = (int(inicio[0]) * 3600) + (int(inicio[1]) * 60) + int(inicio[2])
    hasta = (int(final[0]) * 3600) + (int(final[1]) * 60) + int(final[2])
    duracion = hasta - desde
    try:
        if verificar_duplicacion(origen, desde, duracion):
            return 'YA FUE CREADO UN VIDEO CON ESTOS PARAMETROS!!'
        else:
            cortarVideo (origen, salida, desde, duracion)
    except Exception as e:
        return 'PARTIDO ERROR!!: ' + str(e)
    return 'VIDEO CREADO: '+salida+' ('+str(obtenerDuracionVideo(salida))+' segs.)'

def verificar_duplicacion(origen, inicio, duracion):
    print ('entro a destacado utility')
    existe = Videos.query.get((origen, inicio, duracion))
    if existe:
        return True
    return False
