@echo off

set directorio=%1
set salida=%2
cd %directorio%
@echo %DATE% %TIME% INICIO_PROCESO
(for %%i in (*.mp4) do @echo file '%%i') > mylist.txt
ffmpeg -f concat -i mylist.txt -vf scale=1280:720 -preset fast %salida%
del mylist.txt
@echo %DATE% %TIME% FINALIZO_PROCESO


@REM .\ConcatenarVideos.bat .\AFSA\DESTACADOS\ resumen.mp4
@REM .\ConcatenarVideos.bat .\AFSA\ output.mp4