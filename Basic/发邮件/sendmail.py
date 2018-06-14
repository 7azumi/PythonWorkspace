# 发邮件的库
import smtplib
# 邮件文本
from email.mime.text import MIMEText

# 服务器地址
SMTPServer = "smtp.163.com"
# 发送者地址
sender = "m15023628954@163.com"
# 发送者授权码
passwd = "Fengliu13"


# 发送内容
message = "wooooo~~~~Hooooooo~~~~~~"
# MIME格式内容
msg = MIMEText(message)
# 主题
msg['Subject'] = "From Orange"
# 发送者
msg['From'] = sender


# 创建SMTP服务器
mailserver = smtplib.SMTP(SMTPServer, 25)
# 登录邮箱
mailserver.login(sender, passwd)
# 发送邮件
mailserver.sendmail(sender, [sender,"15202977084@163.com","louis__xiv@outlook.com"],msg.as_string())
# 退出邮箱
mailserver.quit()

