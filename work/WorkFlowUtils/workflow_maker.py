import xml.etree.cElementTree as ET

class WorkFlowMaker:
# 文本->xml

    def __init__(self):
        self.root = ET.Element('root') 
        self.workflow = ET.SubElement(self.root,'workflow') 
        self.workflow_num = 0

    def write(self,path_name):
        ET.ElementTree(self.root).write(path_name, encoding='UTF-8')

    def add(self,word,index = None):
        """
        增加一条流程
        word:str
        index:流程顺序序列号
        """
        if index == None:
            index = self.workflow_num
        items = word.split('|')
        # 公有属性
        workflow = ET.SubElement(self.workflow, 'workflow' + str(index)) 
        ind = ET.SubElement(workflow, 'index') 
        ind.text = str(index)
        visual_ = ET.SubElement(workflow, 'visual') 
        visual_.text = items[0]
        type_ = ET.SubElement(workflow, 'type') 
        type_.text = items[1]
        word = ET.SubElement(workflow, 'word') 
        word.text = items[2]
        delay = ET.SubElement(workflow, 'delay') 
        # delay默认为0
        if items[3] == '':
            items[3] = '0'
        delay.text = items[3]
        click = ET.SubElement(workflow, 'click') 
        # click默认为0
        if items[4] == '':
            items[4] = '0'
        click.text = items[4]
        index_PPT = ET.SubElement(workflow, 'index_PPT') 
        index_PPT.text = items[5]
        # 讲解流程判定
        if items[1] == '1':
            pass
        # 问答流程判定
        elif items[1] == '2':
            result = ET.SubElement(workflow, 'result')
            # 问题答案记录
            for i in range(int((len(items)-4)/3)):
                word = ET.SubElement(result, 'word'+str(i))
                txt = ET.SubElement(word, 'txt')
                txt.text = items[6+i*3]
                exact = ET.SubElement(word, 'exact')
                exact.text = items[7+i*3]
                workflow_index = ET.SubElement(word, 'workflow_index')
                workflow_index.text = items[8+i*3]
        self.workflow_num += 1

def test(file_name,out_put_name):
    """
    测试样例
    file_name:文本位置
    out_put_name:输出位置
    """
    maker = WorkFlowMaker()
    with open(file_name) as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            maker.add(line)
    maker.write(out_put_name)

if __name__ == '__main__':
    test(file_name = "D:\工程应用训练\AutoTeacherProject\\test_data\\test.txt",out_put_name = "D:\工程应用训练\AutoTeacherProject\\test_data\\test.xml")