#encoding: utf-8

import pytest
from com.zhan.test.publicData import publicData


ff = 'aaaaaaaaaaaaaa'
pd = publicData()
pd.setOutput('xdist', 'aaaaaa')

def value(method):
    pa = ['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh']
    return pa

#测试getlatestactivity接口
@pytest.mark.parametrize("processname", value("publicclasscheck"))
def test_publicclasscheck(processname):
    pd = publicData()
    assert pd.getOutput('xdist') == 'aaaaaa'


#测试getlatestactivity接口
# @pytest.mark.parametrize("processname", value("publicclasscheck"))
def test_public():
    print ff

#测试getlatestactivity接口
# @pytest.mark.parametrize("processname", value("publicclasscheck"))
def test_thread():
    pd = publicData()
    assert pd.getOutput('xdist') == 'aaaaaa'