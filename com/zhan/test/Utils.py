# encoding: utf-8

from lxml import etree
import json, threading,datetime,random
from com.zhan.test.publicData import publicData
import com.zhan.test.AppDBHelper as dh

class xmlUtil:
    # 单接口
    @staticmethod
    def getDataByMethod(path, method):
        html = etree.parse(path)
        result = html.xpath(r"//TestSuite/TestMethod[@name='%s']/TestCase" % (method))
        return result

    @staticmethod
    def getDataByMethodCase(path, method, casename):
        html = etree.parse(path)
        result = html.xpath(r"//TestSuite/TestMethod[@name='%s']/TestCase[@name='%s']" % (method, casename))
        return result

    @staticmethod
    def getDebugCaseName(path, methodname, filename):
        pd = publicData.instance()
        html = etree.parse(path)
        methodList = html.xpath(r"//suite[@name='%s']/files/file[@name='test_%s']/Method" % (pd.getSuiteName(), filename))
        for method in methodList:
            if method.text.endswith(methodname):
                return method.text
        return None

    # 查询流程接口
    @staticmethod
    def getProcessDataByMethod(path, method):
        html = etree.parse(path)
        result = html.xpath(r"//TestSuite/TestProcess[@name='%s']" % (method))
        return result

    @staticmethod
    def getConfigEleByMethod(path, method):
        html = etree.parse(path)
        configEle = html.xpath(r"//Config/api[@name='%s']" % (method))[0]
        return configEle

    # 获取验证执行列表
    @staticmethod
    def getAssert(path, processname, methodname, casename):
        html = etree.parse(path)
        assertList = None
        # assertList = html.xpath('//TestSuite/TestMethod[@name=\'%s\']/TestCase[@name=\'%s\']' % (methodname,casename))
        if processname == methodname:
            assertList = html.xpath(
                r"//TestSuite/TestMethod[@name='%s']/TestCase[@name='%s']/Assert" % (methodname, casename))
        else:
            assertList = html.xpath(
                r"//TestSuite/TestProcess[@name='%s']/TestMethod[@name='%s']/TestCase[@name='%s']/Assert" % (
                processname, methodname, casename))
        if len(assertList) == 0:
            raise NameError("Assert config error.Process:%s,Method:%s,Casename:%s" % (processname, methodname, casename))

        return assertList


class JsonUtil:
    # 通过参数从RESPONSE中解析对象
    @staticmethod
    def __getJsonObjByParam(response, param):
        try:
            jsonObj = json.loads(response)
            for par in param.split("."):
                if par[0] == "[":
                    jsonObj = jsonObj[int(par[1:-1])]
                else:
                    jsonObj = jsonObj[par]
            return jsonObj
        except:
            raise NameError("验证参数配置错误,参数为：%s" % param)

    @staticmethod
    def getJsonObjByPar(response, param):
        obj = JsonUtil.__getJsonObjByParam(response, param)
        return obj

    @staticmethod
    def getJsonStrByPar(response, param):
        obj = str(JsonUtil.__getJsonObjByParam(response, param))
        return obj

    @staticmethod
    def getJsonArraySize(response, param):
        obj = JsonUtil.__getJsonObjByParam(response, param)
        if type(obj) == list:
            return len(obj)
        else:
            return 1


class ParamUtil:
    @staticmethod
    def getValue(file, method,project):
        pa = []
        casename = None
        pd = publicData.instance()
        if pd.getMainDir() == "" : pd = FuncUtil.initPublicData(project) #只初始化一次
        filename = file[5:-3]
        path = '%s\data\%s.xml' % (pd.getMainDir(), filename)

        # DEBUG模式，有可能会指定TESTCASE
        if pd.getRunMode().lower() == "debug":
            casename = xmlUtil.getDebugCaseName('%s\config\debug.xml' % (pd.getMainDir()), method, filename)

        # 指定的TESTCASE
        if casename != None:
            result = xmlUtil.getDataByMethodCase(path, method, casename)
        else:#全部的testcase
            result = xmlUtil.getDataByMethod(path, method)

        # 非单接口形式，而是接口流程
        if len(result) == 0:
            result = xmlUtil.getProcessDataByMethod(path, method)
            if len(result) > 0:
                for testmethod in result[0].getchildren():
                    for testcase in testmethod.getchildren():
                        pa.append([method, testmethod.get('name'), testcase,testcase.get('name') ,filename])
        else:
            for i in range(len(result)):
                pa.append([method, method, result[i], result[i].get('name'),filename])

        if pa == []:
            raise Exception("文件%s中的方法%s未配置数据"%(file,method))
        else:
            return pa


class FuncUtil:
    @staticmethod
    def getpublicbyname(publicname):
        db = dh.DBConn.instance()
        if publicname == 'publicid':
            res = db.getValueBySql(r"select [PublicID] from [dbo].[Tpo_PublicClass] where [PublicTitle] = 'ToeflTest'")
            return res[0]
        elif publicname == 'activityid':
            res = db.getValueBySql(r"select [ActivityID] from [dbo].[Tpo_PublicClass_Activities] where [ActivityTitle] = 'ToeflTest'")
            return res[0]

    @staticmethod
    def getoutput(key):
        pd = publicData.instance()
        lock = threading.Lock()
        lock.acquire()
        try:
            return pd.getOutput('%s_%s'%(key,threading.currentThread().ident))
        finally:
            lock.release()

    @staticmethod
    def getdatetime(inteval=0):
        if inteval == None:inteval = 0
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=int(inteval))
        n_days = now + delta
        return r'%s 00:00:00'%(n_days.strftime('%Y-%m-%d'))

    @staticmethod
    def getdate(inteval=0):
        if inteval == None:inteval = 0
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=int(inteval))
        n_days = now + delta
        return n_days.strftime('%Y-%m-%d')

    @staticmethod
    def randomstr(length=8):
        if length == None:length = 8
        return random.randint(10000000, 99999999)


    @staticmethod
    def initPublicData(projectname):
        pd = publicData.instance()
        mainhtml = etree.parse('main.xml')
        runmode = mainhtml.xpath('//run/mode')[0].text
        proconfig = etree.parse(r'tests\%s\config\%s.xml' % (projectname, runmode))
        suitename = proconfig.xpath('//suite')[0].get('name')
        pd.setProjectConfig(projectname, suitename)
        pd.setRunMode(runmode)
        return pd


class AssertUtil:
    # 是否包含某些KEY值
    @staticmethod
    def haskeys(response, expected, operator, **kwargs):
        param = kwargs['func1']['param']
        resObj = JsonUtil.getJsonObjByPar(response, param)
        return resObj

    # 根据路径得到JSON中的某个KEY的值
    @staticmethod
    def getjsonvalue(response, expected, operator, **kwargs):
        param = kwargs['func1']['param']
        actual = JsonUtil.getJsonStrByPar(response, param)
        return actual

    # 根据路径得到JSON中某个ARRAY的数量
    @staticmethod
    def getjsonarraysize(response, expected, operator, **kwargs):
        param = kwargs['func1']['param']
        actual = JsonUtil.getJsonArraySize(response, param)
        return actual



