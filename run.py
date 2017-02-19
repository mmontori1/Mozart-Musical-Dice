import wave, pyaudio
import sys
from random import randint

def randomAudioFile():
	#array of filenames to return
	infiles = []
	count = 1

	#create list of minuets
	while(count < 17):
		file = "waves/M" + str(count)
		rollOne = randint(1, 6)
		rollTwo = randint(1, 6)
		rollTotal = rollOne + rollTwo
		file += "-" + str(rollTotal) + ".wav"
		index = count - 1
		print(file)
		infiles.append(file)
		count += 1

	return infiles

def audioGenerator():
	#files to read in and file to output to
	infiles = randomAudioFile();
	outfile = "dice.wav"

	#reads through each .wav file
	#gets the parameters and frames of each .wav file
	data = []
	for infile in infiles:
	    w = wave.open(infile, 'rb')
	    data.append([w.getparams(), w.readframes(w.getnframes())])
	    w.close()

	#generates the combined .wav file and returns it
	output = wave.open(outfile, 'wb')
	output.setparams(data[0][0])
	count = 0
	for val in data:
		output.writeframes(val[1])
		count += 1
	output.close()
	composition = wave.open("dice.wav");
	return composition

def main():
	f = audioGenerator()
	p = pyaudio.PyAudio()
	chunk = 1024
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
				channels = f.getnchannels(),  
				rate = f.getframerate(),  
				output = True)  
	data = f.readframes(chunk)
	while data:  
		stream.write(data)  
		data = f.readframes(chunk)

	stream.stop_stream()
	stream.close()
	p.terminate()

if __name__ == "__main__":
	main()
