#encoding: utf-8

import requests
import json,threading
from com.zhan.test.Utils import xmlUtil,JsonUtil,FuncUtil
from com.zhan.test.publicData import publicData

class httpExecuter:
    @staticmethod
    def executeHttpRequest(methodname,casename,casedata):
        pd = publicData()
        configEle = xmlUtil.getConfigEleByMethod(r'%s\config\api.xml'%(pd.getMainDir()), methodname)
        url = configEle.find('url').text
        protocol = configEle.find('protocol').text
        output = configEle.find('output')

        if protocol == 'post':
            resText = httpExecuter.__postExecute(url,casedata)
        elif protocol == 'get':
            resText = httpExecuter.__getExecute(url,casedata)
        elif protocol == 'json':
            resText = httpExecuter.__postJson(url,casedata)

        #输出output
        if output <> None:
            outresult = None
            try:
                outresult = JsonUtil.getJsonStrByPar(resText,output.text)
            except NameError:
                pass

            lock = threading.Lock()
            lock.acquire()
            try:
                pd.setOutput('%s_%s' % (output.get("name"), threading.currentThread().ident), outresult)
            finally:
                lock.release()

        return resText


    @staticmethod
    def __postExecute(url,casedata):
        r = requests.post(url, data=httpExecuter.__getBodyByCasedata(casedata), verify=False)
        return r.text

    @staticmethod
    def __getExecute(url,casedata):
        r = requests.get(url,params=httpExecuter.__getBodyByCasedata(casedata), verify=False)
        return r.text

    @staticmethod
    def __postJson(url,casedata):
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, headers=headers, data=json.dumps(httpExecuter.__getBodyByCasedata(casedata)), verify=False)
        return r.text

    #通过TestCase的节点生成Json数据
    @staticmethod
    def __getBodyByCasedata(casedata):
        body = {}
        for i in xrange(len(casedata)):
            if casedata[i].get('type') == None:
                if len(casedata[i].getchildren()) > 0:
                    res = httpExecuter.__getBodyByCasedata(casedata[i])
                    body[casedata[i].tag] = res
                else:
                    body[casedata[i].tag] = casedata[i].text
            elif casedata[i].get('type') == "func":
                method = casedata[i].get('method')
                param = casedata[i].get('param')
                result = getattr(FuncUtil, method)(param)
                body[casedata[i].tag] = result
            elif casedata[i].get('type') == "array":
                if casedata[i].text == None:
                    body[casedata[i].tag] = []
                else:
                    body[casedata[i].tag] = casedata[i].text.split(',')
        return body

