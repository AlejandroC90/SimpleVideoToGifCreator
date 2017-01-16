#!/usr/bin/python
import os
import argparse #to use the arguments/para usar los argumentos
import subprocess #we need it to make a call to ffmpeg/ lo necesitamos para hacer un llamado a ffmpeg
import tempfile #to know the temp directory of the os / para saber en qué directorio guardar los archivos temporales

#CREATING ARGUMENTS FOR COMMAND LINE / SE CREAN LOS ARGUMENTOS PARA LA LINEA DE COMANDOS
parser = argparse.ArgumentParser(description='Script to create fast and high quality gif or swf files / Scripts para crear rapidamente archivos gif y swf')
parser.add_argument('video',help='The input video / El video de entrada')
parser.add_argument('-s','--swf',help='If the output is an swf / Si se desea un swf', action='store_true')
parser.add_argument('-sub','--subtitles',help='If you want the file with subtitles / Si se desean subtitulos', action='store_true')
parser.add_argument('tiempoini',help='Start time / Tiempo de Inicio')
parser.add_argument('duracion',help='Lenght / Duración ')
parser.add_argument('-f','--fps',default=12,help='Frames per second / Frames por segundo')
parser.add_argument('-t','--tama',default=500,help='Height size of the file / Tamaño de la altura del archivo')
parser.add_argument('sali',help='Filename to create without extension / Archivo a crear sin la extensión')
parser.add_argument('-c','--calidad', default=4,help='Quality only for swf files / Calidad sólo para archivos swf')
parser.add_argument('-tu','--tumblr', help = 'To apply the "tumblr effect", it uses imagemagick / Para aplicar el "efecto tumblr", hace uso de imagemagick', action='store_true')
#THESE THREE ARE NOT SET TO BE ABLE TO BE CONFIGURED YET / ESTAS TRES AUN NO SE PUEDEN CONFIGURAR
parser.add_argument('-fi','--filtro',default='lanczos',help='Flags')
parser.add_argument('-dit','--dither',default='bayer:bayer_scale=3',help='Dither')
parser.add_argument('-dif','--diff',default='lanczos',help='Difference')


args = parser.parse_args()



#WE FIND THE TEMP FOLDER TO CREATE THE RUTE TO THE PALETTE AND VIDEO FILE / ENCONTRAMOS LA RUTA TEMPORAL PARA CREAR LA PALETA Y EL VIDEO AHÍ
tempfolder = tempfile.gettempdir()

#LINUX PATH BY DEFAULT / LA RUTA DE LINUX POR DEFECTO
palette= tempfolder + "/palette.png"
video= tempfolder + "/usvideo.mp4"

#IF WE ARE IN WINDOWS / EN EL CASO DE WINDOWS
if os.name == 'nt':
    palette= tempfolder + "\palette.png"
    video= tempfolder + "\ideo.mp4"
    

#DEFAULT EXTENSION OF THE FILE / EXTENSION POR DEFAULT DEL ARCHIVO
ext = ".gif"

#IN THE CASE OF A SWF FILE / SI ES EL CASO PARA HACER UN SWF
if args.swf:
    ext = '.swf'
    if args.subtitulos:
        #IS THE SUBTITLE OPTION IS ENABLED WE CREATE THE SWF WITH THE SUBTITLES
        subprocess.call('ffmpeg -v error' + ' -i ' + '"' + args.video + '" ' + ' -ss ' + args.tiempoini + ' -t ' + args.duracion +  ' -qscale ' + str(args.calidad) + ' -vf' + ' fps=' + str(args.fps) + ',scale=' + str(args.tama) + ':-1' + ',subtitles=' + repr(repr(args.video)) + ' -an ' + args.sali + ext + ' -y', shell=True)

    else:
        subprocess.call('ffmpeg ' + ' -ss ' + args.tiempoini + ' -t ' + args.duracion + ' -i ' + '"' + args.video + '"' + ' -qscale ' + str(args.calidad) + ' -vf' + ' fps=' + str(args.fps) + ',scale=' + str(args.tama) + ':-1 ' + ' -an ' + args.sali + ext + ' -y', shell=True)
        
        
#IF IS NOT AND SWF THEN IT IS A GIF / SI NO ES UN SWF ENTONCES ES UN GIF
else:
    if args.subtitulos:
        #IS THE SUBTITLE OPTION IS ENABLED WE CREATE THE GIF WITH THE SUBTITLES BY CREATING A TEMPORARY VIDEO FILE AND THEN CREATING THE GIF FROM THE VIDEO
        subprocess.call('ffmpeg -v error -i ' + '"' + args.video + '"' + ' -ss ' + args.tiempoini + ' -t ' + args.duracion + ' -vf subtitles=' + repr(repr(args.video)) + ' -y ' + video , shell=True)
        subprocess.call('ffmpeg -v error ' + ' -i ' + '"' + video + '"' + ' -vf  "' + 'fps=' + str(args.fps) + ',scale=' + str(args.tama) + ':-1:flags=' + args.filtro + ',palettegen=stats_mode=diff" -y ' + palette , shell=True)
        subprocess.call('ffmpeg -v error ' + ' -i ' + video + ' -i ' + palette + ' -lavfi ' + '"fps=' + str(args.fps) + ',scale=' + str(args.tama) + ':-1:flags=' + args.filtro + ' [x]; [x][1:v] paletteuse=dither=' + args.dither + ':diff_mode=rectangle"' + ' -y ' + args.sali + ext , shell=True)
    else:
        subprocess.call('ffmpeg -v error -ss ' + args.tiempoini + ' -t ' + args.duracion + ' -i ' + '"' + args.video + '"' + ' -vf ' + '"fps=' + str(args.fps) + ',scale=' + str(args.tama) + ':-1:flags=' + args.filtro + ',palettegen=stats_mode=diff" -y ' + palette , shell=True)
        subprocess.call('ffmpeg -v error ' + ' -ss ' + args.tiempoini + ' -t ' + args.duracion + ' -i ' + '"' + args.video + '"' + ' -i ' + palette + ' -lavfi ' + '"fps=' + str(args.fps) + ',scale=' + str(args.tama) + ':-1:flags=' + args.filtro + ' [x]; [x][1:v] paletteuse=dither=' + args.dither + ':diff_mode=rectangle"' + ' -y ' + args.sali + ext , shell=True)


#THE ON TESTS "TUMBLR-EFFECT" / EL "EFECTO TUMBLR" QUE ESTÁ EN PRUEBAS
if ext == '.gif' and args.tumblr:
    if os.name == 'nt':
        subprocess.call('magick convert ' + args.sali + ext + ' -level 25%,90% ' + args.sali + ext, shell=True)
    else:
        subprocess.call('convert ' + args.sali + ext + ' -level 25%,90% ' + args.sali + ext, shell=True)

#NOT USED WAYS TO CREATE THE TUMBLR-EFFECT    
#convert -contrast $nom $nom
#convert -brightness-contrast -2x7 $nom $nom
#convert $nom -level 10%,75% $nom

#SEARCH FOR FILE TO KNOW THE SIZE AN PRINT THE RESULT MESSAGE / SE IMPRIME EL MENSAJE DE CREADO Y MOSTRAMOS EL TAMAÑO DEL ARCHIVO
print('Process completed, ' + args.sali + ext + ' created, size:')
tam = os.stat(args.sali + ext) 
print(str(tam.st_size) + " bytes")
