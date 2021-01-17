@echo off
set LOGFILE=batch.log
call :LOG > %LOGFILE%
exit /B

:LOG

@echo %DATE% %TIME% INICIO_PROCESO
(for %%i in (*.mp4) do @echo file '%%i') > mylist.txt
ffmpeg -f concat -i mylist.txt -vf scale=1280:720 -preset fast output.mp4
del mylist.txt
@echo %DATE% %TIME% FINALIZO_PROCESO