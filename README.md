### Finger_Vein_Recognition
本程序用于指静脉图像的识别，需与MySQL结合使用。

# 使用说明
**一、MySQL准备**   
1. MySQL用户名设为“root”，密码设为“123456”。  
2. 建立名为“FVRT”的数据库。  
3. 在“FVRT”数据库下通过下列语句建立名为“image”的数据表：  
CREATE TABLE if NOT EXISTS image ( id int unsigned primary key auto_increment,imname text NOT NULL,imdata mediumblob NOT NULL,
imcount INT NOT NULL,KEY(imname(15)))character set = utf8;  

**二、运行程序（1、2任意一种方法）**  
1. 编译脚本  
在您的IDE（建议Pycharm）中建立文件夹，将路径为“./源码”的源码拷入。因本程序用wxPython编写GUI以方便使用，故从路径为“./源码/FVRT_FrameStart.py”中的代码开始启动本程序界面，结合路径为“./源码/指静脉样本”中附带的指静脉样本运行。  
2. 运行可执行文件  
路径为“./exe.win-amd64-3.5.7z”的文件为可执行文件，结合路径为“./源码/指静脉样本”中附带的指静脉样本运行。
