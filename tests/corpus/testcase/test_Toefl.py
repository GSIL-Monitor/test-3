#encoding: utf-8

import pytest,os
from com.zhan.test.Utils import ParamUtil
from com.zhan.test.AssertHelper import AssertHelper

def value(method):
    return ParamUtil.getValue(os.path.basename(__file__),method)

#测试filtrate_paper接口
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("filtrate_paper"))
def test_filtrate_paper(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试get_paper_list
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_paper_list"))
def test_get_paper_list(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试get_paper_detail
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_paper_detail"))
def test_get_paper_detail(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)


#测试get_article_list
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_article_list"))
def test_get_article_list(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)


#测试get_article_detail
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_article_detail"))
def test_get_article_detail(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)


#测试get_article_ques
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_article_ques"))
def test_get_article_ques(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)


#测试filtrate_ques
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("filtrate_ques"))
def test_filtrate_ques(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试get_ques_type_list
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_ques_type_list"))
def test_get_ques_type_list(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试get_ques
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_ques"))
def test_get_ques(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试error_ques_top
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("error_ques_top"))
def test_error_ques_top(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试get_ques_by_topicid
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_ques_by_topicid"))
def test_get_ques_by_topicid(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试biz_ques_classify
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("biz_ques_classify"))
def test_biz_ques_classify(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

# #测试get_biz_ques
# @pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_biz_ques"))
# def test_get_biz_ques(methodname, casename, casedata,filename):
#     AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试get_topic_avg_count
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_topic_avg_count"))
def test_get_topic_avg_count(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试get_label_list
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_label_list"))
def test_get_label_list(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试select_label
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("select_label"))
def test_select_label(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试article_label_summary
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("article_label_summary"))
def test_article_label_summary(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试gen_toefl_workflow_id
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("gen_toefl_workflow_id"))
def test_gen_toefl_workflow_id(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试update_toefl_workflow
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("update_toefl_workflow"))
def test_update_toefl_workflow(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试get_toefl_workflow_detail
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_toefl_workflow_detail"))
def test_get_toefl_workflow_detail(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试del_workflow
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("del_workflow"))
def test_del_workflow(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试save_article_practice
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("save_article_practice"))
def test_save_article_practice(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试save_paper_practice
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("save_paper_practice"))
def test_save_paper_practice(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试get_paper_practice
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_paper_practice"))
def test_get_paper_practice(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试get_practice_status
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_practice_status"))
def test_get_practice_status(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)


#测试breakpoint_practice
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("breakpoint_practice"))
def test_breakpoint_practice(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)


#测试article_breakpoint_practice
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("article_breakpoint_practice"))
def test_article_breakpoint_practice(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)


#测试last_article_practice_summary
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("last_article_practice_summary"))
def test_last_article_practice_summary(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)


#测试get_practice_result
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_practice_result"))
def test_get_practice_result(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试get_answer_by_workflow
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_answer_by_workflow"))
def test_get_answer_by_workflow(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试topic_practice_history
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("topic_practice_history"))
def test_topic_practice_history(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试get_answer_by_topic_id
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_answer_by_topic_id"))
def test_get_answer_by_topic_id(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)


#测试article_practice_count
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("article_practice_count"))
def test_article_practice_count(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试get_practice_list
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_practice_list"))
def test_get_practice_list(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)


#测试get_biz_practice_count
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("get_biz_practice_count"))
def test_get_biz_practice_count(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)

#测试save_biz_practice_count
@pytest.mark.parametrize("methodname,casename,casedata,filename", value("save_biz_practice_count"))
def test_save_biz_practice_count(methodname, casename, casedata,filename):
    AssertHelper.executeAndAssert(methodname, casename, casedata,filename)





