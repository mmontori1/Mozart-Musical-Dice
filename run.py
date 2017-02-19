import wave, pyaudio
import sys
from random import randint

def audioGenerator():
	f = wave.open("waves/M1.wav")
	return f

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
