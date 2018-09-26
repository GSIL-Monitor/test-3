# #encoding: utf-8
from com.zhan.test.publicData import publicData
from lxml import etree
import pymssql,pymysql
from .Singleton import Singleton

# # 单例
# class Singleton(object):
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kw)
#         return cls._instance

@Singleton
class DBConn(object):
    __conn = None
    __cursor = None

    def __init__(self):
        if self.__cursor == None and self.__cursor == None:
            pd = publicData.instance()
            html = etree.parse(r"%s\config\config.xml" % (pd.getMainDir()))
            result = html.xpath('//config/database')
            if len(result) == 0:
                raise NameError("database not config")

            host = result[0].find('host').text
            port = int(result[0].find('port').text) if result[0].find('port').text != None else None
            username = result[0].find('username').text
            password = result[0].find('password').text
            db = result[0].find('db').text

            if result[0].get('name') == 'sqlserver':
                self.__conn = pymssql.connect(host=host, user=username, password=password, database=db, charset="utf8")
            elif result[0].get('name') == 'mysql':
                self.__conn = pymysql.connect(host=host, port=port, user=username, password=password, database=db, charset="utf8",
                                            cursorclass=pymysql.cursors.DictCursor)
            self.__cursor = self.__conn.cursor()

    def getValueBySql(self,sql):
        self.__cursor.execute(sql)
        # 查询数据库单条数据
        result = self.__cursor.fetchone()
        return result

    #执行SQL文件
    def exeSqlFile(self,filepath):
        sqlStr = ""
        for line in open(filepath, mode='r', encoding='UTF-8'):
            sqlStr = sqlStr + line
        self.__cursor.execute(sqlStr)
        self.__conn.commit()

    def closeConn(self):
        self.__conn.close()
        self.__conn = None
        self.__cursor = None

