
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mailserver = "smtp.qq.com"  #邮箱服务器地址
username_send = '2768577041@qq.com'  #邮箱用户名
password = 'xdofbhddinbcdcjf'   #邮箱密码：需要使用授权码
username_recv = '2431320433@qq.com'  

#文件读取及附件格式处理
mail = MIMEMultipart()
file=r'C:\Users\86155\PycharmProjects\python1\day13practise\计算器.html'
att = MIMEText(open(file, 'rb').read(),"base64", "utf-8")  #这个可以发送复杂的附件，比如附件为表格
att["Content-Type"] = 'application/octet-stream'
new_file='=?utf-8?b?' + base64.b64encode(file.encode()).decode() + '?='  #附件格式处理
att["Content-Disposition"] = 'attachment; filename="test.html"' #%new_file

#正文
mail.attach(att)
mail.attach(MIMEText('python计算器测试报告'))#邮件正文的内容
mail['Subject'] = '计算器测试报告'

#附件连接及发送
mail['From'] = username_send  #发件人
mail['To'] = username_recv  #收件人
smtp = smtplib.SMTP(mailserver,port=25) # 连接邮箱服务器，smtp的端口号是25
smtp=smtplib.SMTP_SSL('smtp.qq.com',port=465) #QQ邮箱的服务器和端口号
smtp.login(username_send,password)  #登录邮箱
smtp.sendmail(username_send,username_recv,mail.as_string())# 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
smtp.quit() # 发送完毕退出smtp

print ('success')
