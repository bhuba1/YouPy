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
	
	title = title.replace('|','_')
	while not os.path.exists(directory + "\\" + title + '.webm'):
		time.sleep(.1)
	
	if os.path.exists(directory + "\\" + title + '.webm'):
		totalSize = int(((os.path.getsize(directory + "\\" + title + '.webm')) * 2.46))
			
	while not os.path.exists(directory + "\\" + title + '.mp3'):
		time.sleep(.1)
	
	time.sleep(.6)
	print('[convert] Converting: ' + directory + "\\" + title + '.webm'+ ' to .mp3')

	while downloading:
		size = -1

		
		if os.path.exists(directory + "\\" + title + '.mp3'):
			size = (os.path.getsize(directory + "\\" + title + '.mp3'))
			
			

			if size != totalSize:
				
				per = round((size/totalSize * 100),1)
				
				print ('[convert] Converted: ' + str(per)+"%" + ' | ' + str(size) + ' of ' + str(totalSize), end="\r")
		time.sleep(.1)
	
	# Back to previous line
	sys.stdout.write("\033[F")
	# Clear line
	sys.stdout.write("\033[K")
	
	print('[convert] converted: 100%')
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
	main()
