from WorkFlowUtils.workflow_reader import WorkFlowReader
from SimilarWordUtils.similar_word_utils import SimilarWordUtils
import ActionUtils.ppt_utils as ppt_utils
import ActionUtils.ppt_keyboard as ppt_keyboard
import time

class Controler:
# 主流程控制程序

    def __init__(self,PPT_pos,XML_pos):
        """
        PPT_pos:ppt文件的位置
        XML_pos:xml文件位置
        """
        self.work_stack = WorkFlowReader.read(XML_pos)
        self.stack_book = {}
        for stack in self.work_stack:
            self.stack_book[stack['index']] = stack
        self.PPT_pos = PPT_pos# PPT在电脑存储的位置
        self.index = 1# 记录当前PPT页码
        self.extra_workflows = []# 接入许可
        self.keyboard = ppt_keyboard.PPTKeyboard()# 键盘操作
        self.similar_utils = SimilarWordUtils()

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
        self.keyboard.playPPT()
        while not len(self.work_stack) == 0:
            self.__runOne()
        print('Finish PPT')

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
        if self.index > index:
            self.keyboard.prePPT(self.index - index)
        else:
            self.keyboard.nextPPT(index - self.index)
        self.index = index

    def __playVoice(self,word):
        """
        word:str
        播放str的语音
        """
        print(word)

    def __clickAnime(self,times):
        """
        times点击次数
        动画效果点击
        """
        print('click ' + str(times) + ' times !')

    def __receiveWord(self,seconds):
        """
        seconds:接收语音允许的时间
        接收语音
        """
        self.__delay(seconds)
        return '答案1'

    def __runOne(self):
        """
        执行当前流程
        """
        workflow = self.work_stack.pop()
        # 判断是否非显示流程
        if workflow['visual'] == '0':
            # 非显示流程且没有接入许可
            if not workflow['index'] in self.extra_workflows:
                return
            # 有介入许可
            self.extra_workflows.remove(workflow['index'])
        if workflow['type'] == '1':
            # 讲解类型
            # 首先进入当前PPT位置
            self.__goToPage(int(workflow['index_PPT']))
            # 动画效果点击
            self.__clickAnime(int(workflow['click']))
            # 播放语言
            self.__playVoice(workflow['word'])
            # 等待
            self.__delay(float(workflow['delay']))
        elif workflow['type'] == '2':
            # 讲解类型
            # 首先进入当前PPT位置
            self.__goToPage(int(workflow['index_PPT']))
            # 动画效果点击
            self.__clickAnime(int(workflow['click']))
            # 叙述问题
            self.__playVoice(workflow['word'])
            # 等待
            # self.__delay(float(workflow['delay']))
            # 接收回答
            word = self.__receiveWord(float(workflow['delay']))
            # 判断回答
            for result in workflow['result']:
                # 问题是否精确解
                if result['exact'] == '1':
                    # 精确解
                    # 问题回答错误
                    if not result['txt'] in word:
                        # 存在问题回答错误后的反馈
                        print('Wrong Answer:' + word + ' ---> ' + result['txt'])
                        if not result['workflow_index'] == '':
                            add_workflow = self.stack_book[result['workflow_index']]
                            # 授予介入许可
                            if add_workflow['visual'] == '0':
                                self.extra_workflows.append(add_workflow['index'])
                            self.work_stack.append(add_workflow)
                    else:
                        # 问题回答正确
                        print('Correct Answer:' + word)
                else:
                    # 非精确解
                    # 获取近义词
                    txts = [result['txt']] + self.similar_utils.getSimilarWord(result['txt'])
                    correct = False
                    for txt in txts:
                        if txt in word:
                            correct = True
                            break
                    # 如果错误
                    if not correct:
                        # 存在问题回答错误后的反馈
                        print('Wrong Answer:' + word + ' ---> ' + str(txts))
                        if not result['workflow_index'] == '':
                            add_workflow = self.stack_book[result['workflow_index']]
                            # 授予介入许可
                            if add_workflow['visual'] == '0':
                                self.extra_workflows.append(add_workflow['index'])
                            self.work_stack.append(add_workflow)     
                    else:
                        # 问题回答正确
                        print('Correct Answer:' + word + ' in ' + str(txts))      
            # 完成问题解决方案
            

def test():
    PPT_pos = "D:\工程应用训练\AutoTeacherProject\\test_data\\test.ppt"
    XML_pos = "D:\工程应用训练\AutoTeacherProject\\test_data\\test.xml"
    controler = Controler(PPT_pos,XML_pos)
    controler.run()

if __name__ == '__main__':
    test()