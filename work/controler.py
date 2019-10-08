from WorkFlowUtils.workflow_reader import WorkFlowReader
import ActionUtils.ppt_utils as ppt_utils
import ActionUtils.PPT_mouse as ppt_mouse
import time

class Controler:
# 主流程控制程序

    def __init__(self,PPT_pos,XML_pos):
        """
        PPT_pos:ppt文件的位置
        XML_pos:xml文件位置
        """
        self.work_stack = WorkFlowReader.read(XML_pos)
        self.PPT_pos = PPT_pos
        self.index = 0# 记录当前PPT页码

    def reinit(self,PPT_pos,XML_pos):
        """
        重新初始化
        """
        self.__init__(PPT_pos,XML_pos)

    def run(self):
        """
        执行流程
        """
        ppt_utils.openPPT(self.PPT_pos)
        self.__delay(3) # 初始等待时间
        ppt_mouse.play()
        while not len(self.work_stack) == 0:
            self.__runOne()

    def __delay(self,t):
        """
        延时t秒
        t:int/float/...
        """
        time.sleep(t)

    def __goToPage(self,index):
        """
        index:页码,int
        跳转至index页
        注:第0页为PPT首页
        """
        print('go to page ' + str(index))

    def __playVoice(self,word):
        """
        word:str
        播放str的语音
        """
        print(word)

    def __runOne(self):
        """
        执行当前流程
        """
        workflow = self.work_stack.pop()
        if workflow['type'] == '1':
            # 讲解类型
            # 首先进入当前PPT位置
            self.__goToPage(int(workflow['index_PPT']))
            # 播放语言
            self.__playVoice(workflow['word'])
            # 等待
            self.__delay(float(workflow['delay']))
            pass
        elif workflow['type'] == '2':
            # 讲解类型
            # 首先进入当前PPT位置
            self.__goToPage(int(workflow['index_PPT']))
            # 叙述问题
            self.__playVoice(workflow['word'])
            # 等待
            self.__delay(float(workflow['delay']))
            # 接收回答
            # 判断回答
            # 完成问题解决方案

def test():
    PPT_pos = "D:\工程应用训练\AutoTeacherProject\\test_data\\test.ppt"
    XML_pos = "D:\工程应用训练\AutoTeacherProject\\test_data\\test.xml"
    controler = Controler(PPT_pos,XML_pos)
    controler.run()

if __name__ == '__main__':
    test()