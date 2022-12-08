print('Welcome to py_tools!')
import time
import math
import os
print('当前时间：' + time.ctime())
w = 1
while w == 1 :
    time.sleep(0.5)
    print('----------------------------------------------------------------------')
    print('1.tools \n2.\033[0;34mArch linux\033[0m \n3.关于 \n4.[施工中] \n5.退出')
    print('----------------------------------------------------------------------')
    x = int(input('请输入代码：'))
    if x == 3:
        print('Created by Albert Chen \n自豪的使用\033[0;33mPython\033[0m！')
        print("Arch Linux is the best!!! ")
    if x == 1:
        print('1.算数')
        print('2.[可能有内容]')
        x = int(input('请选择(很明显,木有选择)：'))
        if x == 1:
            print('1.加法')
            print('2.减法')
            print('3.乘法')
            print('4.除法')
            print('5.乘方')
            print('6.开方')
            print('7.退出')
            print('8.回到开始菜单')
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
            if x == 8:
                continue
    if x == 5:
        time.sleep(1)
        break
    if x == 4:
        print('都在施工了，为啥还点开？')
        time.sleep(10)
        print("算了，进来就进来吧。")
        time.sleep(1)
        x = int(input('1.Ubuntu 2.\033[0;31m发 春 模 式\033[0m 3.回到tool选择 :'))
    if x == 3:
        print('Created by Albert Chen \n自豪的使用\033[0;33mPython\033[0m！')
        time.sleep(3)
        continue
