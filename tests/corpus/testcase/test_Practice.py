#encoding: utf-8

import os,pytest
from com.zhan.test.Utils import ParamUtil
from com.zhan.test.AssertHelper import AssertHelper

def value(method):
    return ParamUtil.getValue(os.path.basename(__file__),method)

#测试wrong_list
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("wrong_list"))
def test_wrong_list(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)
