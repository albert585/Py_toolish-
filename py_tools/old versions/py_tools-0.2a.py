print ("Welcome!")
import time
import kitten
print(time.ctime())
x = int(input('1.tools 2.[开发中] 3.pyglet test '))
if x == 1:
	print('py tools v0.0.1')
	print('1.简单算数')
	x = int(input('请选择(很明显,木有选择): '))
	if x == 1:
		print('1.+')
		print('2.-')
		print('3.*')
		print('4./')
		print('5.乘方')
		x = int(input('请选择: '))
		if x == 1:
			x= float(input('请输入加数:'))
			y= float(input('请输入加数2:'))
			plus1 = x
			plus2 = y
			print (plus1 + plus2)
		if x == 3:
			x= float(input('请输入乘数:'))
			y= float(input('请输入乘数2:'))
			chen1 = x
			chen2 = y 
			print(chen1*chen2)
		if x == 2:
			x= float(input('请输入被减数:'))
			y= float(input('请输入减数:'))
			print(x - y)
		if x == 4 :
			x= float(input('请输入被除数:'))
			y= float(input('请输入除数:'))
			chu1 = x 
			chu2 = y 
			print (chu1/chu2)
		if x == 5:
			x= float(input('请输入乘数:'))
			y= float(input('请输入乘数2:'))
			chen1 = x
			chen2 = y 
			print (chen1 ** chen2)
if x == 2: 
 pass
if x == 3:
	print ('请确保已安装pyglet和AVBin!!')
	print('请确保文件名为audio或video')
	x == int(input('如已准备就绪,按1开始'))
	if x == 1 :
		pass
