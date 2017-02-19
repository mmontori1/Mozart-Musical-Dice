import wave, pyaudio
import sys
from random import randint

def randomAudioFile():
	count = 1
	infiles = []
	#create list of minuets
	while(count < 17):
		file = "M" + str(count)
		rollOne = randint(1, 6)
		rollTwo = randint(1, 6)
		rollTotal = rollOne + rollTwo
		file += "-" + str(rollTotal) + ".wav"
		index = count - 1
		infiles.append(file)
		count += 1
	# for files in infiles:
	# 	print files

def audioGenerator():
	# f = wave.open("waves/M1.wav")
	outfile = "dice.wav"
	# infiles = randomAudioFile();
	infiles = ["waves/M1-2.wav", "waves/M2-2.wav"]

	data = []
	for infile in infiles:
	    w = wave.open(infile, 'rb')
	    data.append( [w.getparams(), w.readframes(w.getnframes())] )
	    w.close()

	output = wave.open(outfile, 'wb')
	output.setparams(data[0][0])
	output.writeframes(data[0][1])
	output.writeframes(data[1][1])
	output.close()
	composition = wave.open("dice.wav");
	return composition

def main():
	randomAudioFile()
	# f = audioGenerator()
	# p = pyaudio.PyAudio()
	# chunk = 1024
	# stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
	# 			channels = f.getnchannels(),  
	# 			rate = f.getframerate(),  
	# 			output = True)  
	# data = f.readframes(chunk)
	# while data:  
	# 	stream.write(data)  
	# 	data = f.readframes(chunk)

	# stream.stop_stream()
	# stream.close()
	# p.terminate()

if __name__ == "__main__":
	main()
