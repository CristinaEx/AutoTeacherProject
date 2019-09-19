import os

def openPPT(PPT_path):
    """
    打开PPT
    PPT_path:ppt所在位置+文件名
    """
    os.system('start ' + PPT_path)

if __name__ == '__main__':
    openPPT('D:\工程应用训练\AutoTeacherProject\\test_data\\test.ppt')