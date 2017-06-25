# Mozart's Musical Dice

The Musikalisches Würfelspiel is one of the first examples of interactive music, which was composed by Mozart. Depending on multiple dice rolls, a different piece of music is played. This is done by combining measures to generate a minuet and a trio, both which are 16 measures, to create a waltz. 

I read about this while taking MUSPREF 300: Video Game Music at the University of Michigan, so I thought about creating a program to play the music. This Python program generates, plays, and saves the composition to a file called dice.wav.

# Python Dependencies:
## Pyaudio
For Mac, install using these commands (you must have pip and homebrew installed):
```
brew install portaudio
sudo pip install pyaudio
```

## Py2App
I found downloading the source to install [py2app](https://pypi.python.org/pypi/py2app#downloads) seemed much easier. Go into the folder through terminal and run this command.
```
python setup.py install
```

# Running the program
To run the app directly through terminal:
```
python gui.py
```
# Creating the Application
The app will be created within the dist directory, and can be dragged over to your Applications folder for easy use. To create the app just run the create.sh shell script:
```
sh create.sh
```