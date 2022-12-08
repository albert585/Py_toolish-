import time
print("Welcome to Py_toolish!!!")
print("This is codemao version")
print('ver. 0.1b')
y = 1
while y == 1:
    x = int(input("1.计算 2. Game 3.工具 4.退出 \n你想做什么? "))
    if  x == 2 :
        y = int(input('1.单词九连猜 \n 请选择:'))
        if y == 1:
             import lives
             time.sleep(2)
    if x == 3 :
        import pwd
        repr(pwd)
        time.sleep(2)
    if x == 4:
        break



















