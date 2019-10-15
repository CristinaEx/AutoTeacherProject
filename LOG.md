### 2019/09/16 CristinaEx

- 创建README.md

- 修改README.md,规划好教学流程设计模块的设计方案

- 创建workflow_maker.py,教学流程设计模块的主模块位置

- 建议接下来的工作:考虑简洁和高效的教学流程设计模块的设计

### 2019/09/19 CristinaEx

- test_data:测试数据

- workflow_maker.py:完成将txt流程文本转换为xml

- workflow_reader.py:完成阅读xml文本流程，并转换为流程序列

- controler.py:完成主流程控制程序框架

请选择接受以下工作：

- ActionUtils
- - 行为控制模块，要求提供接口控制PPT
- - 工作在work\\ActionUtils

- VoiceUtils
- - 语音控制模块，要求提供接口，使文本转换为语音
- - 工作在work\\VoiceUtils

### 2019/10/08 CristinaEx

- 新增package文件夹，存放依赖包
- 问题:PPT_mouse.py，出现了不适用屏幕的问题，可不可以通过以下解决方法解决:
- - 获取当前显示信息，通过相对坐标比例*显示信息确定各个键位的绝对位置
- - 通过截屏，再通过图像搜索方法获取当前各个键位的位置
- - 调用PPT内置API

### 2019/10/09 CristinaEx

- GUIUtils为图形界面工具包

- 更新main，完成基础的图形界面

- 现在运行main文件可以测试部分内容了
- - 运行main后选择choose找到test_data里的ppt文件
- - 选择后在分界面确认，跳转回主界面
- - 在主界面点击Open即可开始运行

### 2019/10/15 CristinaEx

- GensimUtils

- 同义词检索工具