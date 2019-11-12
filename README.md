# AutoTeacherProject

## 教学流程设计模块

- 提供教案到XML规范化流程的映射

- 文本(+PPT) -> XML
- - 对非必要元素提供默认填充

- 即时(顺序)输入

- - 输入过程与教学流程顺序有关

XML输入格式如下：
```
<root>
    <workflow>
        <workflow0>
            <index>顺序<index/>
            <visual>1(是否可视1 or 0)<visual/>
            <type>1(讲解类型)<type/>
            <word>该说的语音<word/>
            <delay>等待的时间<delay/>
            <click>动画效果点击次数(num),点击操作在语音输出之前进行<click/>
            <index_PPT>PPT的页码<index_PPT/>
        <workflow0/>
        <workflow1>
            <index>顺序<index/>
            <visual>1(是否可视1 or 0)<visual/>
            <type>2(问答类型)<type/>
            <word>该说的语音<word/>
            <delay>等待的时间<delay/>
            <click>动画效果点击次数(num),点击操作在语音输出之前进行<click/>
            <index_PPT>PPT的页码<index_PPT/>
            <result>
                <word1>
                    <txt>问题的答案（文本）<txt/>
                    <exact>1/0(是否为精确解)<exact/>
                    <workflow_index>问题出现的流程index<workflow_index/>
                <word1/>
            ......
            <result/>
        <workflow1/>
        ......
    <workflow/>
<root/>
```

## 流程读取模块

- 将xml流程读取，并生成流程栈

- 流程栈的顺序默认以index元素大小控制

- xml -> [dict...]

## 主流程控制模块

主流程运行顺序:

- 1.从流程栈里读取一个流程
- 2.识别当前流程是否为可视的(visual)，若不可视，则查看是否有查看许可，若没有许可，则跳过该流程
- 3.识别当前流程类型
- 4.执行动画效果触发
- 5.执行语音输出
- 6.执行讲解或者问题流程特定的内容

如果是问题流程:
- 如果出现问题回答错误，则将该问题所属流程序号插入流程栈栈顶
- 重复以上流程，直到流程栈为空

## 语音识别模块

## 动作执行模块

## 教案制作模块