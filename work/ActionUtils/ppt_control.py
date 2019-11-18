from pymouse import *
from pykeyboard import *
import time

class PPTKeyboard():
    def __init__(self):
        self.key = PyKeyboard()

    """ 按下快捷键F5播放PPT（打开文件以后）"""
    def playPPT(self):
        time.sleep(1)
        self.key.tap_key(self.key.function_keys[5])

    """ PPT向后翻页，index：翻页数"""
    def nextPPT(self,index):
        for i in range(index):
            time.sleep(1)
            self.key.press_key('N')
            self.key.release_key('N')

    """ PPT向前翻页，index：翻页数"""
    def prePPT(self,index):
        for i in range(index):
            time.sleep(1)
            self.key.press_key('P')
            self.key.release_key('P')

    """PPT结束放映"""
    def endPPT(self):
        time.sleep(1)
        self.key.press_key(self.key.escape_key)
        self.key.release_key(self.key.escape_key)

class PPTMouse():
    def __init__(self):
        self.mouse = PyMouse()
        self.x_dim, self.y_dim = self.mouse.screen_size()    #获取屏幕尺寸

    """ 点击屏幕中心点播放动画"""
    def playMovie(self):
        time.sleep(1)
        self.mouse.click(round(self.x_dim/2),round(self.y_dim/2),1)

    """ 点击屏幕中心点结束动画"""
    def endMovie(self):
        time.sleep(1)
        self.mouse.click(round(self.x_dim/2), round(self.y_dim/2), 1)




if __name__ == '__main__':

    pptkey=PPTKeyboard()
    pptkey.playPPT()
    pptkey.nextPPT(2)
    pptmouse=PPTMouse()
    pptmouse.playMovie()
    time.sleep(20)
    pptmouse.endMovie()
    pptkey.nextPPT(1)
    #mppt.prePPT(1)
    #mppt.endPPT()
