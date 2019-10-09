from GUIUtils.dir_list import DirList
import os

class MyDirList(DirList):

    def __init__(self,parent,initState = None):
        DirList.__init__(self,initState)
        self.parent = parent

    def choose(self):
        tdir = self.cwd.get()
        print(self.path + '\\' + tdir)
        if not os.path.exists(self.path + '\\' + tdir):  # 文件不存在
            pass
        else:
            self.parent.PPT_pos = self.path + '\\' + tdir
            self.top.destroy()
