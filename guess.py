import random 
start = input('请决定随机数字开始值: ')
end = input('请决定随机数字结束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end) #randint函数
count = 0
while True:
	count += 1 # count = count = 1
	num = input('请输入一个数字: ')
	num = int(num)
	if num == r:
		print('你猜对了!')
		print('这是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案要大，请重试')
	elif num < r:
		print('比答案要小，请重试')
	print('这是你猜的第', count, '次')


# standrad library 标准化函数库
#程序尽量轻一点 light - weight 
# module 模组 python档案， package套件 
