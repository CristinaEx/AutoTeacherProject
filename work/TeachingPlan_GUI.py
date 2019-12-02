import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error

num=0  #全局变量，流程顺序
window = tk.Tk()     #主界面
window.title('教案编写')
window.geometry('450x150')
tk.Label(window, text='请选择教学类型:').place(x=170, y=20)

#选择讲解类型后的子界面
def teach():
    window_teach=tk.Toplevel(window)
    window_teach.title('讲解环节教案')
    window_teach.geometry('600x330')

    var1 = tk.StringVar()
    var1.set('1')         #默认值
    tk.Label(window_teach, text='讲解词是否可视: ').place(x=10, y=10)
    tk.Label(window_teach, text='（可视为1，不可视为0）').place(x=5, y=30)
    entry_var1 = tk.Entry(window_teach, textvariable=var1)
    entry_var1.place(x=150, y=10)

    var2 = tk.StringVar()
    tk.Label(window_teach, text='讲解词: ').place(x=10, y=70)
    entry_var2 = tk.Entry(window_teach, textvariable=var2,width=60)
    entry_var2.place(x=150, y=70)

    var3 = tk.StringVar()
    var3.set('10')          #默认值
    tk.Label(window_teach, text='等待的时间（秒）: ').place(x=10, y=110)
    entry_var3 = tk.Entry(window_teach, textvariable=var3)
    entry_var3.place(x=150, y=110)

    var4 = tk.StringVar()
    var4.set('0')         #默认值
    tk.Label(window_teach, text='动画个数: ').place(x=10, y=150)
    entry_var4 = tk.Entry(window_teach, textvariable=var4)
    entry_var4.place(x=150, y=150)

    var5 = tk.StringVar()
    tk.Label(window_teach, text='对应PPT页码').place(x=10, y=190)
    entry_var5 = tk.Entry(window_teach, textvariable=var5)
    entry_var5.place(x=150, y=190)

    #讲解环节点击确认后调用函数
    def teach_comfirm():

        kind = 1
        var_1 = var1.get()
        var_2 = var2.get()
        var_3 = var3.get()
        var_4 = var4.get()
        var_5 = var5.get()

        if var_1 == '' or var_2 == '' or var_3 == '' or var_4 == '' or var_5 == '':
            tk.messagebox.showerror(message='信息未填写完整')
        else:
            if var_1 == '1' or var_1 == '0':
                global num
                num = num + 1
                tk.messagebox.showinfo(message='已完成第%d个流程的编写' % num)
                print('顺序：%d' % num)
                print('类型：%d' % kind)
                print('是否可视：%s' % var_1)
                print('讲解词：%s' % var_2)
                print('等待时间：%s' % var_3)
                print('动画个数：%s' % var_4)
                print('PPT页码：%s' % var_5)
            else:
                tk.messagebox.showerror(message='讲解词是否可视只能填1或0')

    # 讲解环节点击取消后调用函数
    def teach_cancel():
        entry_var1.delete(0,'end')
        entry_var2.delete(0,'end')
        entry_var3.delete(0,'end')
        entry_var4.delete(0,'end')
        entry_var5.delete(0,'end')

    #讲解环节的两个button
    btn_comfirm = tk.Button(window_teach, text='确认', command=teach_comfirm)
    btn_comfirm.place(x=10, y=230)
    btn_cancel = tk.Button(window_teach, text='取消', command=teach_cancel)
    btn_cancel.place(x=150, y=230)


#选择问答类型后的子界面
def ask():
    window_ask = tk.Toplevel(window)
    window_ask.title('问答环节教案')
    window_ask.geometry('600x330')

    var1 = tk.StringVar()
    var1.set('1')       #默认值
    tk.Label(window_ask, text='讲解词是否可视: ').place(x=10, y=10)
    tk.Label(window_ask, text='（可视为1，不可视为0）').place(x=5, y=30)
    entry_var1 = tk.Entry(window_ask, textvariable=var1)
    entry_var1.place(x=150, y=10)

    var2 = tk.StringVar()
    tk.Label(window_ask, text='讲解词: ').place(x=10, y=70)
    entry_var2 = tk.Entry(window_ask, textvariable=var2, width=60)
    entry_var2.place(x=150, y=70)

    var3 = tk.StringVar()
    var3.set('10')      #默认值
    tk.Label(window_ask, text='等待的时间（秒）: ').place(x=10, y=110)
    entry_var3 = tk.Entry(window_ask, textvariable=var3)
    entry_var3.place(x=150, y=110)

    var4 = tk.StringVar()
    var4.set('0')      #默认值
    tk.Label(window_ask, text='动画个数: ').place(x=10, y=150)
    entry_var4 = tk.Entry(window_ask, textvariable=var4)
    entry_var4.place(x=150, y=150)

    var5 = tk.StringVar()
    tk.Label(window_ask, text='对应PPT页码').place(x=10, y=190)
    entry_var5 = tk.Entry(window_ask, textvariable=var5)
    entry_var5.place(x=150, y=190)

    var6 = tk.StringVar()
    tk.Label(window_ask, text='问题的答案').place(x=10, y=230)
    entry_var6 = tk.Entry(window_ask, textvariable=var6,width=60)
    entry_var6.place(x=150, y=230)

    # 问答环节点击确认后调用函数
    def ask_comfirm():
        kind = 2
        var_1 = var1.get()
        var_2 = var2.get()
        var_3 = var3.get()
        var_4 = var4.get()
        var_5 = var5.get()
        var_6 = var6.get()

        if var_1 == '' or var_2 == '' or var_3 == '' or var_4 == '' or var_5 == ''or var_6 == '':
            tk.messagebox.showerror(message='信息未填写完整')
        else:
            if var_1 == '1' or var_1 =='0':
                global num
                num = num + 1
                tk.messagebox.showinfo(message='已完成第%d个流程的编写' % num)
                print('顺序：%d' % num)
                print('类型：%d' % kind)
                print('是否可视：%s' % var_1)
                print('讲解词：%s' % var_2)
                print('等待时间：%s' % var_3)
                print('动画个数：%s' % var_4)
                print('PPT页码：%s' % var_5)
                print('问题答案：%s' % var_6)
            else:
                tk.messagebox.showerror(message='讲解词是否可视只能填1或0')

    # 问答环节点击取消后调用函数
    def ask_cancel():
        entry_var1.delete(0,'end')
        entry_var2.delete(0,'end')
        entry_var3.delete(0,'end')
        entry_var4.delete(0,'end')
        entry_var5.delete(0,'end')

    #问答环节的两个button
    btn_comfirm = tk.Button(window_ask, text='确认', command=ask_comfirm)
    btn_comfirm.place(x=10, y=270)
    btn_cancel = tk.Button(window_ask, text='取消', command=ask_cancel)
    btn_cancel.place(x=150, y=270)


#主界面的两个button,选择讲解环节还是问答环节
btn_login = tk.Button(window, text='讲解环节', command=teach)
btn_login.place(x=140, y=80)
btn_sign_up = tk.Button(window, text='问答环节', command=ask)
btn_sign_up.place(x=240, y=80)

window.mainloop()





