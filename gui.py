from Tkinter import *
import Tkinter
from run import *

bgcolor = "#3a93df"
root = Tk()

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

	button = Button(frame, text="Play a song", highlightbackground = bgcolor, command = playComposition)
	button.pack(pady = "30")
	exit = Button(frame, text="exit", highlightbackground = bgcolor, command = exitApp)
	exit.pack()

	root.mainloop()

if __name__ == "__main__":
	main()