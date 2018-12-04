from chardet import detect
count,blanks = 0,0

# rb是以二进制内容来读
with open("a.txt",'rb') as fp:   # rb以二进制文件读取(这样就可以无视编码方式了)
	# 检测文件编码 编码信息保存到code
	code = detect(fp.read())['encoding']
	print(code)

with open("a.txt",'r',encoding=code) as fp:   #encoding 的值变为获取到的的文件编码格式
	while True:
		line = fp.readline()    # readline 这个L必须小写
		if not line:			# 有内容时，not line 为flase 无内容 not line 为ture
			break

		length = (len(line.strip()))  # strip(剥夺) 函数 计算长度时不计算(只是字符串两边)所有不可打印字符
		print(length)
		if length==0:
			blanks+=1
		count+=1

print(" 有内容的行数为：",count,'\n',"空行为：",blanks)

	#detect(fp.read())  # detect是探测的意思
	#print(detect(fp.read())['encoding'])  # detect是探测的意思
	#print(fp.read())

