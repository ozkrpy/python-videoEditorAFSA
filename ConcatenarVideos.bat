@echo off
set LOGFILE=batch.log
call :LOG > %LOGFILE%
exit /B

:LOG

@echo %DATE% %TIME% INICIO_PROCESO
(for %%i in (*.mp4) do @echo file '%%i') > mylist.txt
@REM ffmpeg -f concat -i mylist.txt -vf scale=1280:720 -preset fast output.mp4
ffmpeg -f concat -i mylist.txt -vcodec libx264 -s 1280x720 -b 1750k -acodec libmp3lame -ac 2 -ab 160k -threads 4 output_file.mp4
del mylist.txt
@echo %DATE% %TIME% FINALIZO_PROCESO