#encoding: utf-8

import warnings,sys,os
import com.zhan.test.MailHelper as mh
import pytest
from lxml import etree
from com.zhan.test.publicData import publicData
from com.zhan.test.DBHelper import DatabaseConn
import shutil

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('C:\\Users\\Administrator\\PycharmProjects\\test\\')
#忽略 HTTPS中不验证证书的WARNING
warnings.filterwarnings('ignore')

#从配置文件中得到待运行项目(以逗号分隔)和运行模式
html = etree.parse('main.xml')
runmode = html.xpath('//run/mode')[0].text                       #运行模式，RUN或者DEBUG
projects = html.xpath('//run/project')[0].text.split(',')       #运行的项目名，逗号分隔
allurepath = html.xpath('//run/allure')[0].text                  #ALLURE_COMMANDER_LINE安装路径
webserverdir  = html.xpath('//run/serverdir')[0].text            #展示ALLURE报表的WEB服务器地址

#迭代项目执行
for curProject in projects:
    #项目目录
    basedir = 'tests\\%s\\'%(curProject)
    #运行文件
    runfile = basedir + "config\\run.xml" if runmode=="run" else basedir + "config\\debug.xml"

    #项目下的TEST文件或DEBUG文件，当前默认一个项目一个SUITE生成一个LOG文件
    try:
        html = etree.parse(runfile)
        suite = html.xpath('//suite')[0]
        files = suite.xpath('//suite/files/file')
    except:
        raise NameError, ("main.xml文件配置错误，无法找到运行文件%" % runfile)

    #项目参数
    pd = publicData()
    pd.setProjectConfig(curProject,suite.get('name'))
    pd.setRunMode(runmode)
    DatabaseConn.init()

    param = ""
    #遍历用例执行文件
    for  curFile in files:
        #用例文件名
        filename = "%s.py"%(curFile.get('name'))
        #文件路径
        filepath = "%stestcase\\%s"%(basedir,filename)
        #有子元素
        if len(curFile) > 0:
            for child in curFile:
                param = "%s%s::%s "%(param,filepath,child.text)
        else:
            param = "%s%s "%(param,filepath)

    #输出LOG文件
    # logfile = "--junitxml=%slog/%s.xml"%(basedir,curProject)
    # logfile = "--html=%slog/%s.html  --self-contained-html"%(basedir,curProject)
    #WEB服务器路径，用于展示ALLURE报表
    serverdir = "%s\\zhan\\%s" % (webserverdir, curProject)
    #日志文件保存路径
    logfile = "--alluredir %s\\log"%(serverdir)
    #PYTEST执行参数
    runparam = "-s %s%s"%(param,logfile)

    if __name__ == '__main__':
        pytest.main(runparam)

    #处理REPORT，如果已经有REPORT，先删除，再重新生成
    reportdir = "%s\\reporter"%(serverdir)
    if os.path.exists(reportdir):
        shutil.rmtree(reportdir)
    allcmd = "%s\\allure generate -c %s\\log -o %s" % (allurepath,serverdir,reportdir)
    os.system(allcmd)

    #在ALLURE中拿到主要的统计数据passed,failed
    result={'passed':0,'failed':0}
    for f in os.listdir("%s\\log"%(serverdir)):
        if os.path.splitext(f)[1] == ".xml":
            html = etree.parse("%s\\log\\%s"%(serverdir,f))
            suite = html.getroot()
            suite = suite.find("test-cases",{'ns0':'urn:model.allure.qatools.yandex.ru'})
            for testcase in suite.findall('test-case'):
                if testcase.get('status') == 'failed':
                    result['failed'] = result['failed'] + 1
                elif testcase.get('status') == 'passed':
                    result['passed'] = result['passed'] + 1
    #报表URL
    reporturl = "http://localhost:80/zhan/%s/reporter/index.html"%(curProject)

    mh.sendMail( "%s\\config\\config.xml"%(basedir),curProject,result,reporturl,"%s\\report.html"%serverdir)

    #项目执行结束后的清理
    pd.tearDown()
    DatabaseConn.closeConn()