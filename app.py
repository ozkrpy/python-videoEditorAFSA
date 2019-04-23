import fnmatch
import os

from bottle import route, run, post, request, static_file
#from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./')

@route('/')
def server_static(filepath="index.html"):
    return static_file(filepath, root='./')

@post('/procesarVideo')
def process():

    pathAFSA = 'C:\\Users\\ruffineo\\Desktop\\TEMPORAL-PCSISOP\\Multimedia\\AFSA\\'
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
            if os.path.exists(pathAFSA + 'Partido' + numero_partido + '-Gol1' + extension):
                numero = len(fnmatch.filter(
                    os.listdir(), 'Partido' + numero_partido + '-Gol*')) + 1
        else:
            if os.path.exists(pathAFSA + 'Partido' + numero_partido + '-Palo1' + extension):
                numero = len(fnmatch.filter(
                    os.listdir(), 'Partido' + numero_partido + '-Palo*')) + 1  
        return numero
    
    def calcularDuracion():
        if (tipo == 'palo'):
            return 6
        return 10
    
    # PARAMETRICO
    extension = '.mp4'

    #DEFINIR ARCHIVO DEL PARTIDO COMPLETO
    nombre_archivo_origen = pathAFSA + 'Partido' + numero_partido

    #DEFINIR TIEMPO INICIO Y TIEMPO FIN
    tiempo_fin = (int(minuto) * 60) + int(segundo)
    tiempo_inicio = tiempo_fin - calcularDuracion()
    
    #DEFINIR NUMERO DE ARCHIVO A EJECUTAR
    numero_archivo_crear = obtienesiguientenumeroarchivo()
    if (tipo == 'gol'):
        nombre_archivo_salida = nombre_archivo_origen + '-Gol%s' % numero_archivo_crear + extension
        if (len(segundo)==1):
            texto_segundo = '0' + segundo
        else:
            texto_segundo = segundo
        observacion = 'Gol%s' % numero_archivo_crear + ' Minuto: ' + minuto + ':' + texto_segundo
        clipboard = numero_partido + "\t" + asistente + "\t" + jugador + "\t" + observacion + '\n'
    else:
        nombre_archivo_salida = nombre_archivo_origen + '-Palo%s' % numero_archivo_crear + extension
    
    try:
        clip = ffmpeg_extract_subclip(nombre_archivo_origen + extension, tiempo_inicio, tiempo_fin, nombre_archivo_salida)
    except Exception as e:
        return 'Error al compilar el video: ' + str(e)

    try:
        if (tipo == 'gol'):
            pathname = os.path.join("ResumenFecha.txt")
            resumen = open(pathname, 'a+', encoding='utf-8')
            resumen.write(clipboard)
            resumen.close()
    except Exception as e:
        print('Error al guardar el archivo: ' + str(e))

    return '<h3>PROCESADO CON EXITO</h3><strong>Tipo:</strong> {0}{5} <strong>Partido:</strong> {1} <strong>Tiempo:</strong> {2}:{3} <strong>Jugador:</strong> {4} <strong>LISTO!</strong><br><br><input type="button" value="Crear otro clip!" onclick="history.back(-1)"/>'.format(tipo, numero_partido, minuto, segundo, jugador, numero_archivo_crear)

run(host='localhost', port=8080, debug=True)