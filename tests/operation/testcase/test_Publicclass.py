#encoding: utf-8

import pytest,os
from com.zhan.test.Utils import ParamUtil
from com.zhan.test.AssertHelper import AssertHelper

def value(method):
    return ParamUtil.getValue(os.path.basename(__file__),method)

#测试getlatestactivity接口
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("getlatestactivity"))
def test_getlatestactivity(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试getactivitydetails接口
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("getactivitydetails"))
def test_getactivitydetails(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试getactivitylist
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("getactivitylist"))
def test_getactivitylist(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试getsignupuserwechatinfo
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("getsignupuserwechatinfo"))
def test_getsignupuserwechatinfo(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试GetUserPublicClassList
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("GetUserPublicClassList"))
def test_GetUserPublicClassList(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

