#encoding: utf-8

import pytest,os
from com.zhan.test.Utils import ParamUtil
from com.zhan.test.AssertHelper import AssertHelper


def value(method):
    return ParamUtil.getValue(os.path.basename(__file__),method,'corpus')

#测试filtrate_paper接口
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("filtrate_paper"))
def test_filtrate_paper(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试get_paper_list
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_paper_list"))
def test_get_paper_list(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试get_paper_detail
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_paper_detail"))
def test_get_paper_detail(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


#测试get_article_list
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_article_list"))
def test_get_article_list(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


#测试get_article_detail
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_article_detail"))
def test_get_article_detail(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


#测试get_article_ques
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_article_ques"))
def test_get_article_ques(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


#测试filtrate_ques
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("filtrate_ques"))
def test_filtrate_ques(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试get_ques_type_list
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_ques_type_list"))
def test_get_ques_type_list(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试get_ques
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_ques"))
def test_get_ques(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试error_ques_top
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("error_ques_top"))
def test_error_ques_top(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试get_ques_by_topicid
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_ques_by_topicid"))
def test_get_ques_by_topicid(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试biz_ques_classify
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("biz_ques_classify"))
def test_biz_ques_classify(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

# #测试get_biz_ques
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_biz_ques"))
# def test_get_biz_ques(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试get_topic_avg_count
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_topic_avg_count"))
def test_get_topic_avg_count(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试get_label_list
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_label_list"))
def test_get_label_list(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试select_label
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("select_label"))
def test_select_label(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试article_label_summary
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("article_label_summary"))
def test_article_label_summary(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试gen_toefl_workflow_id
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("gen_toefl_workflow_id"))
def test_gen_toefl_workflow_id(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试update_toefl_workflow
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("update_toefl_workflow"))
def test_update_toefl_workflow(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试get_toefl_workflow_detail
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_toefl_workflow_detail"))
def test_get_toefl_workflow_detail(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试del_workflow
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("del_workflow"))
def test_del_workflow(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试save_article_practice
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("save_article_practice"))
def test_save_article_practice(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试save_paper_practice
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("save_paper_practice"))
def test_save_paper_practice(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试get_paper_practice
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_paper_practice"))
def test_get_paper_practice(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试get_practice_status
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_practice_status"))
def test_get_practice_status(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


#测试breakpoint_practice
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("breakpoint_practice"))
def test_breakpoint_practice(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


#测试article_breakpoint_practice
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("article_breakpoint_practice"))
def test_article_breakpoint_practice(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


#测试last_article_practice_summary
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("last_article_practice_summary"))
def test_last_article_practice_summary(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


#测试get_practice_result
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_practice_result"))
def test_get_practice_result(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试get_answer_by_workflow
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_answer_by_workflow"))
def test_get_answer_by_workflow(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试topic_practice_history
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("topic_practice_history"))
def test_topic_practice_history(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试get_answer_by_topic_id
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_answer_by_topic_id"))
def test_get_answer_by_topic_id(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


#测试article_practice_count
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("article_practice_count"))
def test_article_practice_count(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试get_practice_list
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_practice_list"))
def test_get_practice_list(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


#测试get_biz_practice_count
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("get_biz_practice_count"))
def test_get_biz_practice_count(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试save_biz_practice_count
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("save_biz_practice_count"))
def test_save_biz_practice_count(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

