#encoding: utf-8

import pytest,os,warnings,sys,threading
from com.zhan.test.Utils import ParamUtil,FuncUtil
from com.zhan.test.AssertHelper import AssertHelper

warnings.filterwarnings('ignore')
reload(sys)
sys.setdefaultencoding('utf8')


def value(method):
    return ParamUtil.getValue(os.path.basename(__file__),method,'operation')
#
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getpublic"))
# def test_getpublic(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeFunc(processname,methodname,casedata,casename,filename)

#测试signuppublicclass接口
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("signuppublicclass"))
def test_signuppublicclass(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试signupactivity接口
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("signupactivity"))
def test_signupactivity(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getuserpublicclasslist
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getuserpublicclasslist"))
def test_getuserpublicclasslist(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getuseractivitylist
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getuseractivitylist"))
def test_getuseractivitylist(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

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


#测试getteacherdetail接口
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getteacherdetail"))
def test_getteacherdetail(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试saveuserriseform接口
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("saveuserriseform"))
def test_saveuserriseform(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getuserriseform
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getuserriseform"))
def test_getuserriseform(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getactivityrecommendlistbyteacher
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getactivityrecommendlistbyteacher"))
def test_getactivityrecommendlistbyteacher(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getactivitylistbyactivitycategory接口
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getactivitylistbyactivitycategory"))
def test_getactivitylistbyactivitycategory(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getfamousteachercolumninfo接口
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getfamousteachercolumninfo"))
def test_getfamousteachercolumninfo(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getpublicclassliveroominfo
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getpublicclassliveroominfo"))
def test_getpublicclassliveroominfo(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试teachervaluation
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("teachervaluation"))
def test_teachervaluation(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getteachervaluation接口
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getteachervaluation"))
def test_getteachervaluation(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getteacherlistbytype
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getteacherlistbytype"))
def test_getteacherlistbytype(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getfamousteacherbaselist
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getfamousteacherbaselist"))
def test_getfamousteacherbaselist(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getfamousteacherdetaillist接口
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getfamousteacherdetaillist"))
def test_getfamousteacherdetaillist(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getpublicclasslist
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getpublicclasslist"))
def test_getpublicclasslist(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试studentreceivediscount
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("studentreceivediscount"))
def test_studentreceivediscount(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getuserinfo
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getuserinfo"))
def test_getuserinfo(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getuserinfo
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getadrecommendclassoractivity"))
def test_getadrecommendclassoractivity(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getsignclockrecordbygroup
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getsignclockrecordbygroup"))
def test_getsignclockrecordbygroup(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试usersignclock
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("usersignclock"))
def test_usersignclock(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getusergroupinfo
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getusergroupinfo"))
def test_getusergroupinfo(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#getusersignclockrecord
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getusersignclockrecord"))
def test_getusersignclockrecord(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#getpublicclassvideourl
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getpublicclassvideourl"))
def test_getpublicclassvideourl(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#userbindinggroup
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("userbindinggroup"))
def test_userbindinggroup(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#getassistent
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getassistent"))
def test_getassistent(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#getassistentpublic
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getassistentpublic"))
def test_getassistentpublic(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getgroupinfobygroupid
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getgroupinfobygroupid"))
def test_getgroupinfobygroupid(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


#getmyrecord
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getmyrecord"))
def test_getmyrecord(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#postworkstatistics
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("postworkstatistics"))
def test_postworkstatistics(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getpublicclassactivityrecord
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getpublicclassactivityrecord"))
def test_getpublicclassactivityrecord(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#getactivitypromotion
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getactivitypromotion"))
def test_getactivitypromotion(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getusersrank
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getusersrank"))
def test_getusersrank(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#getactivitypromotionwrited
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getactivitypromotionwrited"))
def test_getactivitypromotionwrited(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

#测试getactivitygroupinfo
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getactivitygroupinfo"))
def test_getactivitygroupinfo(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


#测试gethomeworktodaylist
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("gethomeworktodaylist"))
def test_gethomeworktodaylist(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


#测试syncavtivitysignuppromotion的JOB
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("syncavtivitysignuppromotion"))
def test_syncavtivitysignuppromotion(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


#测试activitylottery
@pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("activitylottery"))
def test_activitylottery(processname,methodname,casedata,casename,filename):
    AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)

# #测试getactivitycourseextendlist
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getactivitycourseextendlist"))
# def test_getactivitycourseextendlist(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
# #测试getactivitymoments
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getactivitymoments"))
# def test_getactivitymoments(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
# #测试getactivityawards
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getactivityawards"))
# def test_getactivityawards(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
# #测试userattendrecord
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("userattendrecord"))
# def test_userattendrecord(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
# #测试getuserbaseinfo
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getuserbaseinfo"))
# def test_getuserbaseinfo(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
# #测试boostactivity
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("boostactivity"))
# def test_boostactivity(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
# #getboosterlist
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getboosterlist"))
# def test_getboosterlist(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
# #savepublicclassuseraddress
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("savepublicclassuseraddress"))
# def test_savepublicclassuseraddress(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
# #getpublicclassuseraddress
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getpublicclassuseraddress"))
# def test_getpublicclassuseraddress(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
# #getawardrecord
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getawardrecord"))
# def test_getawardrecord(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
# #changeaward
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("changeaward"))
# def test_changeaward(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)
#
#
# #测试getexamdate
# @pytest.mark.parametrize("processname,methodname,casedata,casename,filename", value("getexamdate"))
# def test_getexamdate(processname,methodname,casedata,casename,filename):
#     AssertHelper.executeAndAssert(processname,methodname,casedata,casename,filename)


