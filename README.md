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
        <workflow1>
            <index>顺序<index/>
            <type>1(讲解类型)<type/>
            <word>该说的语音<word/>
            <delay>等待的时间<delay/>
            <index_PPT>PPT的页码<index_PPT/>
        <workflow1/>
        <workflow2>
            <index>顺序<index/>
            <type>2(问答类型)<type/>
            <word>该说的语音<word/>
            <delay>等待的时间<delay/>
            <index_PPT>PPT的页码<index_PPT/>
            <result>
                <word1>
                    <txt>问题的答案（文本）<txt/>
                    <exact>1/0(是否为精确解)<exact/>
                    <workflow_index>问题出现的流程名为第几个<workflow_index/>
                <word1/>
            ......
            <result/>
        <workflow2/>
        ......
    <workflow/>
<root/>
```

## 流程读取模块

- 将xml流程读取，并生成流程栈

- 流程栈的顺序默认以index元素大小控制

- xml -> [dict...]

## 主流程控制模块