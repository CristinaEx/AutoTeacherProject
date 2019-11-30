# -*- coding: utf-8 -*-  
from aip import AipSpeech
# pip install baidu-aip

class Voice2Word:

    def __init__(self):

        """ 你的 APPID AK SK """
        self.APP_ID = '17896871'
        self.API_KEY = 'Qjva533G96GmTKVblEYRZWSA'
        self.SECRET_KEY = 'Ya67pHTOs6OCkL35A8LPXQnI13B1wEXV'

        self.client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    # 读取文件
    def __get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def voice2word(self,filename = 'output.wav'):
        # 识别本地文件
        data = self.client.asr(self.__get_file_content(filename), 'wav', 16000, {
            'dev_pid': 1536,
        })
        try:
            data['result']
        except:
            return []
        return data['result']
        
    def word2voice(self,word,filename = 'audio.mp3'):
        result  = self.client.synthesis(word, 'zh', 1, {
            'vol': 5,
        })

        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open(filename, 'wb+') as f:
                f.write(result)

if __name__ == '__main__':
    voice2word = Voice2Word()
    result = voice2word.voice2word()
    for word in result:
        voice2word.word2voice(word)