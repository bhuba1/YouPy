from __future__ import unicode_literals
import youtube_dl
import os
import sys
from urllib.request import urlopen
import threading
import time
from tqdm import tqdm

downloading = False

link =''
directory = "mp3"

ydl_opts = {
	'format': 'bestaudio/best',
	'outtmpl': 'mp3/%(title)s.%(ext)s',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '320',
	}],
}

def createFolder(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
def sizePrinter(title):
	global downloading

	
	while not os.path.exists(directory + "\\" + title + '.webm'):
		# print('asd')
		time.sleep(.1)
	
	if os.path.exists(directory + "\\" + title + '.webm'):
		totalSize = (os.path.getsize(directory + "\\" + title + '.webm')) * 2.46
		# print(str(totalSize))
	
	while not os.path.exists(directory + "\\" + title + '.mp3'):
		# print('asd')
		time.sleep(.1)

	while downloading:
		size = -1

		# print(directory + "\\" + title + '.mp3')
		if os.path.exists(directory + "\\" + title + '.mp3'):
			size = (os.path.getsize(directory + "\\" + title + '.mp3'))
			
			

			if size != totalSize:
				# print('Current size of file: ' + str(size))
				per = round((size/totalSize * 100),1)
				# print ('[convert] converted: ' + str(per)+"%", end="\r")
				
				if True:
					print ('[convert] converted: ' + str(per)+"%" + ' | ' + str(size) + ' of ' + str(totalSize), end="\r")
					
				else:
					print('[convert] converted: 100%')
					break
		time.sleep(.1)
	time.sleep(1)
	sys.stdout.write('\r'+'[convert] converted: 100%\n')
	

	print('Done!')

def download():
	global downloading
	ytdl = youtube_dl.YoutubeDL()
	info = ytdl.extract_info(link, download=False)
	title = info['title']
	formats = info['formats']

	downloading = True
	x = threading.Thread(target=sizePrinter,args=(title,))

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		x.start()
		ydl.download([link])

	downloading = False



def getInput():
	global link
	link = input("Give me a youtube link pls: ")

def main():
	print("Youtube Video getter v0.1")
	getInput()

	print('Loading...')

	createFolder(directory)
	download()


if __name__ == "__main__":
	main();
