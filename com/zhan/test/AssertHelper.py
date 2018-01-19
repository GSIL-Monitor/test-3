#encoding: utf-8

from com.zhan.test.Utils import xmlUtil,JsonUtil,FuncUtil,AssertUtil
from com.zhan.test.publicData import publicData
from com.zhan.test.httpHelper import httpExecuter
from hamcrest import *
from com.zhan.test.isdict_containingkeys import has_keys
import DBHelper,threading
from lxml import etree

class AssertHelper:
    @staticmethod
    def executeAndAssert(processname,methodname, casedata,casename,filename):
        AssertHelper.__assertByMethod(methodname,casedata,processname,filename)

    @staticmethod
    def __assertByMethod(methodname, testCase, processname, filename):
        pd = publicData()
        testtype = testCase.get('type')
        #执行函数
        if testtype == 'func':
            method = testCase.get('method')    #执行的函数的方法
            param = testCase.text
            output = '%s_%s'%(testCase.get('output'),threading.currentThread().ident)
            result = getattr(FuncUtil, method)() if param == None else getattr(FuncUtil, method)(param)
            if output <> None:
                lock = threading.Lock
                lock.acquire()
                try:
                    pd.setOutput(output, result)
                finally:
                    lock.release()
        else:    #执行正常的接口调用
            # methodname = testMethod.get('method')
            subcasename = testCase.get('name')
            subcasedata = testCase
            response = httpExecuter.executeHttpRequest(methodname, subcasename, subcasedata)
            AssertHelper.__assertResponse(processname, methodname, subcasename, response, filename)

    @staticmethod
    def __assertResponse(processname,methodname,casename,response,filename):
        pd = publicData()
        path = r'%s\asset\%s.xml' % (pd.getMainDir(), filename)
        assertList = xmlUtil.getAssert(path,processname,methodname,casename)
        for assertEle in assertList:
            operator = assertEle.get('operator') if assertEle.get('operator') != None else "equal"   #默认的operator是equal

            type = assertEle.get('type')
            method = assertEle.get('method') if assertEle.get('method') != None else "equal"   #默认的method是equal
            param = assertEle.get('param')
            func1 = {'type':type,'method':method,'param':param}
            method1 = assertEle.get('method1')
            if method1 != None:
                type1 = assertEle.get('type1')
                param1 = assertEle.get('param1')
                func2 = {'type': type1, 'method': method1, 'param': param1}
                getattr(AssertMethed, 'comparetwomethod')(response, assertEle.text,operator,func1=func1,func2=func2)
            else:
                getattr(AssertMethed, method)(response, assertEle.text,operator,func1=func1)


class AssertMethed():
    #是否包含内容
    @staticmethod
    def contains(response,expected,operator,**kwargs):
        assert_that(response,contains_string(expected))

    #是否相等
    @staticmethod
    def equal(response,expected,operator,**kwargs):
        assert_that(response, is_(expected))

    #是否包含某些KEY值
    @staticmethod
    def haskeys(response,expected,operator,**kwargs):
        resObj = AssertUtil.haskeys(response,expected,operator,**kwargs)
        assert_that(resObj, has_keys(expected))

    #根据路径得到JSON中的某个KEY的值
    @staticmethod
    def getjsonvalue(response,expected,operator,**kwargs):
        param = kwargs['func1']['param']
        actual = AssertUtil.getjsonvalue(response,expected,operator,**kwargs)
        AssertMethed.__assetByOperator(actual,expected,operator)

    #根据路径得到JSON中某个ARRAY的数量
    @staticmethod
    def getjsonarraysize(response,expected,operator,**kwargs):
        param = kwargs['func1']['param']
        actual = AssertUtil.getjsonarraysize(response,expected,operator,**kwargs)
        AssertMethed.__assetByOperator(actual,expected,operator)

    #两个方法进行比较
    @staticmethod
    def comparetwomethod(response,expected,operator,**kwargs):
        func1 = kwargs['func1']
        func2 = kwargs['func2']

        if func1['type'] == 'func':
            res1 = getattr(FuncUtil,func1['method'])(func1['param'])
        else:
            res1 = getattr(AssertUtil, func1['method'])(response, expected, operator, func1=func1)
        if func2['type'] == 'func':
            res2 = getattr(FuncUtil,func2['method'])(func2['param'])
        else:
            res2 = getattr(AssertUtil, func2['method'])(response, expected, operator, func1=func2)

        AssertMethed.__assetByOperator(res1, res2, operator)


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
        path = r'%s\config\sql.xml' % (pd.getMainDir())
        html = etree.parse(path)
        sql = html.xpath('//sqllist/sql[@name=\'%s\']' % (sqlstr))[0].text
        # print sql
        return DBHelper.DatabaseConn.getValueBySql(sql)[0]


