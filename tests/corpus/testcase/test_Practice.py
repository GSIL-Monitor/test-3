#encoding: utf-8

import os,pytest
from com.zhan.test.Utils import ParamUtil
from com.zhan.test.AssertHelper import AssertHelper

def value(method):
    return ParamUtil.getValue(os.path.basename(__file__),method)

#测试wrong_list
@pytest.mark.parametrize("processname,methodname,  casedata,filename", value("wrong_list"))
def test_wrong_list(processname,methodname,  casedata,filename):
    AssertHelper.executeAndAssert(processname,methodname,  casedata,filename)
