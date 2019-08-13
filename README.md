# 基于指静脉识别的校园安全保障系统设计与实现
本程序用于指静脉图像的识别，需与MySQL结合使用。

## 使用步骤
**一、设置MySQL**   
1. MySQL用户名设为“root”，密码设为“123456”。  
2. 建立名为“FVRT”的数据库。  
3. 在“FVRT”数据库下通过下列语句建立名为“image”的数据表：  
CREATE TABLE if NOT EXISTS image ( id int unsigned primary key auto_increment,imname text NOT NULL,imdata mediumblob NOT NULL,
imcount INT NOT NULL,KEY(imname(15)))character set = utf8;  

**二、运行程序（1、2任意一种方法）**  
1. 编译脚本  
在您的IDE（建议Pycharm）中建立文件夹，将路径为“./源码”的源码拷入。因本程序用wxPython编写GUI以方便使用，故从路径为“./源码/FVRT_FrameStart.py”中的代码开始启动本程序界面，结合路径为“./指静脉样本”中附带的指静脉样本运行。  
2. 运行可执行文件  
路径为“./exe.win-amd64-3.5.7z”的文件为可执行文件，结合路径为“./指静脉样本”中附带的指静脉样本运行。

## 注意
1. 名为“指静脉样本”的文件中包含采集的指静脉样本图像，文件名格式为“FXXYY.bmp”，其中文件名内的“XX”表示被采集指静脉图像的志愿者的身份编号，文件名内的“YY”表示对编号为“XX”的志愿者所采集到的指静脉图像的编号。图像资源大小为64（个志愿者）×15（张图/志愿者）。
2. 核心算法在路径为“./源码/FVRT.py”的FVRT.py文件中。

## 缺陷
该项目因是本人大学时所设计，尚不成熟，还有很多改进的余地：
1. 图像搜索速度：没有利用搜索算法对指静脉样本的特征值进行整合，降低了程序运行的效率。
2. 数据库设计：对MySQL一定要设置特定的用户名和密码才能执行，这给使用的人带来一些麻烦。
3. UI架构选取：写界面时为了贪快只考虑wxPython的灵活性，没有注意到PyQt的文档更全面，给后续开发带来不便。

## 程序运行截图
**一、程序界面**
 <div align="center">
 <img src="https://github.com/bmxbmx3/Finger_Vein_Recognition/blob/master/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E7%A8%8B%E5%BA%8F%E7%95%8C%E9%9D%A2/%E4%B8%BB%E7%95%8C%E9%9D%A2.png" width="60%"/>
  <br>主界面</br>
  <br></br>
</div>

<div align="center">
  <img src="https://github.com/bmxbmx3/Finger_Vein_Recognition/blob/master/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E7%A8%8B%E5%BA%8F%E7%95%8C%E9%9D%A2/%E5%9B%BE%E5%83%8F%E5%8C%B9%E9%85%8D%E7%95%8C%E9%9D%A2.png" width="60%"/>
  <br>图像匹配界面</br>
  <br></br>
</div>

<div align="center">
  <img src="https://github.com/bmxbmx3/Finger_Vein_Recognition/blob/master/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E7%A8%8B%E5%BA%8F%E7%95%8C%E9%9D%A2/%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%86%E7%95%8C%E9%9D%A2.png" width="60%"/>
  <br>图像处理界面</br>
  <br></br>
</div>

<div align="center">
  <img src="https://github.com/bmxbmx3/Finger_Vein_Recognition/blob/master/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E7%A8%8B%E5%BA%8F%E7%95%8C%E9%9D%A2/%E5%9B%BE%E5%83%8F%E8%BE%93%E5%85%A5%E7%95%8C%E9%9D%A2.png" width="60%"/>
  <br>图像输入界面</br>
  <br></br>
</div>

<div align="center">
  <img src="https://github.com/bmxbmx3/Finger_Vein_Recognition/blob/master/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E7%A8%8B%E5%BA%8F%E7%95%8C%E9%9D%A2/%E5%9B%BE%E5%83%8F%E8%BE%93%E5%87%BA%E7%95%8C%E9%9D%A2.png" width="60%"/>
  <br>图像输出界面</br>
  <br></br>
</div>

**二、指静脉图像匹配结果示例**
<div align="center">
 <img src="https://github.com/bmxbmx3/Finger_Vein_Recognition/blob/master/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E6%8C%87%E9%9D%99%E8%84%89%E5%9B%BE%E5%83%8F%E5%8C%B9%E9%85%8D%E7%BB%93%E6%9E%9C%E7%A4%BA%E4%BE%8B/1%E3%80%81%E5%BE%85%E8%AF%86%E5%88%AB%E7%9A%84%E5%9B%BE%E5%83%8F_%E5%8E%9F%E5%9B%BE%EF%BC%9A%E2%80%9CF0101.bmp%E2%80%9D.bmp" width="20%"/>
  <br>待识别的图像_原图：“F0101.bmp”</br>
  <br></br>
</div>

<div align="center">
 <img src="https://github.com/bmxbmx3/Finger_Vein_Recognition/blob/master/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E6%8C%87%E9%9D%99%E8%84%89%E5%9B%BE%E5%83%8F%E5%8C%B9%E9%85%8D%E7%BB%93%E6%9E%9C%E7%A4%BA%E4%BE%8B/2%E3%80%81%E5%BE%85%E8%AF%86%E5%88%AB%E7%9A%84%E5%9B%BE%E5%83%8F_%E5%B0%BA%E5%AF%B8%E5%BD%92%E4%B8%80%E5%8C%96.bmp" width="20%"/>
  <br>待识别的图像_尺寸归一化</br>
  <br></br>
</div>

<div align="center">
 <img src="https://github.com/bmxbmx3/Finger_Vein_Recognition/blob/master/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E6%8C%87%E9%9D%99%E8%84%89%E5%9B%BE%E5%83%8F%E5%8C%B9%E9%85%8D%E7%BB%93%E6%9E%9C%E7%A4%BA%E4%BE%8B/3%E3%80%81%E5%BE%85%E8%AF%86%E5%88%AB%E7%9A%84%E5%9B%BE%E5%83%8F_%E7%81%B0%E5%BA%A6%E5%BD%92%E4%B8%80%E5%8C%96.bmp" width="20%"/>
  <br>待识别的图像_灰度归一化</br>
  <br></br>
</div>

<div align="center">
 <img src="https://github.com/bmxbmx3/Finger_Vein_Recognition/blob/master/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E6%8C%87%E9%9D%99%E8%84%89%E5%9B%BE%E5%83%8F%E5%8C%B9%E9%85%8D%E7%BB%93%E6%9E%9C%E7%A4%BA%E4%BE%8B/4%E3%80%81%E5%BE%85%E8%AF%86%E5%88%AB%E7%9A%84%E5%9B%BE%E5%83%8F_%E6%96%B9%E5%90%91%E8%B0%B7%E5%9E%8B%E6%A3%80%E6%B5%8B.bmp" width="20%"/>
  <br>待识别的图像_方向谷型检测</br>
  <br></br>
</div>

<div align="center">
  <img src="https://github.com/bmxbmx3/Finger_Vein_Recognition/blob/master/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E6%8C%87%E9%9D%99%E8%84%89%E5%9B%BE%E5%83%8F%E5%8C%B9%E9%85%8D%E7%BB%93%E6%9E%9C%E7%A4%BA%E4%BE%8B/5%E3%80%81%E5%BE%85%E8%AF%86%E5%88%AB%E7%9A%84%E5%9B%BE%E5%83%8F_%E6%A8%A1%E7%B3%8A%E5%A2%9E%E5%BC%BA.bmp" width="20%"/>
  <br>待识别的图像_模糊增强</br>
  <br></br>
</div>

<div align="center">
 <img src="https://github.com/bmxbmx3/Finger_Vein_Recognition/blob/master/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E6%8C%87%E9%9D%99%E8%84%89%E5%9B%BE%E5%83%8F%E5%8C%B9%E9%85%8D%E7%BB%93%E6%9E%9C%E7%A4%BA%E4%BE%8B/6%E3%80%81%E5%BE%85%E8%AF%86%E5%88%AB%E7%9A%84%E5%9B%BE%E5%83%8F_%E9%98%88%E5%80%BC%E5%88%86%E5%89%B2.bmp" width="20%"/>
  <br>待识别的图像_阈值分割</br>
  <br></br>
</div>

<div align="center">
 <img src="https://github.com/bmxbmx3/Finger_Vein_Recognition/blob/master/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E6%8C%87%E9%9D%99%E8%84%89%E5%9B%BE%E5%83%8F%E5%8C%B9%E9%85%8D%E7%BB%93%E6%9E%9C%E7%A4%BA%E4%BE%8B/7%E3%80%81%E5%BE%85%E8%AF%86%E5%88%AB%E7%9A%84%E5%9B%BE%E5%83%8F_%E5%8E%BB%E5%99%AA.bmp" width="20%"/>
  <br>待识别的图像_去噪</br>
  <br></br>
</div>

<div align="center">
 <img src="https://github.com/bmxbmx3/Finger_Vein_Recognition/blob/master/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E6%8C%87%E9%9D%99%E8%84%89%E5%9B%BE%E5%83%8F%E5%8C%B9%E9%85%8D%E7%BB%93%E6%9E%9C%E7%A4%BA%E4%BE%8B/8%E3%80%81%E5%BE%85%E8%AF%86%E5%88%AB%E7%9A%84%E5%9B%BE%E5%83%8F_%E7%BB%86%E5%8C%96.bmp" width="20%"/>
  <br>待识别的图像_细化</br>
  <br></br>
</div> 

<div align="center">
<img src="https://github.com/bmxbmx3/Finger_Vein_Recognition/blob/master/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E6%8C%87%E9%9D%99%E8%84%89%E5%9B%BE%E5%83%8F%E5%8C%B9%E9%85%8D%E7%BB%93%E6%9E%9C%E7%A4%BA%E4%BE%8B/9%E3%80%81%E5%BE%85%E8%AF%86%E5%88%AB%E7%9A%84%E5%9B%BE%E5%83%8F_%E5%8E%BB%E9%99%A4%E6%AE%8B%E4%BD%99%E6%96%91%E7%82%B9.bmp" width="20%"/>
  <br>待识别的图像_去除残余斑点</br>
  <br></br>
</div> 

<div align="center">
<img src="https://github.com/bmxbmx3/Finger_Vein_Recognition/blob/master/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E6%8C%87%E9%9D%99%E8%84%89%E5%9B%BE%E5%83%8F%E5%8C%B9%E9%85%8D%E7%BB%93%E6%9E%9C%E7%A4%BA%E4%BE%8B/10%E3%80%81%E4%B8%8E%E4%B9%8B%E5%8C%B9%E9%85%8D%E7%9A%84%E5%9B%BE%E5%83%8F%EF%BC%9A%E2%80%9CF0108.bmp%E2%80%9D.bmp" width="20%"/>
  <br>与之匹配的图像：“F0108.bmp”</br>
  <br></br>
</div> 

## 声明
Finger_Vein_Recognition为本人（bmxbmx3）参与2017年南京邮电大学大学生创新训练计划独自设计的作品，主要用于指静脉识别的实现，仅供学习研究之用，请勿用于非法用途，如有疑问欢迎提issue留言。
