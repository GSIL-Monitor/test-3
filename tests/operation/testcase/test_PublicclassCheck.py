#encoding: utf-8

import pytest,os
from com.zhan.test.Utils import ParamUtil
from com.zhan.test.AssertHelper import AssertHelper

def value(method):
    return ParamUtil.getValue(os.path.basename(__file__),method)

#测试getlatestactivity接口
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("publicclasscheck"))
def test_publicclasscheck(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试getlatestactivity接口
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("getlatestactivity"))
def test_getlatestactivity(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)