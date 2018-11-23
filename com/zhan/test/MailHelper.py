#encoding: utf-8

import smtplib
from pyh import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from lxml import etree

def sendMail(configFile,projectname,result,url,path):
    html = etree.parse(configFile)
    mailconfig = html.xpath('//config/mailServer')[0]
    sender = mailconfig.find('sender').text
    receiver = mailconfig.find('receiver').text
    username = mailconfig.find('username').text
    password = mailconfig.find('password').text
    smtpserver = mailconfig.find('smtpserver').text

    msg = MIMEMultipart('related')
    msg['Subject'] = Header("%s API Test Report"%projectname, 'utf-8')
    __createHtml(result,url,path,projectname)
    html = open(path,mode='r').read()
    msg.attach(MIMEText(html, 'html', 'utf-8'))

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

def __createHtml(result,url,path,projectname):
    page = PyH('Report')
    page << h1('%s APITestReport'%projectname, cl='center')
    page << p('Passed:%s'%(result['passed']))
    page << p('Failed:%s'%(result['failed']))
    page << p('API Detail Report:')
    page << a(url,href=url)
    page << p(u"Please use Chrome,FireFox,IE11 to view this report.Thanks!")
    page.printOut(file=path,encodetype="utf-8")

def MailTo(txt):
    sender = 'sendermail'
    receiver = '85224271@qq.com'
    username = 'sendermail'
    password = 'senderpass'
    smtpserver = 'smtp.exmail.qq.com'

    msg = MIMEMultipart('related')
    msg['Subject'] = Header("PublicClass Live Login Fail", 'utf-8')
    msg.attach(MIMEText(txt, 'html', 'utf-8'))

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

