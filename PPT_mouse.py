#实验屏幕尺寸是1280*720
#PPT图标在（750,710）处

from pymouse import PyMouse
import time


m = PyMouse()

def play():               #播放PPT
    m.click(750, 710, 1)   #左击PPT图标所在位置
    time.sleep(2)
    m.click(120,5,1)       #左击放映按钮


def next(n):              #向后翻页
    for i in range(n):
        time.sleep(1)
        m.click(500, 200, 2)   #随意右击屏幕上的一个点
        time.sleep(1)
        m.click(505, 202, 1)   #左击下一张

def previous(n):            #向前翻页
    for i in range(n):
        time.sleep(1)
        m.click(500, 200, 2)   #随意右击屏幕上的一个点
        time.sleep(1)
        m.click(505, 225, )   #左击上一张

def end():
    time.sleep(1)
    m.click(500, 200, 2)  # 随意右击屏幕上的一个点
    time.sleep(1)
    m.click(505, 480, 1)  # 左击结束放映

play()
next(2)
previous(1)
end()
