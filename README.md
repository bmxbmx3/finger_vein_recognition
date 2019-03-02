# Finger_Vein_Recognition
本程序用于指静脉图像的识别，需与MySQL结合使用。
在使用本程序前，您需确保系统已配置MySQL，如确认完毕，按如下步骤操作。

MySQL准备：
1、MySQL用户名设为“root”，密码设为“123456”。
2、建立名为“FVRT”的数据库。
3、在“FVRT”数据库下通过下列语句：
CREATE TABLE if NOT EXISTS image ( id int unsigned primary key auto_increment,imname text NOT NULL,imdata mediumblob NOT NULL,
imcount INT NOT NULL,KEY(imname(15)))character set = utf8;
建立名为“image”的数据表。

接下来即可打开“exe.win-amd64-3.5”文件下的“指静脉识别.exe”程序结合附带的指静脉样本运行。
