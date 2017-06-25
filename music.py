import wave, pyaudio
import sys
from random import randint

def randomAudioFiles():
	# array of filenames to return
	infiles = []
	count = 1

	# creates list of 16 randomly chosen measures for the minuet
	while count < 17 :
		file = "waves/M" + str(count)
		rollOne = randint(1, 6)
		rollTwo = randint(1, 6)
		rollTotal = rollOne + rollTwo
		file += "-" + str(rollTotal) + ".wav"
		infiles.append(file)
		count += 1

	# creates list of 16 randomly chosen measures for the trio
	while count < 33 :
		file = "waves/T" + str(count)
		roll = randint(1, 6)
		file += "-" + str(roll) + ".wav"
		infiles.append(file)
		count += 1

	return infiles

def audioGenerator():
	# files to read in and file to output to
	infiles = randomAudioFiles();
	outfile = "dice.wav"

	# reads through each .wav file
	# gets the parameters and frames of each .wav file
	data = []
	for infile in infiles:
	    w = wave.open(infile, 'rb')
	    data.append([w.getparams(), w.readframes(w.getnframes())])
	    w.close()

	# writes to the outfile 
	# generates the combined .wav file and returns it
	output = wave.open(outfile, 'wb')
	output.setparams(data[0][0])
	for val in data:
		output.writeframes(val[1])
	output.close()
	composition = wave.open("dice.wav");
	return infiles
