# #encoding: utf-8
#
# import pytest,sys
# from threading import current_thread
# from com.zhan.test.publicData import publicData
#
# def value(method):
#     pd = publicData()
#     pd.setOutput('xdist','bbbbbb')
#     pa = ['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh']
#     return pa
#
# #测试getlatestactivity接口
# @pytest.mark.parametrize("processname", value("publicclasscheck"))
# def test_publicclasscheck11(processname):
#     pd = publicData()
#     assert pd.getOutput('xdist') == 'bbbbbb'
#
#
# #测试getlatestactivity接口
# # @pytest.mark.parametrize("processname", value("publicclasscheck"))
# def test_public11():
#     pd = publicData()
#     assert pd.getOutput('xdist') == 'bbbbbb'
#
# #测试getlatestactivity接口
# # @pytest.mark.parametrize("processname", value("publicclasscheck"))
# def test_thread11():
#     pd = publicData()
#     assert pd.getOutput('xdist') == 'bbbbbb'