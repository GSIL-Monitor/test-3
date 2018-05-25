# #encoding: utf-8
from com.zhan.test.publicData import publicData
from lxml import etree
import pymssql,pymysql

# 单例
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class DBConn(Singleton):
    __conn = None
    __cursor = None

    def __init__(self):
        if self.__cursor == None and self.__cursor == None:
            pd = publicData()
            html = etree.parse(r"%s\config\config.xml" % (pd.getMainDir()))
            result = html.xpath('//config/apidatabase')
            if len(result) == 0:
                raise NameError("framework database not config")

            host = result[0].find('host').text
            port = int(result[0].find('port').text) if result[0].find('port').text != None else None
            username = result[0].find('username').text
            password = result[0].find('password').text
            db = result[0].find('db').text

            if result[0].get('name') == 'mysql':
                self.__conn = pymysql.connect(host=host, port=port, user=username, password=password, database=db, charset="utf8",
                                            cursorclass=pymysql.cursors.DictCursor)
            self.__cursor = self.__conn.cursor()


    def closeConn(self):
        self.__conn.close()
        self.__conn = None
        self.__cursor = None

    def insertDetailReport(self,detail):
        pass

    def insertMainReport(self,main):
        pass
