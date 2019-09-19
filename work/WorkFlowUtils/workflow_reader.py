import xml.etree.cElementTree as ET

class WorkFlowReader:

    @staticmethod
    def read(path_file):
        """
        读取xml流程文件
        并返回排序好的流程栈
        """
        tree = ET.parse(path_file)
        root = tree.getroot()
        workflows = root[0]
        result = []
        for workflow in workflows:
            d = {}
            for it in workflow:
                if it.tag == 'result':
                    d['result'] = []
                    for r in it:
                        o = {}
                        for i in r:
                            o[i.tag] = i.text
                        d['result'].append(o)
                    continue
                d[it.tag] = it.text
            result.append(d)
        result.sort(key = lambda i:-int(i['index']))
        return result

if __name__ == '__main__':
    print(WorkFlowReader.read("D:\工程应用训练\AutoTeacherProject\\test_data\\test.xml"))