from WorkFlowUtils.workflow_reader import WorkFlowReader

class Controler:
# 主流程控制程序

    def __init__(self,PPT_pos,XML_pos):
        """
        PPT_pos:ppt文件的位置
        XML_pos:xml文件位置
        """
        self.work_stack = WorkFlowReader.read(XML_pos)

    def run(self):
        """
        执行流程
        """
        while not len(self.work_stack) == 0:
            self.runOne()

    def runOne(self):
        """
        执行当前流程
        """
        workflow = self.work_stack.pop()
        print(workflow)

def test():
    PPT_pos = "D:\工程应用训练\AutoTeacherProject\\test_data\\test.ppt"
    XML_pos = "D:\工程应用训练\AutoTeacherProject\\test_data\\test.xml"
    controler = Controler(PPT_pos,XML_pos)
    controler.run()

if __name__ == '__main__':
    test()