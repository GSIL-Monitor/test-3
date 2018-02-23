#encoding: utf-8

import os,pytest
from com.zhan.test.Utils import ParamUtil
from com.zhan.test.AssertHelper import AssertHelper


def value(method):
    return ParamUtil.getValue(os.path.basename(__file__),method,'corpus')


#测试wrong_list
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("wrong_list"))
def test_wrong_list(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试del_wrong_list
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("del_wrong_list"))
def test_del_wrong_list(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试multi_ques_practice_list_vip
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("multi_ques_practice_list_vip"))
def test_multi_ques_practice_list_vip(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试topic_practice_history
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("practice_history"))
def test_practice_history(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试list
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("list"))
def test_list(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


# #测试toefl_article_practice_list
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("toefl_article_practice_list"))
# def test_toefl_article_practice_list(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


# 测试add
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("add"))
def test_add(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

# 测试favlist
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("favlist"))
def test_favlist(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

# 测试status
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("status"))
def test_status(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

# 测试del
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("del"))
def test_del(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

# # 测试update_practice_status_vip
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("update_practice_status_vip"))
# def test_update_practice_status_vip(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
# # 测试update_practice_status
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("update_practice_status"))
# def test_update_practice_status(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
# # 测试login
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("login"))
# def test_login(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
