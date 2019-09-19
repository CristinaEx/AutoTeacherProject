from WorkFlowUtils.workflow_reader import WorkFlowReader
from ActionUtils.ppt_utils import *
import time

class Controler:
# 主流程控制程序

    def __init__(self,PPT_pos,XML_pos):
        """
        PPT_pos:ppt文件的位置
        XML_pos:xml文件位置
        """
        self.work_stack = WorkFlowReader.read(XML_pos)
        openPPT(PPT_pos)

    def run(self):
        """
        执行流程
        """
        while not len(self.work_stack) == 0:
            self.__runOne()

    def __delay(self,t):
        """
        延时t秒
        t:int/float/...
        """
        time.sleep(t)

    def __runOne(self):
        """
        执行当前流程
        """
        workflow = self.work_stack.pop()
        if workflow['type'] == '1':
            # 讲解类型
            # 首先进入当前PPT位置
            print('go to page ' + workflow['index_PPT'])
            # 播放语言
            print(workflow['word'])
            # 等待
            self.__delay(float(workflow['delay']))
            pass
        elif workflow['type'] == '2':
            # 讲解类型
            # 首先进入当前PPT位置
            print('go to page ' + workflow['index_PPT'])
            # 叙述问题
            print(workflow['word'])
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