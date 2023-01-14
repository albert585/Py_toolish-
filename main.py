import time
import os
import math
print("Welcome to Py_toolish!!!")
print('ver. 0.1')
y = 1
while y == 1:
    x = int(input("1.计算 2. Game 3.工具 4.退出 \n你想做什么? "))
    if x == 1:
                        print('1.加法')
                        print('2.减法')
                        print('3.乘法')
                        print('4.除法')
                        print('5.乘方')
                        print('6.开方')
                        print('7.退出')
                        x = int(input('请输入代码：'))
                        if x == 1:
                                num1,num2 = eval(input("输入两个数值（用逗号隔开）："))
                                print('结果：',num1 + num2)
                        if x == 3:
                                num3,num4= eval(input("输入两个数值（用逗号隔开）："))
                                print('结果：',num3 * num4)
                        if x == 2:
                                num5,num6 = eval(input("输入两个数值（用逗号隔开）："))
                                print('结果：',num5 - num6)
                        if x == 4:
                                num7,num8 = eval(input("输入两个数值（用逗号隔开）："))
                                print('结果：',num7 / num8)
                        if x == 5:
                                num9,num0 = eval(input("输入两个数值（用逗号隔开）："))
                                print('结果：',(num9 , num0))
                        if x == 6:
                                num11 = int(input("输入数值："))
                                print('结果：',math.sqrt(num11))
                        if x == 7:
                                break

    if  x == 2 :
        y = int(input('1.单词九连猜 \n 请选择:'))
        if y == 1:
             os.system("python ./src/lives.py")
             time.sleep(2)
    if x == 3 :
        print("1.密码生成器 \n2.Tmoe \n3.其他")
        z = int(input("please choose："))
        if z == 2:
            os.system("bash -c "$(curl -Lv gitee.com/mo2/linux/raw/master/debian.sh)"")
        if z == 1:
            os.system("python ./src/pwd.py")
        time.sleep(2)
    if x == 4:
        break



















