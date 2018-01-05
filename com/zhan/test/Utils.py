#encoding: utf-8

from lxml import etree
import json
from com.zhan.test.publicData import publicData

class xmlUtil:
    #单接口
    @staticmethod
    def getDataByMethod(path, method):
        html = etree.parse(path)
        result = html.xpath('//TestSuite/TestMethod[@name=\'%s\']/TestCase' % (method))
        return result

    @staticmethod
    def getDataByMethodCase(path, method,casename):
        html = etree.parse(path)
        result = html.xpath('//TestSuite/TestMethod[@name=\'%s\']/TestCase[@name=\'%s\']' % (method,casename))
        return result

    @staticmethod
    def getDebugCaseName(path, methodname,filename):
        pd = publicData()
        html = etree.parse(path)
        methodList = html.xpath('//suite[@name=\'%s\']/files/file[@name=\'%s\']/Method' % (pd.getSuiteName(),filename))
        for method in methodList:
            if method.text.endswith(methodname):
                return method.get('name')
        return None


    #查询流程接口
    @staticmethod
    def getProcessDataByMethod(path, method):
        html = etree.parse(path)
        result = html.xpath('//TestSuite/TestProcess[@name=\'%s\']' % (method))
        return result

    @staticmethod
    def getConfigEleByMethod(path, method):
        html = etree.parse(path)
        configEle = html.xpath('//Config/api[@name=\'%s\']' % (method))[0]
        return configEle

    #获取验证执行列表
    @staticmethod
    def getAssert(path,processname,methodname,casename):
        html = etree.parse(path)
        assertList = None
        # assertList = html.xpath('//TestSuite/TestMethod[@name=\'%s\']/TestCase[@name=\'%s\']' % (methodname,casename))
        if processname == None:
            assertList = html.xpath('//TestSuite/TestMethod[@name=\'%s\']/TestCase[@name=\'%s\']/Assert' % (methodname,casename))
        else:
            assertList = html.xpath('//TestSuite/TestProcess[@name=\'%s\']/TestMethod[@name=\'%s\']/TestCase[@name=\'%s\']/Assert' % (processname,methodname, casename))

        if len(assertList) == 0:
            raise NameError, ("Assert config error.Process:%s,Method:%s,Casename:%s" % (processname,methodname, casename))

        return assertList


class JsonUtil:
    #通过参数从RESPONSE中解析对象
    @staticmethod
    def __getJsonObjByParam(response,param):
        try:
            jsonObj = json.loads(response)
            for par in param.split("."):
                if par[0] == "[":
                    jsonObj = jsonObj[int(par[1:-1])]
                else:
                    jsonObj = jsonObj[par]
            return jsonObj
        except:
            raise NameError, ("验证参数配置错误,参数为：%s"%param)


    @staticmethod
    def getJsonObjByPar(response,param):
        obj = JsonUtil.__getJsonObjByParam(response,param)
        return obj

    @staticmethod
    def getJsonStrByPar(response,param):
        obj = str(JsonUtil.__getJsonObjByParam(response,param))
        return obj

    @staticmethod
    def getJsonArraySize(response,param):
        obj = JsonUtil.__getJsonObjByParam(response,param)
        if type(obj) == list:
            return len(obj)
        else:
            return 1


class ParamUtil:
    @staticmethod
    def getValue(file,method):
        pa = []
        casename = None
        pd = publicData()
        path = '%s/data/%s.xml' % (pd.getMainDir(), file[5:-3])

        #DEBUG模式，有可能会指定TESTCASE
        if pd.getRunMode().lower() == "debug":
            casename = xmlUtil.getDebugCaseName('%s/config/debug.xml' % (pd.getMainDir()), method,file[5:-3])

        if casename <> None:
            result = xmlUtil.getDataByMethodCase(path, method, casename)
        else:
            result = xmlUtil.getDataByMethod(path, method)

        #非单接口形式，而是接口流程
        if len(result) == 0:
            result = xmlUtil.getProcessDataByMethod(path,method)
        for i in xrange(len(result)):
            pa.append([method, result[i].get('name'), result[i],file[5:-3]])
        return pa



class FuncUtil:
    @staticmethod
    def getoutput(key):
        pd = publicData()
        return pd.getOutput(key)

    @staticmethod
    def getpassportid(ss):
        return ss