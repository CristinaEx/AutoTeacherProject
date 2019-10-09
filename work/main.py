from tkinter import *
from my_dir_list import *
from controler import *
import os

class VisualMain(Frame):
# 可视化界面

    def __init__(self):
        self.PPT_pos = 'None'
        self.XML_pos = 'None'
        self.control = None
        self.last_dir = os.curdir

        Tk().title('AutoTeacherProject')
        Frame.__init__(self,None)
        frame_up = Frame(self,width=380, height=100, bg='white')
        frame_down = Frame(self,width=380, height=50, bg='white')
        # 元素
        self.__text_msg = Text(frame_up)
        Button(frame_down, text='Select', command=self.__buttonSelectPath).grid(row=0, column=1) 
        Button(frame_down, text='Open', command=self.__buttonOpen).grid(row=0, column=2) 
        Button(frame_down, text='Quit', command=self.__buttonExit).grid(row=0, column=3) 

        #使用grid设置各个容器位置
        frame_up.grid(row=0, column=1)
        frame_down.grid(row=1, column=1)

        #把元素填充进frame
        
        self.__text_msg.grid()
        self.pack()
        mainloop()

    def __buttonSelectPath(self):
        MyDirList(self)

    def __buttonOpen(self):
        self.XML_pos = self.PPT_pos[:-3] + 'xml'
        try:
            self.control = Controler(self.PPT_pos,self.XML_pos)
        except:
            return
        else:
            self.control.run()

    def __buttonExit(self):
        exit(0)

if __name__ == '__main__':
    test = VisualMain()