#encoding: utf-8

from .Singleton import Singleton

# #单例
# class Singleton(object):
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kw)
#         return cls._instance

@Singleton
# class publicData(Singleton):
class publicData(object):
    __projectName = ""    #当前执行项目名称
    __mainDir = ""        #项目主目录
    __suiteName = ""      #SUITE名称
    __output = {}         #用于保存输出参数
    __runMode = ""        #运行模式，debug或者run

    def __init__(self):
        pass

    def setProjectConfig(self,projectName, suiteName):
        self.__projectName = projectName
        self.__mainDir = r"tests\%s" % (projectName)
        self.__suiteName = suiteName
        self.__output = {}
        self.__runMode = ""

    def tearDown(self):
        self.__projectName = ""
        self.__mainDir = ""
        self.__suiteName = ""
        self.__output = {}
        self.__runMode = ""

    def getSuiteName(self):
        return self.__suiteName

    def getProjectName(self):
        return self.__projectName

    def getMainDir(self):
        return self.__mainDir

    def setOutput(self,key,value):
        self.__output[key] = value

    def getOutputKeys(self):
        return self.__output.keys()

    def getOutput(self,key):
        return self.__output[key]

    def setRunMode(self,mode):
        self.__runMode = mode

    def getRunMode(self):
        return self.__runMode
