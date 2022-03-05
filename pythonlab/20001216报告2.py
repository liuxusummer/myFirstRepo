from tkinter import*
'''
20001216 刘旭
这是一个简易的计算器程序

'''

root = Tk()

#设置窗口的长宽

root.geometry('400x480')

#设置标题

root.title("简易计算器")

#定义显示框属性

frame_shownum = Frame(width=400, height=250)

frame_shownum.pack()

#定义顶部区域

sv = StringVar() #使字符串显示在显示框上

sv.set('0') #设置字符串



#定义显示字符串的标签,justify设置字符串对齐方式，anchor设置控件的锚点

show_label = Label(frame_shownum, textvariable=sv, bg='white', width=12, height=1, font=("黑体", 20, 'bold'),\

justify=LEFT, anchor='e')
show_label.pack(padx=10, pady=10)

#设置按键

num1 = ''

num2 = ''

operator = None

s = '' #定义了一个字符串，目的是方便delete（）使用

def delete(): # 实现删除功能

    global num1 # global设置全局变量

    global num2

    global operator

    global s;

    if operator == None:

        num1 = num1[:-1] # 利用切片法删除最后一个字符串，

        sv.set(num1) # 显示数字

    else:
        s = s[:-1]

    if(s ==''):

        operator = None

        sv.set(num1+s)
        
# 清楚功能的实现
def clear():
    global num1
    global num2
    global operator
    num1 = ''
    num2 = ''
    operator = None
    sv.set('0') # 显示0

 # 输入框中显示公式   
def change(num):

    global num1

    global num2

    global operator

    global l

    if operator == None:

        num1 = num1 + num

        sv.set(num1)

    else:

        num2 = num2 + num

        l = operator + num2

        sv.set(num1+operator+num2)

# 运算符功能实现
def operation(op):

    global operator

    if op in ['+','-','*','/']:

        operator = op

    if operator == '+':

        sv.set(int(num1)+int(num2))

    if operator == '-':

        sv.set(int(num1)-int(num2))

    if operator == '*':

        sv.set(int(num1)*int(num2))

    if operator == '/':

        sv.set(int(num1)/int(num2))


# 创建面板二

frame_bord= Frame(width=400, height=450)

#设计功能键

b_del = Button(frame_bord, text="删除", width=6, height=2, command=delete)

b_del.grid(row=3, column=3,sticky=S) # 按键布局

b_clear = Button(frame_bord, text="清除", width=6, height=2, command=clear).grid(row=3, column=3,sticky=N)

#设计数字键

b_1 = Button(frame_bord, text="1", width=6, height=4,command=lambda:change("1")).grid(row=0, column=0)

b_2 = Button(frame_bord, text="2", width=6, height=4,command=lambda:change("2")).grid(row=0, column=1)

b_3 = Button(frame_bord, text="3", width=6, height=4,command=lambda:change("3")).grid(row=0, column=2)

b_4 = Button(frame_bord, text="4", width=6, height=4,command=lambda:change("4")).grid(row=0, column=3)

b_5 = Button(frame_bord, text="5", width=6, height=4,command=lambda:change("5")).grid(row=1, column=0)

b_6 = Button(frame_bord, text="6", width=6, height=4,command=lambda:change("6")).grid(row=1, column=1)

b_7 = Button(frame_bord, text="7", width=6, height=4,command=lambda:change("7")).grid(row=1, column=2)

b_8 = Button(frame_bord, text="8", width=6, height=4,command=lambda:change("8")).grid(row=1, column=3)

b_9 = Button(frame_bord, text="9", width=6, height=4,command=lambda:change("9")).grid(row=2, column=0)

b_0 = Button(frame_bord, text="0", width=6, height=4,command=lambda:change("0")).grid(row=2, column=1)

#设计运算符号

b_add = Button(frame_bord, text="+", width=6, height=4,command=lambda:operation("+")).grid(row=2, column=2)

b_sub = Button(frame_bord, text="-", width=6, height=4,command=lambda:operation("-")).grid(row=2, column=3)

b_mul = Button(frame_bord, text="*", width=6, height=4,command=lambda:operation("*")).grid(row=3, column=0)

b_div= Button(frame_bord, text="/", width=6, height=4,command=lambda:operation("/")).grid(row=3, column=1)

b_equ = Button(frame_bord, text="=", width=6, height=4,command=lambda:operation("=")).grid(row=3, column=2)

frame_bord.pack(padx=10, pady=10)

root.mainloop()
