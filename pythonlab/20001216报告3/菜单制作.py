from tkinter import *
from random import *
'''
20001216 刘旭
菜单制作

'''
root=Tk()
root.geometry('320x240')
root.title('菜单')
menubar=Menu(root)
def drawrings(): #  画五环
    import 五环
def drawgrass(): # 画三叶草
    import 三叶草
def easy(): #随机生成简单数学题目
    count1=0
    for i in range(10):
        x=randint(0,10)
        y=randint(0,10)
        print(x,'+',y,'=')
        answer=int(input('你的答案是：'))
        if x+y==answer:
            count1=count1+1
    print('您的得分为：',count1)
    if count1>=8:
        print('恭喜你闯关成功！')
    else:
        print('很遗憾未成功')
def middle(): #随机生成中等难度数学题目
    count1=0
    for i in range(100):
        x=randint(10,100)
        y=randint(10,100)
        print(x,'+',y,'=')
        answer=int(input('你的答案是：'))
        if x+y==answer:
            count1=count1+1
    print('您的得分为：',count1)
    if count1>=8:
        print('恭喜你闯关成功！')
    else:
        print('很遗憾未成功')
def difficult(): #随机生成困难数学题目
    count1=0
    for i in range(1000):
        x=randint(100,1000)
        y=randint(100,1000)
        print(x,'+',y,'=')
        answer=int(input('你的答案是：'))
        if x+y==answer:
            count1=count1+1
    print('您的得分为：',count1)
    if count1>=8:
        print('恭喜你闯关成功！')
    else:
        print('很遗憾未成功')
# 创建下拉菜单数学计算，然后将其加入到顶级菜单栏之中
mathmenu = Menu(menubar,tearoff=0)
mathmenu.add_command(label='简单题目',command=easy)
mathmenu.add_separator()
mathmenu.add_command(label='中等题目',command=middle)
mathmenu.add_separator()
mathmenu.add_command(label='困难题目',command=difficult)
menubar.add_cascade(label='数学游戏',menu=mathmenu)
#创建下拉菜单画画游戏，将其加入到顶级菜单中
drawmenu = Menu(menubar,tearoff=0)
drawmenu.add_command(label='画五环',command=drawrings)
drawmenu.add_separator()
drawmenu.add_command(label='画三叶草',command=drawgrass)
menubar.add_cascade(label='画画游戏',menu=drawmenu)
#创建下拉菜单帮助，然后将其加入到顶级栏中
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label='关于',command=print('made by 20001216 刘旭'))
helpmenu.add_separator()
helpmenu.add_command(label='关闭',command=root.destroy)
menubar.add_cascade(label='帮助',menu=helpmenu)
#显示菜单
root.config(menu=menubar)
root.mainloop()
