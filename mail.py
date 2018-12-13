'''
	所有的邮件都是以smtp协议发送的
'''
import smtplib
from email.mime.text import MIMEText # 构建邮件的正文
from email.header import Header  # 收件人 发件人的主题信息

from_addr = "1016709328@qq.com"
to_addr = "1016709328@qq.com"
sever_addr = "smtp.qq.com"
psw = 'ygramkdesmivbdcd'

contents = "Hello world"
msg = MIMEText(contents,'plain','utf-8')
msg['From'],msg['To'] = from_addr,to_addr
msg['Subject'] = "Test"

#创建服务器链接句柄
sever = smtplib.SMTP(sever_addr,25)
sever.login(from_addr,psw)
sever.sendmail(from_addr,[to_addr],msg.as_string())  # 可以发给多个人
sever.quit() #最后退出服务器

