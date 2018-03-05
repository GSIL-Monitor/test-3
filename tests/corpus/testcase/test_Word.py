#encoding: utf-8

import os,pytest
from com.zhan.test.Utils import ParamUtil
from com.zhan.test.AssertHelper import AssertHelper

def value(method):
    return ParamUtil.getValue(os.path.basename(__file__),method,'corpus')

#测试user_vocabulary_list接口
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("user_vocabulary_list"))
def test_user_vocabulary_list(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)