''' 素数 '''
# for n in range(2,10):
# 	count = 0
# 	for x in range(2,n):
# 		if n%x == 0:
# 			count=count+1
# 	if count==0:
# 		print("n=",n)	

for n in range(2,10):
	count = 0
	for x in range(2,n):
		if n%x == 0:
			break
	else:                    # else 指for循环所有内容都不符合时才进到else
		print("n=",n)	