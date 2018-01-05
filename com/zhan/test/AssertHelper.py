#encoding: utf-8

from com.zhan.test.Utils import xmlUtil,JsonUtil,FuncUtil
from com.zhan.test.publicData import publicData
from com.zhan.test.httpHelper import httpExecuter
from hamcrest import *
from com.zhan.test.isdict_containingkeys import has_keys
import DBHelper
from lxml import etree

class AssertHelper:
    @staticmethod
    def executeAndAssert(methodname, casename, casedata,filename):
        if casedata.tag == 'TestProcess':
            for testMethod in casedata:
                AssertHelper.__assertByMethod(casedata.get('name'),testMethod, methodname, filename)
        else:
            testMethod = casedata
            AssertHelper.__assertByMethod(None,testMethod,methodname,filename)

    @staticmethod
    def __assertByMethod(processname,testMethod,methodname,filename):
        pd = publicData()
        testtype = testMethod.get('type')
        if testtype == 'func':
            method = testMethod.get('method')
            param = testMethod.text
            output = testMethod.get('output')
            result = getattr(FuncUtil, method)() if param == None else getattr(FuncUtil, method)(param)
            if output <> None:
                pd.setOutput(output, result)
        else:
            # methodname = testMethod.get('method')
            subcasename = testMethod.get('name')
            subcasedata = testMethod
            response = httpExecuter.executeHttpRequest(methodname, subcasename, subcasedata)
            AssertHelper.__assertResponse(processname, methodname, subcasename, response, filename)

    @staticmethod
    def __assertResponse(processname,methodname,casename,response,filename):
        pd = publicData()
        path = '%s/asset/%s.xml' % (pd.getMainDir(), filename)
        assertList = xmlUtil.getAssert(path,processname,methodname,casename)
        for assertEle in assertList:
            method = assertEle.get('method') if assertEle.get('method') <> None else "equal"         #默认的方法是equal
            param = assertEle.get('param')
            operator = assertEle.get('operator') if assertEle.get('operator') <> None else "equal"   #默认的operator是equal
            method1 = assertEle.get('method1')
            param1 = assertEle.get('param1')
            if param == None:
                getattr(AssertMethed, method)(response,assertEle.text)
            elif method1 == None:
                getattr(AssertMethed, method)(response, assertEle.text, param, operator)
            else:
                getattr(AssertMethed, method)(response, assertEle.text, param, operator,method1,param1)


class AssertMethed():
    #是否包含内容
    @staticmethod
    def contains(response,expected):
        assert_that(response,contains_string(expected))

    #是否相等
    @staticmethod
    def equal(response,expected):
        assert_that(response, is_(expected))

    #是否包含某些KEY值
    @staticmethod
    def haskeys(response,expected,param,operator):
        resObj = JsonUtil.getJsonObjByPar(response,param)
        assert_that(resObj, has_keys(expected))

    #根据路径得到JSON中的某个KEY的值
    @staticmethod
    def getjsonvalue(response,expected,param,operator):
        actual = JsonUtil.getJsonStrByPar(response, param)
        AssertMethed.assetByOperator(actual,expected,operator)

    #根据路径得到JSON中某个ARRAY的数量
    @staticmethod
    def getjsonarraysize(response,expected,param,operator):
        actual = JsonUtil.getJsonArraySize(response, param)
        AssertMethed.assetByOperator(actual,expected,operator)


    @staticmethod
    def getjsonarraysizeandcompare(response,expected,param,operator,method1,param1):
        result = getattr(AssertMethed,method1)(param1)
        print result
        actual = JsonUtil.getJsonArraySize(response, param)
        exp = int(result)
        AssertMethed.__assetByOperator(actual,exp,operator)

    #有操作符的验证
    @staticmethod
    def __assetByOperator(actual,expected,operator):
        if type(actual) == str:
            if operator == "equal":
                assert_that(actual,is_(expected))
            elif operator == "greater":
                assert_that(actual,greater_than(expected))
            elif operator == "less":
                assert_that(actual,less_than(expected))
            elif operator == "notequal":
                assert_that(actual,is_not(expected))
        elif type(actual) == int:
            if operator == "equal":
                assert_that(actual,is_(int(expected)))
            elif operator == "greater":
                assert_that(actual,greater_than(int(expected)))
            elif operator == "less":
                assert_that(actual,less_than(int(expected)))
            elif operator == "notequal":
                assert_that(actual,is_not(int(expected)))


    @staticmethod
    def getvaluebysql(sqlstr):
        pd = publicData()
        path = '%s/config/sql.xml' % (pd.getMainDir())
        html = etree.parse(path)
        sql = html.xpath('//sqllist/sql[@name=\'%s\']' % (sqlstr))[0].text
        # print sql
        return DBHelper.DatabaseConn.getValueBySql(sql)[0]


