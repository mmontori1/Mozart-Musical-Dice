from Tkinter import *
import Tkinter
from music import *
import threading

bgcolor = "#3a93df"
root = Tk()
playing = False
visible_text = False
thread = None

def playComposition():
	global playing

	# uses the generated file to play
	mozart = wave.open("dice.wav")
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

# stop song
def stop():
	global playing
	global thread
	if playing:
		playing = False
		thread.join()

def showText():
	global visible_text
	if visible_text:
		text.delete(1.0,END)
	else:
		text.insert(END, "Just a text Widget\nin two lines\n")

# exits the app
def exitApp():
	root.destroy()

# runs app
def main():
	root.geometry("200x200")
	root.configure(background = bgcolor)
	root.wm_title("Mozart Musical Dice")
	
	# label = Label(background = bgcolor)
	# label.pack()

	frame = Frame(root, background = bgcolor)
	frame.pack(side = LEFT)
	frame.place()

	dice = Frame(root, background = bgcolor)
	dice.pack()
	dice.place()
	inst = Button(dice, text="How to use", highlightbackground = bgcolor, command = showText)
	inst.pack(pady = "10")

	text = Text(root, height = 2, width = 30)
	text.pack()

	# add instructions how to uses the app somewhere for ease of use
	# add a method to create picture images of the dice for each portion of the minuet/trio
	# - about button
	# - instruction button
	generate = Button(frame, text="Generate", highlightbackground = bgcolor, command = audioGenerator)
	generate.pack(pady = "10")
	begin = Button(frame, text="Play", highlightbackground = bgcolor, command = play)
	begin.pack(pady = "10")
	end = Button(frame, text="Stop", highlightbackground = bgcolor, command = stop)
	end.pack(pady = "10")

	root.mainloop()

if __name__ == "__main__":
	main()