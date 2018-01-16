#encoding: utf-8

import pytest,os
from com.zhan.test.Utils import ParamUtil
from com.zhan.test.AssertHelper import AssertHelper

def value(method):
    return ParamUtil.getValue(os.path.basename(__file__),method)

#测试getlatestactivity接口
@pytest.mark.parametrize("processname,methodname,casedata,filename", value("publicclasscheck"))
def test_publicclasscheck(processname,methodname,  casedata,filename):
    AssertHelper.executeAndAssert(processname,methodname,  casedata,filename)

#测试getlatestactivity接口
@pytest.mark.parametrize("processname,methodname,casedata,filename", value("getlatestactivity"))
def test_getlatestactivity(processname,methodname, casedata,filename):
    AssertHelper.executeAndAssert(processname,methodname,  casedata,filename)