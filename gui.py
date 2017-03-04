from Tkinter import *
import Tkinter
from music import *
import threading

bgcolor = "#3a93df"
root = Tk()
playing = False
thread = None

def playComposition():
	global playing
	# uses the generated file to play
	mozart = audioGenerator()
	p = pyaudio.PyAudio()

	# plays through the entire song
	chunk = 1024
	stream = p.open(format = p.get_format_from_width(mozart.getsampwidth()),  
				channels = mozart.getnchannels(),  
				rate = mozart.getframerate(),  
				output = True)  
	data = mozart.readframes(chunk)
	while data and playing:  
		stream.write(data)  
		data = mozart.readframes(chunk)

	# closes the stream once the songs over
	stream.stop_stream()
	stream.close()
	p.terminate()

# play song
def play():
	global playing
	global thread
	if not playing:
		playing = True
		thread = threading.Thread(target=playComposition)
		thread.start()
	else:
		playing = True
		print(playing)

# stop song
def stop():
	global playing
	global thread
	if playing:
		playing = False
		thread.join()

# exits the app
def exitApp():
	root.destroy()

# runs app
def main():
	root.geometry("200x200")
	root.configure(background = bgcolor)
	
	label = Label(background = bgcolor)
	label.pack()

	frame = Frame(root, background = bgcolor)
	frame.pack()

	button = Button(frame, text="Play", highlightbackground = bgcolor, command = play)
	button.pack(pady = "30")
	exit = Button(frame, text="Stop", highlightbackground = bgcolor, command = stop)
	exit.pack()

	root.mainloop()

if __name__ == "__main__":
	main()