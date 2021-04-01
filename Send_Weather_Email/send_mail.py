import smtplib
import ssl
import json
from email.mime.text import MIMEText
from email.header import Header
from email.message import EmailMessage


def send_mail(email_content):
    """
    receiver : str
    email_conten : dict, 包括 'subject', 'main_message'  （主题，正文）
    """

    with open("information.json", 'r', encoding='UTF-8') as f:
        information = json.load(f)
        f.close()

    from_address = information["sender"]["from_address"]
    to_address   = information["receiver"]["to_address"]
    password     = information["sender"]["password"]
    name         = information["sender"]["name"]

    subject      = email_content["subject"]
    main_message = email_content["main_message"]

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message            =  MIMEText(main_message, "plain", "utf-8")
    message["from"]    =  Header(name, "utf-8")                     # 发送者
    message["to"]      =  Header(to_address, "utf-8")               # 接受者
    message["subject"] =  Header(subject, "utf-8")                  # 邮件主题

    try:
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", port=465)
        smtpObj.login(from_address, password)
        smtpObj.sendmail(from_address, [to_address], message.as_string())
        print("发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")