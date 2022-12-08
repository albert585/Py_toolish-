print('Welcome!')
import time
import math
print('当前时间：' + time.ctime())
w = 1
while w == 1 :
	print('1.tools 2.[开发中] 4.exit')
	x = int(input('请输入代码：'))
	if x == 1:
		print('py tools v0.5')
		print('1.算数')
		x = int(input('请选择(很明显,木有选择)：'))
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
	if x == 4:
		break
