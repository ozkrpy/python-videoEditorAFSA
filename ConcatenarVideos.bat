@echo INICIO_PROCESO
(for %%i in (*.mp4) do @echo file '%%i') > mylist.txt
ffmpeg -f concat -i mylist.txt -c copy output.mp4
del mylist.txt
@echo FINALIZO_PROCESO