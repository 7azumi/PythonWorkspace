import tkinter


# 创建窗口
win = tkinter.Tk()
# 添加标题
win.title("人生苦短，我用Python")
# 设置窗口大小及位置
win.geometry("450x300+300+240")

'''
Lable控件：

text:显示的文本
bg:背景色
fg:字体色

'''
# 创建lable
labe1 = tkinter.Label(win,
                      text="A simple example for Lable",
                      bg='pink',
                      fg='blue',
                      font=('consolas',15))
# 挂载lable
labe1.pack()


'''
Button控件:



'''
def func():
    print("Press button1")

# 创建Button
button1 = tkinter.Button(win,
                         text='按钮',
                         command=func,
                         width=8,
                         )
# 挂载Button




button1.pack()



win.mainloop()