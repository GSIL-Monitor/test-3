#encoding: utf-8

import os,pytest
from com.zhan.test.Utils import ParamUtil
from com.zhan.test.AssertHelper import AssertHelper

def value(method):
    return ParamUtil.getValue(os.path.basename(__file__),method)

#测试user_vocabulary_list
@pytest.mark.corpus
@pytest.mark.parametrize("processname,methodname,casedata,filename", value("user_vocabulary_list"))
def test_user_vocabulary_list(processname,methodname,casedata,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,filename)
