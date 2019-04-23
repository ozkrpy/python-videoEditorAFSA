"# python-videoEditorAFSA" 

Video editor para extraer goles de grabaciones de partidos jugados en las fechas AFSA.
PARAMETROS
Los archivos se deben nombrar "PartidoX.mp4".
Se deben depositar en la misma carpeta, y una vez descargados a la misma se debe modificar la aplicacion python para que el PATH "pathAFSA", sea el mismo que la carpeta donde se encuentran los videos.
Ejecutar la aplicacion python desde un terminal, con lo que se inicializara el servidor Bubble y escuchara en la direccion "http://localhost:8080/home.html".
El sitio toma el numero de partido y compila esto para buscarlo en la carpeta marcada para el pathAFSA, se debe indicar el momento donde finaliza la jugada "Minuto" y "Segundo" correspondiente, en caso de ser un gol la grabacion no durara mas de diez segundos, si es un palo durara seis segundos.
Se pueden seleccionar los nombres de jugador y asistente, con esto se generara un archivo de texto que indicara los datos de 
* PARTIDO
* ASISTENTE   
* GOLEADOR    
* OBSERVACION: Que indica numero de gol, minuto y segundo segun el partido.
Una vez procesado el clip, se mostrara el resultado obtenido y la opcion de volver a realizar el mismo proceso.