from VoiceUtils.voice2word import *
from VoiceUtils.recorder import Recorder
from playsound import playsound

"""
我用windows+python，所以在playsound里的winCommand里添加下面的代码
while True:
    if winCommand('status', alias, 'mode').decode() == 'stopped':
        winCommand('close', alias)
        break
一定在“winCommand('play', alias, 'from 0 to', durationInMS.decode())”位置后添加代码。实测没问题。
"""

class VoiceUtils:

    def __init__(self):
        self.recorder = Recorder()
        self.output_filename = 'output.wav'
        self.voice = Voice2Word()

    def record(self,second,output_path = '.'):
        """
        second:录音时间
        output_file:输出文件位置
        """
        self.recorder.record(second,output_path + '\\' + self.output_filename)

    def voice2word(self,filename = 'output.wav'):
        result = self.voice.voice2word(filename)
        return result

    def word2voice(self,word,filename = 'audio.mp3'):
        self.voice.word2voice(word,filename)

    def playAudio(self,filename = 'audio.mp3'):
        playsound(filename)
 

if __name__ == '__main__':
    voice = VoiceUtils()