# media converter 2.0
# requires ffmpeg
# works by copying this script into directory then running with python launcher
# written by Justin Chan

import os
import fnmatch 
import subprocess
import time

#input filetype to convert, and final media type here
from_media = 'avi'
to_media = 'mp3'
pathname = os.getcwd()
path,subdirs,files = os.walk(pathname).next()
convert_files = fnmatch.filter(os.listdir(path),'*.'+from_media)
num_convert_files = len(convert_files)
print('number of files to convert = '),(num_convert_files)
print('beginning conversion')
t1 = time.time()

for file in convert_files:
	file_to_convert = path+'/'+file
	converted_file = file_to_convert[:-4]+'.'+to_media
	print('starting to convert '),(file)
	t2 = time.time()
	command = ['ffmpeg','-loglevel','quiet','-i',file_to_convert,converted_file]
	outpipe = subprocess.Popen(command)
	output,error = outpipe.communicate()
	outpipe.wait()
	t3 = time.time()
	print('completed in '),(t3-t2),('seconds')
t4 = time.time()
print('completed!')
print('elapsed time:'),(t4-t1),('seconds')