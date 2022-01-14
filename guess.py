import random 

r = random.randint(1, 100) #randint函数
while True:
	num = input('请输入一个数字: ')
	num = int(num)
	if num == r:
		print('你猜对了!')
		break
	elif num > r:
		print('比答案要大，请重试')
	elif num < r:
		print('比答案要小，请重试')


# standrad library 标准化函数库
#程序尽量轻一点 light - weight 
# module 模组 python档案， package套件 
