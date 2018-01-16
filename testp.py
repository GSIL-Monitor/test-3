#encoding: utf-8

class AttrTest():
    @staticmethod
    def contains(response,expected,operator,**kwargs):
        print(response,expected)
        print(kwargs['func1']['aa'])


getattr(AttrTest,'contains')('my response','expected','operator',func1={'aa':'bb','cc':'dd'})