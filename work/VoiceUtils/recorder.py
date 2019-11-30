import pyaudio
import wave
import os

from playsound import playsound

RECORD_START = 'mp3\\record_start.mp3'
RECORD_END = 'mp3\\record_end.mp3'

class Recorder:

    def __init__(self):
        """PyAudio example: Record a few seconds of audio and save to a WAVE file."""
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 16000

    def record(self,RECORD_SECONDS = 3,WAVE_OUTPUT_FILENAME = "output.wav"):    
        p = pyaudio.PyAudio()

        stream = p.open(format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                input=True,
                frames_per_buffer=self.CHUNK)

        playsound(RECORD_START)
        print("* recording")

        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("* done recording") 
        playsound(RECORD_END)
           
        stream.stop_stream()
        stream.close()
        p.terminate()

        if os.path.exists(WAVE_OUTPUT_FILENAME):
            os.remove(WAVE_OUTPUT_FILENAME)

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    
if __name__ == '__main__':
    recorder = Recorder()
    recorder.record(RECORD_SECONDS = 5)