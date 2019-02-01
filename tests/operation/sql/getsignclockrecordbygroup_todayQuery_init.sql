-- -- --删除用户的打卡数据
DELETE FROM Zhan_Operation_Activity_SignClock where SignUpUserId in ('531059','531457');
-- -- --插入当日打卡记录
INSERT INTO Zhan_Operation_Activity_SignClock (Id, SignDate, ActivityId, MomentId, GroupId, SignUpUserId, CreateTime, CreateBy, UpdateTime, UpdateBy, TimeStamp) VALUES ('1001', NOW(), '1000', '1000', '1001', '531059', '2018-03-05 19:49:10.450', '1', '2018-03-05 19:49:10.450', '1', DEFAULT);
INSERT INTO Zhan_Operation_Activity_SignClock (Id, SignDate, ActivityId, MomentId, GroupId, SignUpUserId, CreateTime, CreateBy, UpdateTime, UpdateBy, TimeStamp) VALUES ('1000', NOW(), '1000', '1000', '1001', '531457', '2018-03-05 19:49:10.450', '1', '2018-03-05 19:49:10.450', '1', DEFAULT);
-- -- --插一条昨天的打卡记录
INSERT INTO Zhan_Operation_Activity_SignClock (SignDate, ActivityId, MomentId, GroupId, SignUpUserId, CreateTime, CreateBy, UpdateTime, UpdateBy, TimeStamp) VALUES (DATE_SUB(NOW(),INTERVAL 1 DAY), '1000', '1000', '1000', '531059', '2018-03-05 19:49:10.450', '1', '2018-03-05 19:49:10.450', '1', DEFAULT);
commit;