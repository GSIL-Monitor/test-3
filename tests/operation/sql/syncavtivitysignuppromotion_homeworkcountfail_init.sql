--删除当日的数据
DELETE FROM [dbo].[Tpo_PublicClass_Activitity_SignUp] where  [ActivityID] in ('1005');
DELETE FROM [dbo].[Tpo_PublicClass_Activitity_Moment] WHERE [ActivitityID] in ('1005');
DELETE FROM [dbo].[Tpo_PublicClass_Activities] WHERE [ActivityID] in ('1005');
DELETE FROM [dbo].[Zhan_Operation_Activities_Group] WHERE [GroupID] in ('1005');
DELETE FROM [dbo].[Tpo_PublicClass_Activities_Course] WHERE [ActivityID] in ('1005');
DELETE FROM [dbo].[Zhan_Operation_Activities_Work] WHERE [ActivityID] in ('1005');
--新建活动1005
SET IDENTITY_INSERT [dbo].[Tpo_PublicClass_Activities] ON
INSERT INTO [dbo].[Tpo_PublicClass_Activities] ([ActivityID], [ActivityTitle], [ActivityDescription], [SignUpExpectCount], [SignUpActualCount], [StartTime], [EndTime], [CreateTime], [CreatedBy], [UpdateTime], [UpdatedBy], [IsDeleted], [LinkUrl], [ActivityCategory], [ActivityShortDescription], [ActivityTip], [CoverImageUrl], [ActivityType], [AdvertiseStartTime], [AdvertiseEndTime], [AssistentWechatID], [CheckCode], [TeacherIds], [QRCodeUrl], [BindAccountUrl], [ActivityItem], [ActivityLabel], [SuitCrowds], [SolveProblems], [RecruitVideo], [RecruitImage], [OpeningVideo], [OpeningImage]) VALUES (N'1005', N'PromotionTest', N'晋级活动测试', N'3000', N'12',CONVERT(varchar,dateadd(day,-5,GETDATE()),120), CONVERT(varchar,dateadd(day,15,GETDATE()),120), N'2018-02-05 16:40:51.390', N'1', N'2018-02-07 10:55:10.120', N'1', N'0', null, N'2', N'活动短描述', N'入群须知测试123', N'59e98ae765144f38b5221d99bc92bbd820180205164128764', N'9982', CONVERT(varchar,dateadd(day,-20,GETDATE()),120), CONVERT(varchar,dateadd(day,-10,GETDATE()),120), N'7', N'测试', N'488', null, N'3197558d421649b0ac0333331dea9db620180207105510', N'9901', null, N'目标,渴望老师指导', N'不懂评分标准,题型区分不清,语法错误太多', N'892db97b11d50e2c099b4c6964ccbe60', N'bc8f2887f2d1c55a3f5f3dd3f16fdd0e', null, null)
SET IDENTITY_INSERT [dbo].[Tpo_PublicClass_Activities] OFF
--活动阶段，无条件
SET IDENTITY_INSERT [dbo].[Tpo_PublicClass_Activitity_Moment] ON
INSERT INTO [dbo].[Tpo_PublicClass_Activitity_Moment] ([MomentId], [ActivitityId], [BeginDate], [EndDate], [MomentDescription], [ReachHomeworkTimes], [HasPromotionForm], [SignClockCount]) VALUES ( N'1005', N'1005', CONVERT(varchar,dateadd(day,-1,GETDATE()),23), CONVERT(varchar,dateadd(day,-1,GETDATE()),23), null, N'1', 0, 0)
INSERT INTO [dbo].[Tpo_PublicClass_Activitity_Moment] ([MomentId], [ActivitityId], [BeginDate], [EndDate], [MomentDescription], [ReachHomeworkTimes], [HasPromotionForm], [SignClockCount]) VALUES ( N'1006', N'1005', CONVERT(varchar,dateadd(day,0,GETDATE()),23), CONVERT(varchar,dateadd(day,0,GETDATE()),23), null, 0, 0, 0)
SET IDENTITY_INSERT [dbo].[Tpo_PublicClass_Activitity_Moment] OFF
--新建活动作业
SET IDENTITY_INSERT [dbo].[Tpo_PublicClass_Activities_Course] ON
INSERT INTO [dbo].[Tpo_PublicClass_Activities_Course] ([ID], [ActivityID], [CourseType], [StartTime], [EndTime], [VideoUrl], [VideoID], [CreateTime], [CreatedBy], [CourseCommand]) VALUES (N'1005', N'1005', N'5', CONVERT(varchar,dateadd(day,-1,GETDATE()),23) + ' 00:00:00', CONVERT(varchar,dateadd(day,0,GETDATE()),23) + ' 00:00:00', null, null, N'2018-03-29 20:21:20.457', N'1', N'小站5157')
SET IDENTITY_INSERT [dbo].[Tpo_PublicClass_Activities_Course] OFF
--新建活动的班级
SET IDENTITY_INSERT [dbo].[Zhan_Operation_Activities_Group] ON
INSERT INTO [dbo].[Zhan_Operation_Activities_Group] ([GroupID], [GroupName], [ActivityID], [LinkUrlDivideClass], [LinkUrlSignIn], [DepartmentId], [Remark], [IsDeleted], [CreateTime], [CreatedBy], [UpdateTime], [UpdatedBy], [TimeStamp]) VALUES (N'1005', N'活动微信群5', N'1005', N'http://testDivideClassLink.com/?ActivityID=11414&GroupID=1', N'http://testSignInLink.com/?ActivityID=11414&GroupID=1', N'10149', N'Group_Vincent', N'0', N'2018-02-28 17:29:13.540', N'1', N'2018-02-28 17:29:13.540', N'1', DEFAULT);
SET IDENTITY_INSERT [dbo].[Zhan_Operation_Activities_Group] OFF
--写入报名记录，绑定班级
INSERT INTO [dbo].[Tpo_PublicClass_Activitity_SignUp] ([ActivityID], [ChannelCode], [CreatedBy], [CreateTime], [SignUpUserID], [IsAudit], [TimeStamp], [GroupName], [GroupNickName], [MomentID], [Moment], [CheckinCount], [HomeworkCount], [HomeworkAccuracy], [PromotionCount]) VALUES (N'1005', N'LY2016111506', N'1', N'2017-01-07 16:20:57.000', N'19710', N'1', DEFAULT, N'活动微信群5', N'newname', N'1005', N'第1阶段', null, null, null, null)
