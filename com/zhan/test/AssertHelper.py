#encoding: utf-8

from com.zhan.test.Utils import xmlUtil,JsonUtil,FuncUtil,AssertUtil
from com.zhan.test.publicData import publicData
from com.zhan.test.httpHelper import httpExecuter
from hamcrest import *
from com.zhan.test.isdict_containingkeys import has_keys
import AppDBHelper,threading,sys
import com.zhan.test.AppDBHelper as dh
from lxml import etree
import os,time

reload(sys)
sys.setdefaultencoding('utf-8')

class AssertHelper:
    @staticmethod
    def executeAndAssert(processname,methodname, casedata,casename,filename):
        pd = publicData()
        #初始化
        initSqlFile = r'%s\sql\%s_%s_init.sql' % (pd.getMainDir(),methodname,casename)
        if os.path.exists(initSqlFile):
            dbConn = dh.DBConn()
            dbConn.exeSqlFile(initSqlFile)
        try:
            response = AssertHelper.__assertByMethod(methodname,casedata,processname,filename)
            AssertHelper.__assertResponse(processname, methodname, casedata.get('name'), response, filename)
        finally:
            # 清理
            finSqlFile = r'%s\sql\%s_%s_fin.sql' % (pd.getMainDir(),methodname,casename)
            if os.path.exists(finSqlFile):
                dbConn = dh.DBConn()
                dbConn.exeSqlFile(finSqlFile)

    @staticmethod
    def executeFunc(processname,methodname, casedata,casename,filename):
        AssertHelper.__executeFunc(methodname, casedata, processname, filename)

    @staticmethod
    def __executeFunc(methodname, testCase, processname, filename):
        pd = publicData()
        method = testCase.get('method')  # 执行的函数的方法
        param = testCase.get('param')
        output = '%s_%s' % (testCase.get('output'), threading.currentThread().ident)
        result = getattr(FuncUtil, method)() if param == None else getattr(FuncUtil, method)(param)
        if output <> None:
            lock = threading.Lock()
            lock.acquire()
            try:
                pd.setOutput(output, result)
            finally:
                lock.release()

    @staticmethod
    def __assertByMethod(methodname, testCase, processname, filename):
        # testtype = testCase.get('type')
        # #执行函数
        # if testtype == 'func':
        #     AssertHelper.__executeFunc(methodname, testCase, processname, filename)
        # else:    #执行正常的接口调用
        #     # methodname = testMethod.get('method')
        subcasename = testCase.get('name')
        subcasedata = testCase
        response = httpExecuter.executeHttpRequest(methodname, subcasename, subcasedata)
        return response


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
            val = assertEle.get('value')
            func1 = {'type':type,'method':method,'param':param,'value':val}        #第一个函数
            method1 = assertEle.get('method1')
            if method1 != None:
                type1 = assertEle.get('type1')
                param1 = assertEle.get('param1')
                val1 = assertEle.get('value1')
                func2 = {'type': type1, 'method': method1, 'param': param1,'value':val1}        #第二个函数
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
        # param = kwargs['func1']['param']
        actual = AssertUtil.getjsonvalue(response,expected,operator,**kwargs)
        AssertMethed.__assetByOperator(actual,expected,operator)

    #根据路径得到JSON中某个ARRAY的数量
    @staticmethod
    def getjsonarraysize(response,expected,operator,**kwargs):
        # param = kwargs['func1']['param']
        actual = AssertUtil.getjsonarraysize(response,expected,operator,**kwargs)
        AssertMethed.__assetByOperator(actual,expected,operator)

    # 得到SQL内容
    @staticmethod
    def getvaluebysql(response, expected, operator, **kwargs):
        func1 = kwargs['func1']
        actual = AssertMethed.__getvaluebysql(func1['param'],func1['value'])
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
        #通用的处理
        if type(actual) == str:
            actual = actual.decode('utf-8')
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

        #通用类型的处理
        if operator == "none":
            assert_that(actual, none())
        elif operator == "notnone":
            assert_that(actual, not_none())

    @staticmethod
    def __getvaluebysql(sqlname,param):
        pd = publicData()
        path = r'%s\config\sql.xml' % (pd.getMainDir())
        html = etree.parse(path)
        sql = html.xpath(r"//sqllist/sql[@name='%s']" % (sqlname))[0].text
        if param != None:
            res = param.split(',')
            for index in xrange(0, len(res)):
                sql = str.replace(sql, '%param%', res[index], 1)
        # print sql
        dbConn = dh.DBConn()
        return dbConn.getValueBySql(sql)[0]
