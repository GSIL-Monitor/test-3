--删除当日的打卡数据
DELETE FROM [dbo].[Zhan_Operation_Activity_SignClock] where [SignDate] between cast(convert(varchar(10),dateadd(day,0,GETDATE()),120)+' 00:00:00' as datetime) and cast(convert(varchar(10),dateadd(day,1,GETDATE()),120)+' 00:00:00' as datetime)
DELETE FROM [dbo].[Zhan_Operation_Activity_SignClock] where  [Id] in ('1000','1001','1002');
DELETE FROM [dbo].[Tpo_PublicClass_Activitity_SignUp] where  [ActivityID] in ('1001');
--插入当日打卡记录
SET IDENTITY_INSERT [dbo].[Zhan_Operation_Activity_SignClock] ON
INSERT INTO [dbo].[Zhan_Operation_Activity_SignClock] ([Id], [SignDate], [ActivityId], [MomentId], [GroupId], [SignUpUserId], [CreateTime], [CreateBy], [UpdateTime], [UpdateBy], [TimeStamp]) VALUES (N'1001', CONVERT(varchar,dateadd(day,0,GETDATE()),120), N'1001', N'0', N'1001', N'21905', N'2018-03-05 19:49:10.450', N'1', N'2018-03-05 19:49:10.450', N'1', DEFAULT)
INSERT INTO [dbo].[Zhan_Operation_Activity_SignClock] ([Id], [SignDate], [ActivityId], [MomentId], [GroupId], [SignUpUserId], [CreateTime], [CreateBy], [UpdateTime], [UpdateBy], [TimeStamp]) VALUES (N'1000', CONVERT(varchar,dateadd(day,0,GETDATE()),120), N'1001', N'0', N'1001', N'19710', N'2018-03-05 19:49:10.450', N'1', N'2018-03-05 19:49:10.450', N'1', DEFAULT)
SET IDENTITY_INSERT [dbo].[Zhan_Operation_Activity_SignClock] OFF
--插一条昨天的打卡记录
INSERT INTO [dbo].[Zhan_Operation_Activity_SignClock] ([SignDate], [ActivityId], [MomentId], [GroupId], [SignUpUserId], [CreateTime], [CreateBy], [UpdateTime], [UpdateBy], [TimeStamp]) VALUES (CONVERT(varchar,dateadd(day,-1,GETDATE()),120), N'1001', N'0', N'1001', N'19710', N'2018-03-05 19:49:10.450', N'1', N'2018-03-05 19:49:10.450', N'1', DEFAULT)
--写入报名记录，绑定班级
INSERT INTO [dbo].[Tpo_PublicClass_Activitity_SignUp] ([ActivityID], [ChannelCode], [CreatedBy], [CreateTime], [SignUpUserID], [IsAudit], [TimeStamp], [GroupName], [GroupNickName], [MomentID], [Moment], [CheckinCount], [HomeworkCount], [HomeworkAccuracy], [PromotionCount]) VALUES (N'1001', N'LY2016111506', N'1', N'2017-01-07 16:20:57.000', N'19710', N'1', DEFAULT, N'活动测试群2', N'testName', null, null, null, null, null, null)
INSERT INTO [dbo].[Tpo_PublicClass_Activitity_SignUp] ([ActivityID], [ChannelCode], [CreatedBy], [CreateTime], [SignUpUserID], [IsAudit], [TimeStamp], [GroupName], [GroupNickName], [MomentID], [Moment], [CheckinCount], [HomeworkCount], [HomeworkAccuracy], [PromotionCount]) VALUES (N'1001', N'LY2016111506', N'1', N'2017-01-07 16:20:57.000', N'21905', N'1', DEFAULT, N'活动测试群2', N'newname', null, null, null, null, null, null)
