from Tkinter import *
import Tkinter
from music import *
import threading

bgcolor = "#3a93df"
root = Tk()
playing = False
thread = None
howTo = False

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
	playing = False

def playSong():
	global playing
	global thread
	if not playing:
		playing = True
		thread = threading.Thread(target=playComposition)
		thread.start()
	else:
		playing = True

def stopSong():
	global playing
	global thread
	if playing:
		playing = False
		thread.join()

def exitApp():
	stopSong()
	root.destroy()

def createInstructions(frame):
	global howTo
	if not howTo:
		howTo = True
		header = Label(frame, bg = bgcolor, text = "Instructions: ")
		header.pack(pady = "20")
		generate = Label(frame, bg = bgcolor, text = "Generate: Generates a new composition at random to simulate dice rolls.")
		generate.pack(pady = "5")
		play = Label(frame, bg = bgcolor, text = "Play: Plays current composition. Cannot generate while playing.")
		play.pack(pady = "5")
		stop = Label(frame, bg = bgcolor, text = "Stop: Stops current composition")
		stop.pack(pady = "5")
		clear = Label(frame, bg = bgcolor, text = "Clear: Clears out instructions")
		clear.pack(pady = "5")
		quit = Label(frame, bg = bgcolor, text = "Quit: Exits the app")
		quit.pack(pady = "5")

# uses audioGenerator to create labels with dice rolls
def createMusic(frame):
	dice = audioGenerator()
	headerText = "current piece: "
	header = Label(frame, bg = bgcolor, text = headerText)
	header.pack()

	count = 0
	result = "Minuet Rolls: "
	removal = ""
	val = ""
	while count < 16 :
		val = dice[count]
		removal = val.split('-', 1)[-1]
		result += removal.split('.', 1)[0]
		result += ", "
		count += 1
	result = result[:-2]
	minuet = Label(frame, bg = bgcolor, text = result)
	minuet.pack()

	result = "Trio Rolls: "
	while count < 32:
		val = dice[count]
		removal = val.split('-', 1)[-1]
		result += removal.split('.', 1)[0]
		result += ", "
		count += 1
	result = result[:-2]
	trio = Label(frame, bg = bgcolor, text = result)
	trio.pack()

def generateMusic(frame):
	global playing
	global howTo
	if not playing:
		if howTo:
			clearFrame(frame)
			createMusic(frame)
			createInstructions(frame)
		else:
			clearFrame(frame)
			createMusic(frame)

# clears entire frame
def clearFrame(frame):
	global playing
	global howTo
	if not playing:
		howTo = False
		childrens = frame.winfo_children()
		for widget in childrens:
			widget.destroy()

# clears instructions
def clearInstructions(frame):
	global playing
	global howTo
	if howTo:
		howTo = False
		childrens = frame.winfo_children()
		for widget in childrens:
			if widget is not childrens[0] and widget is not childrens[1] and widget is not childrens[2]:
				widget.destroy()

# runs app
def main():
	root.geometry("680x300")
	root.configure(background = bgcolor)
	root.wm_title("Mozart Musical Dice")

	frame = Frame(root, background = bgcolor)
	frame.pack(side=LEFT)

	dice = Frame(root, background = bgcolor)
	dice.pack()

	generateMusic(dice)
	createInstructions(dice)

	inst = Button(frame, text="How to use", highlightbackground = bgcolor, command = lambda:(createInstructions(dice)))
	inst.pack(padx = "20", pady = "10")
	generate = Button(frame, text="Generate", highlightbackground = bgcolor, command = lambda:(generateMusic(dice)))
	generate.pack(padx = "20", pady = "10")
	begin = Button(frame, text="Play", highlightbackground = bgcolor, command = playSong)
	begin.pack(padx = "20", pady = "10")
	end = Button(frame, text="Stop", highlightbackground = bgcolor, command = stopSong)
	end.pack(padx = "20", pady = "10")
	clear = Button(frame, text="Clear", highlightbackground = bgcolor, command = lambda: (clearInstructions(dice)))
	clear.pack(padx = "20", pady = "10")
	quit = Button(frame, text="Quit", highlightbackground = bgcolor, command = exitApp)
	quit.pack(padx = "20", pady = "10")

	root.mainloop()

if __name__ == "__main__":
	main()