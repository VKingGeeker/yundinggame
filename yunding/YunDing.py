import os
import threading
import time
import tkinter
from tkinter import ttk
from tkinter import *
from urllib import request, parse
import json

rightCookie = ""
buyReq = request.Request('http://joucks.cn:3344/api/byPalyerGoods')
isStop = False


def checkToken(cookie):
    """
    检测cookie是否可用
    :param cookie:
    :return:
    """
    req = request.Request('http://joucks.cn:3344/api/getSellGoods?pageIndex=1&tid=all')
    req.add_header('Cookie', cookie)
    with request.urlopen(req) as f:
        jsonStr = f.read().decode('utf-8')
        jsonObj = json.loads(jsonStr)
        if jsonObj['data'] is None:
            return False
        else:
            global rightCookie
            rightCookie = cookie
            buyReq.add_header('Cookie', cookie)
            return True


def gui_arrang(self):
    self.token_input.pack()
    self.result_button.pack()


def get_screen_size(window):
    return window.winfo_screenwidth(), window.winfo_screenheight()


def get_window_size(window):
    return window.winfo_reqwidth(), window.winfo_reqheight()


def start_clean_func_ByName_thread(goods_method, goods_name, kind_name, price_method, compare, goods_price, treeview,
                                   current_status_label):
    """
    该方法为了防止按下开始按钮后程序无响应
    :param goods_name:
    :param price_method:
    :param compare:
    :param goods_price:
    :param treeview:
    """
    global isStop
    isStop = False
    th = threading.Thread(target=start_clean_func_ByName,
                          args=(goods_method, goods_name, kind_name, price_method, compare, goods_price, treeview,
                                current_status_label))
    th.setDaemon(True)  # 守护线程
    th.start()


def start_clean_func_ByName(goods_method, goods_name, kind_name, price_method, compare, goods_price, treeview,
                            current_status_label):
    """
    扫货方法
    :param goods_method: 根据什么搜索
    :param goods_name: 物品名
    :param kind_name: 分类名
    :param price_method: 根据单价or总价
    :param compare: 大于、小于、等于
    :param goods_price: 价格范围
    :param treeview: 表格
    """
    # 此处页码需遍历

    x = 1
    while True:
        global isStop
        if isStop:
            break
        y = 1
        while True:
            if isStop:
                break
            if goods_method == 1:
                req = request.Request('http://joucks.cn:3344/api/getSellGoods?pageIndex=' + str(y) + '&tid=all')
            else:
                req = request.Request(
                    'http://joucks.cn:3344/api/getSellGoods?pageIndex=' + str(y) + '&tid=' + kind_name)
            req.add_header('Cookie', rightCookie)
            with request.urlopen(req) as f:
                jsonStr = f.read().decode('utf-8')
                jsonObj = json.loads(jsonStr)
                usersSell = jsonObj['data']['playerSellUser']

                if len(usersSell) != 0:
                    for ele in usersSell:
                        # 此处装备类都没有goods
                        user = ele['user']['nickname']
                        id = ele['_id']
                        if ele['goods'] is not None:
                            goods = ele['goods']['name']
                        else:
                            goods = ""
                        price = float(ele['game_gold'])
                        count = ele['count']
                        avg_price = price / count
                        # print("user:" + user + "\t名称:" + goods + "\t价格：" + str(avg_price) + "\t 数量：" + str(count))
                        if price_method == 1:
                            if compare == "大于":
                                compareRes = (avg_price > goods_price)
                            elif compare == "等于":
                                compareRes = (avg_price == goods_price)
                            else:
                                compareRes = (avg_price < goods_price)
                        else:
                            if compare == "大于":
                                compareRes = (price > goods_price)
                            elif compare == "等于":
                                compareRes = (price == goods_price)
                            else:
                                compareRes = (price < goods_price)
                        if goods_method == 1:
                            goods_condition = (goods == goods_name)
                        else:
                            goods_condition = True
                        if compareRes and goods_condition:
                            buy_data = parse.urlencode({'usgid': id})
                            with request.urlopen(buyReq, data=buy_data.encode('utf-8')) as g:
                                weaponJson = g.read().decode('utf-8')
                                weaponObj = json.loads(weaponJson)
                                goods_name = weaponObj['data']['name']
                                treeview.insert('', 'end', values=(user, goods_name, price, count))
                                print("user:" + user + "\t名称:" + goods_name + "\t价格：" + str(price) + "\t 数量：" + str(
                                    count))
                                time.sleep(0.5)
                    current_status_label.config(text="当前状态：第" + str(x) + "次循环," + "第" + str(y) + "页")
                    print("第" + str(y) + "页")
                    y += 1
                    time.sleep(1)
                else:
                    break
        x += 1
        print("第" + str(x) + "次循环")
        if x % 50 == 0:
            time.sleep(5)
        else:
            time.sleep(1)


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 3)
    print(size)
    root.geometry(size)


def stop_clean_func(current_status_label):
    global isStop
    isStop = True
    current_status_label.config(text="当前状态：停止")
    # print("到这"+str(isStop))


def intoFunc(root_res_label, root, token):
    # 此处写cookie验证
    if checkToken(token):

        fq = open(os.getcwd() + '\\token', 'w', encoding="utf-8")
        fq.write(token)
        fq.close()
        # 打开新窗口前关闭上一个窗口
        root.destroy()
        func = Tk()
        func.title("云顶工具—功能页")
        func.resizable(0, 0)
        center_window(func, 900, 600)

        # 单选框(第一组)
        v = IntVar()
        v.set(1)
        raido1 = Radiobutton(func, text='根据物品名(武器类无效)：', variable=v, value=1)
        raido1.pack(anchor=W)
        raido1.place(x=30, y=5)
        raido2 = Radiobutton(func, text='根据物品类别：', variable=v, value=2)
        raido2.pack(anchor=W)
        raido2.place(x=30, y=40)

        # 根据名称文本框
        goods_name_text = tkinter.Entry(func, width=15, font=123)
        goods_name_text.pack()
        goods_name_text.place(x=200, y=5)

        # 根据分类下拉列表
        kindStr = tkinter.StringVar()  # 窗体自带的文本，新建一个值
        kindStrMap = {'全类目': 'all',
                      '材料类': '5db663b34682c5567589308b',
                      '装备类': '2',
                      '打造书': '5db663c84682c5567589308d',
                      '打造铁': '5db663d04682c5567589308e',
                      '宠物类': '5db663e24682c55675893090',
                      '皮毛类': '5dbd0bec43a0da0d3f4b1001',
                      '植物类': '5dd4f2e69d78d6163b6fd556',
                      '技能书': '5dedb5a0f21c607ea82ba0a3',
                      '烹饪类': '5df08747f4147a6cfaf6e2ad',
                      '炼药类': '5df08765af0ec237e0bfcbb6'
                      }

        def go1(*args):  # 处理事件，*args表示可变参数
            print(kindlist.get())  # 打印选中的值

        def go2(*args):  # 处理事件，*args表示可变参数
            print(comparelist.get())  # 打印选中的值

        kindlist = ttk.Combobox(func, textvariable=kindStr, state='readonly', width=13)
        kindlist["values"] = ("全类目", "材料类", "装备类", "打造书", "打造铁", "宠物类", "皮毛类", "植物类", "技能书", "烹饪类", "炼药类")
        kindlist.current(0)  # 选择第一个
        kindlist.bind("<<ComboboxSelected>>", go1)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
        kindlist.pack()
        kindlist.place(x=200, y=40)

        # 单选框(第二组)
        m = IntVar()
        m.set(2)
        raido4 = Radiobutton(func, text='根据总价', variable=m, value=2)
        raido4.pack(anchor=W)
        raido4.place(x=370, y=5)
        raido3 = Radiobutton(func, text='根据单价', variable=m, value=1)
        raido3.pack(anchor=W)
        raido3.place(x=370, y=40)

        # 价格下拉列表运算符选项
        compareStr = tkinter.StringVar()
        comparelist = ttk.Combobox(func, textvariable=compareStr, state='readonly', width=5)
        comparelist["values"] = ("大于", "小于", "等于")
        comparelist.current(0)  # 选择第一个
        comparelist.bind("<<ComboboxSelected>>", go2)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
        comparelist.pack()
        comparelist.place(x=460, y=7)

        # 价格文本框
        goods_price_text = tkinter.Entry(func, width=7, font=123)
        goods_price_text.pack()
        goods_price_text.place(x=530, y=7)

        # 价格单位
        goods_price_label = tkinter.Label(func, width=5, height=1, text="金叶")
        goods_price_label.pack()
        goods_price_label.place(x=600, y=7)

        frame = Frame(func)
        frame.place(x=30, y=100, width=850, height=430)
        columns = ("用户名", "物品名", "价格", "数量")
        # 滚动条
        scrollBar = tkinter.Scrollbar(frame)
        scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        treeview = ttk.Treeview(frame, height=20, show="headings", columns=columns, yscrollcommand=scrollBar.set)  # 表格
        scrollBar.config(command=treeview.yview)

        treeview.column("用户名", width=220, anchor='center')  # 表示列,不显示
        treeview.column("物品名", width=220, anchor='center')
        treeview.column("价格", width=210, anchor='center')
        treeview.column("数量", width=180, anchor='center')
        treeview.heading("用户名", text="用户名")  # 显示表头
        treeview.heading("物品名", text="物品名")
        treeview.heading("价格", text="价格")
        treeview.heading("数量", text="数量")

        # 开始按钮
        goods_clean_start_button = tkinter.Button(func,
                                                  command=lambda: start_clean_func_ByName_thread(v.get(),
                                                                                                 goods_name_text.get(),
                                                                                                 kindStrMap.get(
                                                                                                     kindStr.get(), ""),
                                                                                                 m.get(),
                                                                                                 compareStr.get(),
                                                                                                 float(
                                                                                                     goods_price_text.get()),
                                                                                                 treeview,
                                                                                                 current_status_label),
                                                  text="开始",
                                                  width=10)
        goods_clean_start_button.pack()
        goods_clean_start_button.place(x=650, y=35)

        # 结束按钮
        goods_clean_end_button = tkinter.Button(func, command=lambda: stop_clean_func(current_status_label), text="结束",
                                                width=10)
        goods_clean_end_button.pack()
        goods_clean_end_button.place(x=750, y=35)

        treeview.pack()
        treeview.place()

        # 当前状态
        current_status_label = tkinter.Label(func, width=30, height=1, text="当前状态：停止", anchor=NW)
        current_status_label.pack()
        current_status_label.place(x=30, y=540)

        func.mainloop()
    else:
        root_res_label.config(text='cookie不正确')


# -------------------------------进入页-------------
def main():
    # 创建主窗口,用于容纳其它组件
    root = tkinter.Tk()

    # 给主窗口设置标题内容
    root.title("云顶工具—验证页")
    root.resizable(0, 0)
    center_window(root, 500, 170)
    # menu = tkinter.Menu(title='aaa')
    cookie_label = tkinter.Label(root, text="在下面输入浏览器获取到的cookie:")
    root_res_label = tkinter.Label(root, text='')

    # 创建一个输入框,并设置尺寸
    cookie_text = tkinter.Text(root, width=50, height=5)
    # 创建一个查询结果的按钮
    cookie_label.pack()
    cookie_text.pack()

    root_res_label.pack()
    cookie_label.place(relx=0.3, rely=0.1)
    cookie_text.place(relx=0.15, rely=0.25)

    root_res_label.place(relx=0.8, rely=0.75)

    if not os.path.exists(os.getcwd() + '\\token'):
        fd = open(os.getcwd() + '\\token', 'w', encoding="utf-8")
        fd.close()
    with open(os.getcwd() + '\\token') as f:
        str = f.read()

    cookie_text.insert(tkinter.INSERT, str)
    # str = g.read()
    result_button = tkinter.Button(root, command=lambda: intoFunc(root_res_label, root,
                                                                  cookie_text.get(0.1, END).replace("\n", "")),
                                   text="进入",
                                   width=30)
    # result_button.bind()
    # print(token_text.get(1.0, END))
    result_button.pack()
    result_button.place(relx=0.3, rely=0.75)
    # 完成布局
    root.mainloop()


if __name__ == '__main__':
    main()
