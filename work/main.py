from tkinter import *
from my_dir_list import *
from controler import *
from PIL import Image
from PIL import ImageTk
import os

# pip install baidu-aip

class VisualMain(Frame):
# 可视化界面

    def __init__(self):
        self.PPT_pos = 'None'
        self.XML_pos = 'None'
        self.control = None
        self.last_dir = os.curdir

        Tk().title('AutoTeacherProject')
        Frame.__init__(self,None)
        frame_top = Frame(self,width=380, height=50, bg='white')
        frame_up = Frame(self,width=380, height=100, bg='white')
        frame_down = Frame(self,width=380, height=50, bg='white')
        # 元素
        self.text = StringVar()
        self.text.set('Please Choose PPT!')
        self.label_msg = Label(frame_top,textvariable = self.text)
        Button(frame_down, text='Select', command=self.__buttonSelectPath).grid(row=0, column=1) 
        Button(frame_down, text='Open', command=self.__buttonOpen).grid(row=0, column=2) 
        Button(frame_down, text='Quit', command=self.__buttonExit).grid(row=0, column=3) 
        # pic
        pic_root = Image.open('GUIUtils\\pic\\pic_1.gif')
        pic_root = ImageTk.PhotoImage(pic_root)
        pic_label = Label(frame_up, image = pic_root)
        pic_label.bm = pic_root

        #使用grid设置各个容器位置
        frame_top.grid(row=0, column=1)
        frame_up.grid(row=1, column=1)
        frame_down.grid(row=2, column=1)

        #把元素填充进frame
        
        # self.__text_msg.grid()
        pic_label.pack()
        self.label_msg.pack()
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