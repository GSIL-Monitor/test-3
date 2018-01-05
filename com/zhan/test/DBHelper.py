#encoding: utf-8

import pymysql.cursors
import pymssql
from lxml import etree
from com.zhan.test.publicData import publicData


class DatabaseConn:
    conn = None
    cursor = None

    @staticmethod
    def init():
        DatabaseConn.conn = None
        DatabaseConn.cursor = None
        pd = publicData()
        html = etree.parse("%s/config/config.xml" % (pd.getMainDir()))
        result = html.xpath('//config/database')
        if len(result) == 0:
            raise NameError("database not config")

        host = result[0].find('host').text
        port = int(result[0].find('port').text) if result[0].find('port').text <> None else None
        username = result[0].find('username').text
        password = result[0].find('password').text
        db = result[0].find('db').text

        if result[0].get('name') == 'sqlserver':
            DatabaseConn.conn = pymssql.connect(host=host, user=username, password=password, database=db, charset="utf8")
        elif result[0].get('name') == 'mysql':
            DatabaseConn.conn = pymysql.connect(host=host, port=port, user=username, password=password, database=db, charset="utf8",
                                   cursorclass=pymysql.cursors.DictCursor)
        DatabaseConn.cursor = DatabaseConn.conn.cursor()


    @staticmethod
    def getValueBySql(sql):
        DatabaseConn.cursor.execute(sql)
        # 查询数据库单条数据
        result = DatabaseConn.cursor.fetchone()
        return result

    @staticmethod
    def closeConn():
        DatabaseConn.conn.close()


# DatabaseConn.init()
# print DatabaseConn.getValueBySql("select * from Tpo_PublicClass_Activities where StartTime >= CAST('2017-06-01' as date)  and endtime <= CAST('2017-07-01' as date) ")
# # print getValueBySql("select * from tbl_toefl_practice_article a where a.id = 3")


