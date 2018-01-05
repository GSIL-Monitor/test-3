#encoding: utf-8

import pymysql.cursors
import pymssql
from lxml import etree

conn = None
cursor = None

html = etree.parse('C:\\Users\\Administrator\\PycharmProjects\\test\\tests\\corpus\\config\\config.xml')
result = html.xpath('//config/database')
if len(result) == 0:
    raise NameError("database not config")

host = result[0].find('host').text
port = int(result[0].find('port').text) if result[0].find('port').text <> None else None
username = result[0].find('username').text
password = result[0].find('password').text
db = result[0].find('db').text

if result[0].get('name') == 'sqlserver':
    conn = pymssql.connect(host=host, user=username, password=password, database=db, charset="utf8")
elif result[0].get('name') == 'mysql':
    conn = pymysql.connect(host=host, port=port, user=username, password=password, database=db, charset="utf8",
                           cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()


def getValueBySql(sql):
    cursor.execute(sql)
    # 查询数据库单条数据
    result = cursor.fetchone()
    return result

def closeConn():
    conn.close()

