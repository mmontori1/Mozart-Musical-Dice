# Mozart's Musical Dice

The Musikalisches Würfelspiel is one of the first examples of interactive music, which was composed by Mozart. Depending on multiple dice rolls, a different piece of music is played. This is done by combining measures to generate a minuet and a trio, both which are 16 measures, to create a waltz. 

I read about this while taking MUSPREF 300: Video Game Music at the University of Michigan, so I thought about creating a program to play the music. This Python program generates, plays, and saves the composition to a file called dice.wav.

#Python Dependencies:
###Pyaudio
For Mac, install using these commands (you must have pip and homebrew installed):
```
	brew install portaudio
	sudo pip install pyaudio
```

#Running the program
For Mac, go to the folder through terminal and run the python file gui.py
```
	python gui.py
```