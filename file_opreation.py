import os
root_path = os.getcwd()			#获取当前目录  
offset = len(root_path.split("\\"))
print(root_path," ",offset)     # 获取文件夹的层数
# 返回文件夹 子目录 和文件
for root,dirs,files in os.walk(root_path):
	current_dir = root.split("\\")
	indent = len(current_dir)-offset
	print("\t"*indent,"\\"+current_dir[-1])
	for f in files:
		print("\t"*(indent+1),f)