'''
	所有的邮件都是以smtp协议发送的
	MIME 多用途互联网邮件扩展
'''
import smtplib
from email.mime.text import MIMEText # 构建邮件的正文
from email.header import Header  # 收件人 发件人的主题信息
from email.mime.multipart import MIMEMultipart  # Multipart 带附件的邮件 每一个附件都是一个part
from email.mime.base import MIMEBase  # 每一个MIMEBase 对应一个附件
from email import encoders

def add_attachment(file):
	with open(file,"r") as fp:
		mime = MIMEBase('application','octect-string',filename=file)  #1、指定对象是什么类型 2以什么方式发送octect-string'(八进制类型)
		# Disposition处理方式 用attachment(附件的意思) 方式
		mime.add_header("Content-Disposition",'attachment',filename=file)  # 添加附件头部
		mime.add_header("Content-ID","<0>")
		mime.add_header("X-attachment-Id","0") #告诉浏览器 用什么指定的程序去打开
		mime.set_payload(fp.read()) #把附件内容写进来 
		encoders.encode_base64(mime)  #base64 是一种编码格式 类似于utf-8
		att_msg.attach(mime)


from_addr = "1016709328@qq.com"
to_addr = "1016709328@qq.com"
sever_addr = "smtp.qq.com"
psw = 'ygramkdesmivbdcd'

# 创建邮件的正文对象
contents = "Hello world"
msg = MIMEText(contents,'plain','utf-8')
# msg['From'],msg['To'] = from_addr,to_addr
# msg['Subject'] = "Test"

# 创建带附件的邮件对象
att_msg = MIMEMultipart()
# 第一部分是正文对象  用attach(系 用绳子系) 方法

att_msg['From'],att_msg['To'] = from_addr,to_addr
att_msg['Subject'] = "Test"
att = ["test.txt","test2.txt"]
att_msg.attach(msg)  # 将正文添加到带附件的邮件里面

for a in att:
	add_attachment(a)

# with open("test.txt","r") as fp:
# 	mime = MIMEBase('application','octect-string',filename=file)  #1、指定对象是什么类型 2以什么方式发送octect-string'(八进制类型)
# 	# Disposition处理方式 用attachment(附件的意思) 方式
# 	mime.add_header("Content-Disposition",'attachment')  # 添加附件头部
# 	mime.add_header("Content-ID","<0>")
# 	mime.add_header("X-attachment-Id","0") #告诉浏览器 用什么指定的程序去打开
# 	mime.set_payload(fp.read()) #把附件内容写进来 
# 	encoders.encode_base64(mime)  #base64 是一种编码格式 类似于utf-8
# 	att_msg.attach(mime)

# 创建服务器链接句柄
sever = smtplib.SMTP(sever_addr,25)
sever.login(from_addr,psw)
sever.sendmail(from_addr,[to_addr],att_msg.as_string())  # 可以发给多个人
sever.quit() #最后退出服务器

