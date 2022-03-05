Factor=(7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2) # 按顺序存储17位系数
Last=('1','0','X','9','8','7','6','5','4','3','2') # 结果对应的身份证号校验码
while True: # 做死循环
    ID=input('请输入18位身份证号码，输入0退出程序：')
    if ID == '0':
        break
    if (len(ID)!=18):
        print('输入身份证位数有误，请重新输入')
        continue # 返回输入步骤
    else:
        for i in range(0,17):
            Sum=0
            Sum+=int(Factor[i])*int(ID[i]) # 计算相加结果
        d = Sum % 11
        print('校验码%s'%Last[d])
        Lastchar=ID[17]
        Lastchar=Lastchar.upper # 如果是字母，则变为大写，可兼容输入大小写x
    if Lastchar == Last[d]:
        print(ID,'为合法身份证，',end='')
        if int(ID[-2])%2 == 0: # 判断性别
            print('性别为女')
        else:
            print('性别为男')
    else:
        print(ID,'为非法身份证号码')
            
    
