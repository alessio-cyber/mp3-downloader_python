from pytube import YouTube #libreria da utilizzare
import os #per gestione file e path


yt = YouTube( 
	str(input("INSERISCI URL VIDEO_YOUTUBE: \n>> "))) 

#estrae l'audio
video = yt.streams.filter(only_audio=True).first() 

#gestione path
print("inserisci un path di destinazione (leave blank for current directory)") 
destination = str(input(">> ")) or '.'

#download del file nel path scelto
out_file = video.download(output_path=destination) 

#salvataggio del file sul sistema
base, ext = os.path.splitext(out_file) 
new_file = base + '.mp3'
os.rename(out_file, new_file) 

#stampa finale di avviso
print(yt.title + " has been successfully downloaded.")
