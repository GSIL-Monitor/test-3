#encoding: utf-8

import pytest,os,warnings,sys,threading
from com.zhan.test.Utils import ParamUtil
from com.zhan.test.AssertHelper import AssertHelper
import allure

warnings.filterwarnings('ignore')

# def value(method):
#     return ParamUtil.getValue(os.path.basename(__file__),method,'operation')
#
# # #测试getlatestactivity接口
# # @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("publicclasscheck"))
# # def test_publicclasscheck(processname,methodname,  casedata,casename,filename):
# #     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
# #测试getlatestactivity接口
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getlatestactivity"))
# def test_getlatestactivity(processname,methodname, casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


def value(method):
    return ['111','222','333']



@pytest.mark.parametrize("test", value("test1"))
def test_test1(test):
    print('test1'+ test + "\n")

# def test_test2():
#     print('test2'+"\n")
#
# def test_test3():
#     print('test3'+"\n")
#
