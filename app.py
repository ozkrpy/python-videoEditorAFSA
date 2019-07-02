import fnmatch
import os
import subprocess
import time

from bottle import post, request, route, run, static_file
#from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# PARAMETRICO
extension = '.mp4'
# pathAFSA = 'C:\\Users\\ruffineo\\Desktop\\TEMPORAL-PCSISOP\\Multimedia\\AFSA\\'
pathAFSA = 'C:\\Users\\ozkrp\\Desktop\\FORMATEO\\AFSA\\'
pathGoles = pathAFSA + 'Goles\\'
pathTemp = pathGoles + 'temporary.mp4'


def convertirHora(segundos):
    return time.strftime('%H:%M:%S', time.gmtime(int(segundos)))


@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./')


@route('/')
def server_static(filepath="home.html"):
    return static_file(filepath, root='./')


@post('/procesarGol')
def process():
    try:
        partido = request.forms.get('partido')
        numero_partido = str(partido)
        minuto = request.forms.get('minuto')
        segundo = request.forms.get('segundo')
        jugador = request.forms.get('jugador')
        tipo = request.forms.get('tipo')
        asistente = request.forms.get('asistente')
    except:
        return 'Error al obtener los datos de entrada'

    def obtienesiguientenumeroarchivo():
        numero = 1
        if (tipo == 'gol'):
            if os.path.exists(pathGoles + numero_partido + '-Gol1' + extension):
                numero = len(fnmatch.filter(
                    os.listdir(pathGoles), numero_partido + '-Gol*')) + 1
        else:
            if os.path.exists(pathAFSA + 'Partido' + numero_partido + '-Palo1' + extension):
                numero = len(fnmatch.filter(
                    os.listdir(pathAFSA), 'Partido' + numero_partido + '-Palo*')) + 1
        return numero

    def calcularDuracion():
        if (tipo == 'palo'):
            return 6
        return 10

    def calcularDuracionCadena():
        if (tipo == 'palo'):
            return '00:00:06'
        return '00:00:10'

    # DEFINIR ARCHIVO DEL PARTIDO COMPLETO
    nombre_archivo_origen = pathAFSA + 'Partido' + numero_partido

    # DEFINIR TIEMPO INICIO Y TIEMPO FIN
    tiempo_fin = (int(minuto) * 60) + int(segundo)
    tiempo_inicio = tiempo_fin - calcularDuracion()
    segundos_entrada_inicio = convertirHora(tiempo_inicio)

    # DEFINIR NUMERO DE ARCHIVO A EJECUTAR
    numero_archivo_crear = obtienesiguientenumeroarchivo()
    if (tipo == 'gol'):
        nombre_archivo_salida = pathGoles + numero_partido + \
            '-Gol%s' % numero_archivo_crear + extension
        if (len(segundo) == 1):
            texto_segundo = '0' + segundo
        else:
            texto_segundo = segundo
        observacion = 'Gol%s' % numero_archivo_crear + \
            ' Minuto: ' + minuto + ':' + texto_segundo
        clipboard = numero_partido + "\t" + asistente + \
            "\t" + jugador + "\t" + observacion + '\n'
    else:
        nombre_archivo_salida = nombre_archivo_origen + \
            '-Palo%s' % numero_archivo_crear + extension

    try:
        comando_corte = 'ffmpeg  -y -ss ' + segundos_entrada_inicio + \
                        ' -i ' + nombre_archivo_origen + extension + ' -t ' + calcularDuracionCadena() + ' -c copy ' + \
                        pathTemp
        subprocess.call(comando_corte, shell=True)
    except Exception as e:
        return 'Error al compilar el video: ' + str(e)

    try:
        cadena_gol = asistente + '/' + jugador
        comando_autor = 'ffmpeg -threads 4 -i ' + pathTemp + ' -vf ' + \
                        '"drawtext=fontfile=/Windows/Fonts/candara.ttf: text=' + cadena_gol + \
                        ': fix_bounds=1: fontcolor=white: fontsize=100: bordercolor=black: borderw=1: x=20: y=main_h-line_h-20: shadowcolor=white:" -preset ultrafast ' + \
                        nombre_archivo_salida + '"'
        subprocess.call(comando_autor, shell=True)
        os.remove(pathTemp)
    except Exception as e:
        return 'Error al agregar texto al video: ' + str(e)

    try:
        if (tipo == 'gol'):
            pathname = os.path.join(pathAFSA, "ResumenFecha.txt")
            resumen = open(pathname, 'a+', encoding='utf-8')
            resumen.write(clipboard)
            resumen.close()
    except Exception as e:
        print('Error al guardar el archivo: ' + str(e))

    return '<h3>PROCESADO CON EXITO</h3><strong>Tipo:</strong> {0}{5} <strong>Partido:</strong> {1} <strong>Tiempo:</strong> {2}:{3} <strong>Jugador:</strong> {4} <strong>LISTO!</strong><br><br><input type="button" value="Crear otro clip!" onclick="history.back(-1)"/>'.format(tipo, numero_partido, minuto, segundo, jugador, numero_archivo_crear)


@post('/procesarPartido')
def process():
    try:
        tiempo_inicio_hora = request.forms.get('hora_inicio')
        tiempo_inicio_minuto = request.forms.get('minuto_inicio')
        tiempo_inicio_segundo = request.forms.get('segundo_inicio')
        tiempo_fin_hora = request.forms.get('hora_fin')
        tiempo_fin_minuto = request.forms.get('minuto_fin')
        tiempo_fin_segundo = request.forms.get('segundo_fin')
    except:
        return 'Error al obtener los datos de entrada'

    tiempo_game_inicio = (int(tiempo_inicio_hora) * 3600) + \
        (int(tiempo_inicio_minuto) * 60) + int(tiempo_inicio_segundo)
    partido_inicio = convertirHora(tiempo_game_inicio)
    tiempo_game_fin = (int(tiempo_fin_hora) * 3600) + \
        (int(tiempo_fin_minuto) * 60) + int(tiempo_fin_segundo)
    duracion = tiempo_game_fin - tiempo_game_inicio
    partido_fin = convertirHora(duracion)

    def obtienesiguientenumeroarchivo():
        numero = 1
        if os.path.exists(pathAFSA + 'Partido1' + extension):
            numero = len(fnmatch.filter(
                os.listdir(pathAFSA), 'Partido*')) + 1
        return numero

    numero_game = obtienesiguientenumeroarchivo()
    try:
        # ffmpeg_extract_subclip(pathAFSA + 'output' + extension, tiempo_game_inicio, tiempo_game_fin, pathAFSA + 'Partido' + str(numero_game) + extension)
        comando_corte = 'ffmpeg -threads 4 -ss ' + partido_inicio + \
                        ' -i ' + pathAFSA + 'output' + extension + ' -t ' + partido_fin + ' -c copy ' + \
                        pathAFSA + 'Partido' + str(numero_game) + extension
        print(comando_corte)
        subprocess.call(comando_corte, shell=True)
    except Exception as e:
        return 'Error al compilar el video: ' + str(e)

    return '<h3>PROCESADO CON EXITO</h3><strong>Se creo el Partido: </strong>{0}<br><br><input type="button" value="Crear otro clip!" onclick="history.back(-1)"/>'.format(numero_game)


run(host='localhost', port=8000, debug=True)
