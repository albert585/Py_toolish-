import os
print("Py_toolish! \nWelcome!")
y = 0
def command(common):
    os.system(common)
def command2(y):
    while y == 1:
        common=str(input(">"))
        command(common)
        if common =="exit":
            y=-1
def worldz():
    if os.path.exists("/usr/bin/banner"):
        os.system("banner WorldZ!")
    else:
        os.system("sudo pacman -Syyu banner")
        os.system("banner WorldZ!")     
while True:
    x=str(input("fakeshell>"))
    if x=="help":
        print("ver:显示版本 \nexit/quit:退出 \nconsole:启动控制台 \ntools工具")
    if x=="console":
        y=+1
        command2(y)
    if x=="exit":
        break
    if x=="quit":
        break
    if x=="worldz":
        worldz()
    if x=="ver":
        print("Py_toolish cli 0.0.1a")
        os.system("python3 --version")
        os.system("uname -a")
    if x=="tools":
        os.system("python ./main.py")