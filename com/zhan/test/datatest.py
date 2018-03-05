#encoding: utf-8

import requests,json

# import pymssql,random
#
# conn = pymssql.connect(host='192.168.41.11', user='sa', password='xzasdfg@123', database='Zhan_PublicClass', charset="utf8")
# cursor = conn.cursor()
#
# fw = open(r'e:\test.txt',mode='w')
# # fr = open(r'e:\ppid.dat',mode='r')
#
# # for i in range(1,30000):
# #     ran = random.randint(1,200)
# #     str = r"update Zhan_Operation_Activity_SignClock set groupid = '%s' where id = '%s'"%(ran,i) + "\n"
# #     fw.write(str)
# # fw.close()
#
#
# for ppid in  open(r'e:\ppid.dat',mode='r').readlines():
#     for activityid in open(r'e:\activityId.dat',mode='r').readlines():
#             str = r"INSERT INTO [dbo].[Tpo_PublicClass_Activitity_SignUp] ([ActivityID], [ChannelCode], [CreatedBy], [CreateTime], [SignUpUserID], [IsAudit], [TimeStamp]) VALUES (N'%s', N'LY2016111511', N'1', N'2017-01-10 15:51:54.460', N'%s', N'1', DEFAULT)"%(activityid.strip(),ppid.strip()) + "\n"
#         #     # cursor.execute(str)
#         #     # print(cursor.fetchone())
#             fw.write(str)
#
# fw.close()

fw = open(r'e:\test.txt',mode='w')
# fr = open(r'e:\ppid.dat',mode='r')

for ppid in  open(r'e:\signupuserid.txt',mode='r').readlines():
    userid = str(int(ppid.strip()) + 5000000000)
    r = requests.post("http://192.168.41.11:8001/publicclass/getpublicclassvideourl", data={"UserId":userid,"PublicClassId":953}, verify=False)
    obj = json.loads(r.text)
    res =obj['Data'].encode("utf-8")[-32:]  + "\n"
    fw.write(res)

fw.close()