from tkinter import *

win = Tk()
win.title('监视窗口')  # 设置标题
win.geometry("700x700+200+200")  # 设置窗口大小700x700和位置+200+200，位置以屏幕左上角为原点
"""------------------------------------LABEL控件------------------------------------"""
# win:父窗口
# text:显示的文本内容
# bg:背景色
# fg:字体颜色
# font:字体
# wraplength:指定text文本多宽后换行
# justify:设置换行后的对齐方式
# anchor:位置 n北，e东，w西，s南，center中间；可以组合ne：东北
label = Label(
    win,
    text='qiubin',
    bg='#1d1919',
    fg='#226597',
    font=("黑体", 20),
    width=20,
    height=10,
    wraplength=100,
    justify='left',
    anchor='center',
)
# label.pack()  # 显示控件
"""------------------------------------BUTTON控件------------------------------------"""


def pt():
    print('binbin')


button1 = Button(win, text='打印', command=pt, width=7, height=1)
button1.pack()  # 显示按钮
button2 = Button(win, text='测试', command=lambda: print('测试成功！'))
button2.pack()
button3 = Button(win, text='退出', command=win.quit)  # 退出按钮
button3.pack()

"""------------------------------------Entry控件------------------------------------"""
entry1 = Entry(win, show='*')  # show="*"表示可以输入密码
entry1.pack()
e = Variable()
entry2 = Entry(win, bg='#c6cbef')
entry2.pack()


def showinfo():
    """输出输入内容"""
    print(entry2.get())


button4 = Button(win, text='测试输入', command=showinfo)
button4.pack()
"""------------------------------------Text控件------------------------------------"""
# 用于显示多行文本
scroll = Scrollbar()  # 滚动条
text = Text(win, width=30, height=10)
scroll.pack(side=RIGHT, fill=Y)
# text.pack(side=LEFT, fill=Y)
"""关联滚动条和Text"""
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
# text.pack()
str1 = '''盖闻天地之数，有十二万九千六百岁为一元。将一元分为十二会，乃子、丑、寅、卯、辰、
巳、午、未、申、酉、戌、亥之十二支也。每会该一万八百岁。且就一日而论：子时得阳气，而丑则鸡
鸣；寅不通光，而卯则日出；辰时食后，而巳则挨排；日午天中，而未则西蹉；申时晡而日落酉；戌黄昏
而人定亥。譬于大数，若到戌会之终，则天地昏蒙而万物否矣。再去五千四百岁，交亥会之初，则当黑
暗，而两间人物俱无矣，故曰混沌。又五千四百岁，亥会将终，贞下起元，近子之会，而复逐渐开明。邵
康节曰：“冬至子之半，天心无改移。一阳初动处，万物未生时。”到此，天始有根。再五千四百岁，正当
子会，轻清上腾，有日，有月，有星，有辰。日、月、星、辰，谓之四象。故曰，天开于子。又经五千四
百岁，子会将终，近丑之会，而逐渐坚实。易曰：“大哉乾元！至哉坤元！万物资生，乃顺承天。”至此，
地始凝结。再五千四百岁，正当丑会，重浊下凝，有水，有火，有山，有石，有土。水、火、山、石、土
谓之五形。故曰，地辟于丑。又经五千四百岁，丑会终而寅会之初，发生万物。'''
text.insert(INSERT, str1)
"""------------------------------------Checkbutton多选框控件------------------------------------"""


def update():
    message = ''
    if hobby1.get() == True:
        message += 'money\n'
    if hobby2.get() == True:
        message += 'power\n'
    if hobby3.get() == True:
        message += 'people\n'
    text.delete(0.0, END)
    text.insert(INSERT, message)


hobby1 = BooleanVar()
check1 = Checkbutton(win, text='money', variable=hobby1, command=update)
check1.pack()
hobby2 = BooleanVar()
check2 = Checkbutton(win, text='power', variable=hobby2, command=update)
check2.pack()
hobby3 = BooleanVar()
check3 = Checkbutton(win, text='people', variable=hobby3, command=update)
check3.pack()
text = Text(win, width=50, height=5)
text.pack()
"""------------------------------------Radiobutton单选框------------------------------------"""
# 一组单选框要绑定同一个变量，就能区分单选框
r = IntVar()


def pr_in():
    print(r.get())


radio1 = Radiobutton(win, text='one', value=1, variable=r, command=pr_in)
radio1.pack()
radio2 = Radiobutton(win, text='two', value=2, variable=r, command=pr_in)
radio2.pack()

"""------------------------------------Listbox控件一------------------------------------"""
# 列表框控件：可以包含一个或多个文本框
lb = Listbox(win, selectmode=BROWSE)  # BROWSE可以移动选中位置
# lb.pack()
for item in ['one', 'two', 'three', 'four']:
    lb.insert(END, item)  # END表示在后面添加
lb.insert(ACTIVE, 'cool')  # ACTIVE表示在前面添加
lb.insert(END, *["very good", "very nice"])  # 插入列表
lb.delete(1, 2)  # 删除：参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只删除第一个索引处的内容,索引从零开始
lb.select_set(2, 3)  # 选中：参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只选中第一个索引处的内容
lb.select_clear(2)  # 取消选中：参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只取消第一个索引处的内容
print(lb.size())  # 获取到列表中的元素个数
print(lb.get(2, 3))  # 获取值
print(lb.curselection())  # 返回当前的索引项，不是item元素
print(lb.select_includes(3))  # 判断：一个选项是否被选中
"""------------------------------------Listbox控件二------------------------------------"""
lbv = StringVar()
lb1 = Listbox(win, selectmode=SINGLE, listvariable=lbv)  # 与BORWSE相似，但是不支持鼠标按下后移动选中位置
# lb1.pack()
lb1.insert(END, '111')
lb1.insert(END, '222')
print(lbv.get())
lbv.set(('1', '2', '3'))


def myprint(event):
    print(lb1.get(lb1.curselection()))


lb1.bind('<Double-Button-1>', myprint)  # 双加输出选中项
"""------------------------------------Listbox控件三------------------------------------"""
lb2 = Listbox(win, selectmode=EXTENDED)  # EXTENDED：可以使listbox支持shift和Ctrl
# lb2.pack()
for item in ["good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd", "good", "nice", "handsome", "aaa", "bbb", "ccc",
             "ddd", "good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd", "good", "nice", "handsome", "aaa", "bbb",
             "ccc", "ddd", "good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd"]:
    lb2.insert(END, item)
scroll1 = Scrollbar(win)
# scroll1.pack(side=RIGHT, fill=Y)
lb2.configure(yscrollcommand=scroll1.set)
# lb2.pack(side=LEFT, fill=BOTH)
scroll1['command'] = lb2.yview
"""------------------------------------Listbox控件四------------------------------------"""
lb3 = Listbox(win, selectmode=MULTIPLE)  # MULTIPLE支持多选
# lb3.pack()
for item in ["good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd"]:
    lb3.insert(END, item)
"""------------------------------------Scale控件------------------------------------"""
# 供用户通过拖拽指示器来改变变量的值，可以水平，也可以竖直
# tickinterval刻度
scale1 = Scale(win, from_=0, to=100, orient=VERTICAL, tickinterval=20, length=200)


# scale1.pack()


# scale1.set(55)
def showscale():
    print(scale1.get())


# Button(win, text='按钮', command=showscale).pack()
"""------------------------------------Spinbox控件------------------------------------"""
# 数值范围控件
v = StringVar()


def update1():
    print(v.get())


sp = Spinbox(win, from_=0, to=100, increment=0.1, textvariable=v)  # command=updata1每调节一下就会输出一次
sp.pack()
Button(win, text='打印输出', command=update1).pack()
"""------------------------------------Menu顶层菜单------------------------------------"""
# menubar = Menu(win)
# win.config(menu=menubar)
#
#
# def func():
#     print('*****************')
#
#
# menu1 = Menu(menubar, tearoff=False)
# for item in ['python', 'c', 'java', 'c++', 'c#', 'php', 'B', '退出']:
#     if item == '退出':
#         # 添加分割线
#         # menu1.add_separator()
#         menu1.add_command(label=item, command=win.quit)
#     else:
#         menu1.add_command(label=item, command=func)
# menubar.add_cascade(label='语言', menu=menu1)
"""------------------------------------Menu鼠标右键菜单------------------------------------"""
# menubar = Menu(win)
#
#
# def func():
#     print('^^^^^^^^^')
#
#
# menu = Menu(menubar, tearoff=False)
# # 给菜单选项添加内容
# for item in ['python', 'c', 'java', 'c++', 'c#', 'php', 'B', '退出']:
#     if item == '退出':
#         # 添加分割线
#         menu.add_separator()
#         menu.add_command(label=item, command=win.quit)
#     else:
#         menu.add_command(label=item, command=func)
# menubar.add_cascade(label='语言', menu=menu)
#
#
# def showmenu(event):
#     menubar.post(event.x_root, event.y_root)
"""------------------------------------Combobox下拉控件------------------------------------"""
cv=StringVar()
com=

win.bind("<Button-3>", showmenu)

win.mainloop()  # 消息循环
