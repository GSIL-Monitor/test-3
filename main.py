#encoding: utf-8

import warnings,sys,os
import com.zhan.test.MailHelper as mh
import com.zhan.test.AppDBHelper as dh
from com.zhan.test.publicData import publicData
from com.zhan.test.Utils import FuncUtil
import pytest
from lxml import etree
import shutil

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(r'C:\Users\Administrator\PycharmProjects\test')
#忽略 HTTPS中不验证证书的WARNING
warnings.filterwarnings('ignore')

#从配置文件中得到待运行项目(以逗号分隔)和运行模式
html = etree.parse('main.xml')
runmode = html.xpath('//run/mode')[0].text                       #运行模式，RUN或者DEBUG
projects = html.xpath('//run/project')[0].text.split(',')       #运行的项目名，逗号分隔
allurepath = html.xpath('//run/allure')[0].text                  #ALLURE_COMMANDER_LINE安装路径
webserverdir  = html.xpath('//run/serverdir')[0].text            #展示ALLURE报表的WEB服务器地址
reporttype = html.xpath('//run/report')[0].text                      #报表方式

#迭代项目执行
for curProject in projects:
    #项目目录
    basedir = r'tests\%s'%(curProject)
    #运行文件
    runfile = r'%s\config\run.xml'%(basedir)  if runmode=="run" else r'%s\config\debug.xml'%(basedir)

    pd = publicData()
    pd = FuncUtil.initPublicData(curProject)
    #sql初始化
    initSqlFile = r'%s\sql\init.sql'%(basedir)
    if os.path.exists(initSqlFile) :
        dbConn = dh.DBConn()
        dbConn.exeSqlFile(initSqlFile)

    #项目下的TEST文件或DEBUG文件，当前默认一个项目一个SUITE生成一个LOG文件
    try:
        htmltest = etree.parse(runfile)
        suite = htmltest.xpath('//suite')[0]
        files = suite.xpath('//suite/files/file')
    except:
        raise NameError, ("main.xml文件配置错误，无法找到运行文件%" % runfile)

    param = ""
    filenum = len(files)
    #遍历用例执行文件
    for  curFile in files:
        #文件路径
        filepath = r"%s\testcase\%s.py"%(basedir,curFile.get('name'))
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
    serverdir = r"%s\zhan\%s" % (webserverdir, curProject)
    #日志文件保存路径
    logfile = r"--alluredir %s\log"%(serverdir)
    #PYTEST执行参数
    if filenum == 1:
        runparam = "-s %s %s"%(param,logfile)
    else:
        runparam = "-s %s -n%s -v --dist=loadscope %s"%(param,filenum,logfile)

    if __name__ == '__main__':
        pytest.main(runparam)

    #处理REPORT，如果已经有REPORT，先删除，再重新生成
    reportdir = r"%s\reporter"%(serverdir)
    if os.path.exists(reportdir):
        shutil.rmtree(reportdir)
    allcmd = r"%s\allure generate -c %s\log -o %s" % (allurepath,serverdir,reportdir)
    os.system(allcmd)

    #在ALLURE中拿到主要的统计数据passed,failed
    result={'passed':0,'failed':0}
    for f in os.listdir(r"%s\log"%(serverdir)):
        if os.path.splitext(f)[1] == ".xml":
            html = etree.parse(r"%s\log\%s"%(serverdir,f))
            suite = html.getroot()
            suite = suite.find("test-cases",{'ns0':'urn:model.allure.qatools.yandex.ru'})
            for testcase in suite.findall('test-case'):
                if testcase.get('status') == 'failed':
                    result['failed'] = result['failed'] + 1
                elif testcase.get('status') == 'passed':
                    result['passed'] = result['passed'] + 1
    #报表URL
    reporturl = "http://localhost:80/zhan/%s/reporter/index.html"%(curProject)

    mh.sendMail( r"%s\config\config.xml"%(basedir),curProject,result,reporturl,r"%s\report.html"%serverdir)

    #清理数据数据
    # endSqlFile = r'%s\sql\end.sql'%(basedir)
    # if os.path.exists(endSqlFile) :
    #     dbConn.exeSqlFile(endSqlFile)
    pd.tearDown()