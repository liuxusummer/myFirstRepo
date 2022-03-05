# 密码验证
from tkinter import *

root = Tk() #创建窗体
root.title('密码验证') # 创建标题
root.geometry('350x150') # 设置窗体大小
def verify(): # 用来确认密码是否正确
    if(E1.get()=='admin' and E2.get()=='123456'):
        print('密码正确，欢迎进入')
        root.destroy()
        
        import 菜单制作
       
    else:
        print('密码错误，请重试')
L1 = Label(root,text='用户名:') # 创建用户名标签
L1.place(x=10,y=10) # 设置大小
E1=Entry(root,bd=5,font=12,width=15) # 设置输入框
E1.place(x=65,y=10)
L2=Label(root,text='密    码:')
L2.place(x=10,y=60)
E2=Entry(root,bd=5,font=12,width=15,show='*')
E2.place(x=65,y=60)
B1=Button(root,text='验证密码信息',width=15,command=verify)# 设置验证按钮
B1.place(x=65,y=100)
root.mainloop()
