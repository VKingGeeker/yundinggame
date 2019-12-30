"""
@Author : 行初心
@Date   : 18-10-1
@Blog   : www.cnblogs.com/xingchuxin
@Gitee  : gitee.com/zhichengjiu
"""
from tkinter import *

def clickFunc(v):
    print(v.get())
def main():
    root = Tk()

    v = IntVar()
    v.set(2)  # 如果1，那么儒家被默认选中
    # 如果2，那么道家被默认选中
    # 如果3，那么佛家被默认选中

    rb1 = Radiobutton(root, text='儒家', command=lambda:clickFunc(v),variable=v, value=1)
    rb1.pack()

    rb2 = Radiobutton(root, text='道家', command=lambda:clickFunc(v),variable=v, value=2)
    rb2.pack()

    rb3 = Radiobutton(root, text='佛家',command=lambda:clickFunc(v), variable=v, value=3)
    rb3.pack()

    mainloop()


if __name__ == '__main__':
    main()