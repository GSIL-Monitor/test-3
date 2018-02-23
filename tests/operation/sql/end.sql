--delete record--
DELETE FROM [dbo].[Tpo_PublicClass] WHERE [PublicTitle] = N'ToeflTest';
GO

DELETE FROM [dbo].[Tpo_PublicClass_Activities] WHERE [ActivityTitle] = N'ToeflTest';
GO