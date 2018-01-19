#encoding: utf-8

import pytest,os,warnings,sys,threading
from com.zhan.test.Utils import ParamUtil
from com.zhan.test.AssertHelper import AssertHelper

warnings.filterwarnings('ignore')
reload(sys)
sys.setdefaultencoding('utf8')

def value(method):
    return ParamUtil.getValue(os.path.basename(__file__),method,'operation')

#测试getlatestactivity接口
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("publicclasscheck"))
def test_publicclasscheck(processname,methodname,  casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getlatestactivity接口
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getlatestactivity"))
def test_getlatestactivity(processname,methodname, casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)



