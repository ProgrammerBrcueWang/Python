'''
	功能： 参数的寻找  内层找不到 找外层，外层找不到找全局，
'''
c=456
def foo():
	def bar():
		print("c=",c)    #内层函数没有定义c 但是他会从内层向外边函数中找，如果还找不到则会放到全局变量中找
	bar()				 

# 主函数

if __name__ == '__main__':
	foo()
	hanshu = foo     # 给函数取别名
	print(__name__)
	# 查看内键变量
	#print(locals())  # （工作空间所有的变量）会返回一个字典
	#print(globals())
	print(foo) # 返回函数的首地址
	print(foo())  # python每个函数都有返回值 如果没有return 返回值是none
