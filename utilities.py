import time

def convertirHora(segundos):
    return time.strftime('%H:%M:%S', time.gmtime(int(segundos)))

# PARAMETRICO
EXTENSION = '.mp4'
PATHAFSA = './AFSA/'
PATHGOLES = PATHAFSA + 'Goles/'
PATHTEMP = PATHGOLES + 'temporary.mp4'