'''
	功能: nonlocal 的使用(必须在函数内层里面) 
'''
def foo():
	b = 123
	# 内层函数
	def bar():
		nonlocal b   #必须先定义 不能定义赋值直接弄
		b = 4546
		print("b=",b)

	# 调用内层函数
	bar()
	print("b=",b)

# 主函数
foo()
