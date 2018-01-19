#encoding: utf-8

import pytest,os,warnings,sys,threading
from com.zhan.test.Utils import ParamUtil,FuncUtil
from com.zhan.test.AssertHelper import AssertHelper

warnings.filterwarnings('ignore')
reload(sys)
sys.setdefaultencoding('utf8')


def value(method):
    return ParamUtil.getValue(os.path.basename(__file__),method,'operation')

#测试getlatestactivity接口
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getlatestactivity"))
def test_getlatestactivity(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getactivitydetails接口
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getactivitydetails"))
def test_getactivitydetails(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getactivitylist
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getactivitylist"))
def test_getactivitylist(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getsignupuserwechatinfo
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getsignupuserwechatinfo"))
def test_getsignupuserwechatinfo(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

# #测试GetUserPublicClassList
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("GetUserPublicClassList"))
# def test_GetUserPublicClassList(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
