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

### 2019/10/18 CristinaEx

- remove GensimUtils

- 现在使用同义词检索工具SimilarWordUtils

- - 使用方法:
```
from SimilarWordUtils.similar_word_utils import SimilarWordUtils

similar_tools = SimilarWordUtils()
print(similar_tools.getSimilarWord("我"))
print(similar_tools.getSimilarWord("你"))
print(similar_tools.getSimilarWord("他"))
print(similar_tools.getSimilarWord("自行车"))
```
output:
```
['自己', '自家', '自个儿', '自各儿', '自身', '本身', '自我', '本人', '小我', '我', '自', '己']
['你', '您', '恁', '而', '尔', '汝', '若', '乃', '卿', '君', '公']
['异', '他', '外', '客']
['自行车', '脚踏车', '单车', '车子']
```

### 2019/11/04 wwwaqqq

- 解决PPT_mouse.py出现的不适用屏幕的问题

- 改用ppt_keyboard.py,调用pykeyboard实现键盘操作，控制PPT的播放、向前翻页、向后翻页、结束放映。

- 注意实验电脑需要关闭自带功能键（才能用快捷键F5播放PPT）

### 2019/11/12 CristinaEx

- 基本完成主业务逻辑

- 增加基本属性click,click为该流程语音播放前，需要触发多少次动画效果

- 需求
- - 完成语音模块
- - 行为模块需要增加触发动画效果的功能（就是PPT的动画，平常我们需要点击触发的那种）

- 另外，麻烦把各自负责模块在readme里面简要介绍一下

### 2019/11/16 wwwaqqq

- ppt_control:增加PPT中播放和暂停动画的功能

- 采用获取电脑屏幕尺寸并点击屏幕正中央的方式播放动画（考虑到动画一般置于PPT中间且占据大部分面积，应该不会出现屏幕不适配的问题）

- 另外的方式

- - 快捷键（不太成功）
- - 动画直接设置为自动播放（不需要任何操作）

- readme准备待程序完善以后再写

### 2019/11/26 CristinaEx

- 需求
- - 结束动画放映的功能
- - 语音模块!!!

### 2019/12/02 wwwaqqq

- 结束动画放映调用的函数与开始动画放映的函数完全一致

- TeachingPlan_GUI

- 从主页面的两个button选择讲解类型或问答类型，进入子界面
- 在子界面填写该流程信息，存在一些默认值
- 填写完后按确认，成功则告知完成第几个流程的编写，失败则告知填写不完全或填写不规范
- 按取消则会清除该流程所有信息，进行重填

- 由于不太清楚要产生什么格式的输出，目前只是完成了将用户的输入转成一串不严谨格式的信息输出
