# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from ImInputDialog import *
from ImProcessDialog import *
from ImMatchDialog import *
from ImOutputDialog import *
from RunDialog import *
import json
from FVRT import *
import builtins
from numpy import *
from math import *
import time
from threading import Thread
from pubsub import pub

###########################################################################
# Class Frame
###########################################################################


class Frame(wx.Frame):

    ImInputData = 0
    ImProcessData = 0
    ImMatchData = 0
    phashData = {"hash_size": 8, "highfreq_factor": 4, "THRESHOLD": 0.7}
    ahashData = {"hash_size": 8, "THRESHOLD": 0.7}
    dhashData = {"hash_size": 8, "THRESHOLD": 0.7}
    whashData = {"hash_size": 0, "image_scale": 0, "mode": 0, "remove_max_haar_ll": 0, "THRESHOLD": 0.7}

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"指静脉识别", pos=wx.DefaultPosition, size=wx.Size(650, 120),
                          style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(600, 120), wx.Size(-1, -1))

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel9 = wx.Panel(self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel8 = wx.Panel(self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer6 = wx.FlexGridSizer(1, 7, 0, 5)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.ImInputBtn = wx.Button(self.m_panel8, wx.ID_ANY, u"图像输入", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.ImInputBtn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.arrow_1 = wx.StaticBitmap(self.m_panel8, wx.ID_ANY, wx.Bitmap(u"arrow.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(-1, -1), 0)
        fgSizer6.Add(self.arrow_1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.ImProcessBtn = wx.Button(self.m_panel8, wx.ID_ANY, u"图像处理", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ImProcessBtn.Enable(False)

        fgSizer6.Add(self.ImProcessBtn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.arrow_2 = wx.StaticBitmap(self.m_panel8, wx.ID_ANY, wx.Bitmap(u"arrow.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(-1, -1), 0)
        fgSizer6.Add(self.arrow_2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.ImMatchBtn = wx.Button(self.m_panel8, wx.ID_ANY, u"图像匹配", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ImMatchBtn.Enable(False)

        fgSizer6.Add(self.ImMatchBtn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.arrow_2 = wx.StaticBitmap(self.m_panel8, wx.ID_ANY, wx.Bitmap(u"arrow.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(-1, -1), 0)
        fgSizer6.Add(self.arrow_2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.ImOutputBtn = wx.Button(self.m_panel8, wx.ID_ANY, u"图像输出", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ImOutputBtn.Enable(False)

        fgSizer6.Add(self.ImOutputBtn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_panel8.SetSizer(fgSizer6)
        self.m_panel8.Layout()
        fgSizer6.Fit(self.m_panel8)
        bSizer13.Add(self.m_panel8, 1, wx.ALIGN_CENTER, 5)

        self.m_panel9.SetSizer(bSizer13)
        self.m_panel9.Layout()
        bSizer13.Fit(self.m_panel9)
        bSizer11.Add(self.m_panel9, 1, wx.ALIGN_CENTER, 5)

        self.m_panel4.SetSizer(bSizer11)
        self.m_panel4.Layout()
        bSizer11.Fit(self.m_panel4)
        bSizer4.Add(self.m_panel4, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.ImInputBtn.Bind(wx.EVT_BUTTON, self.ImInput)
        self.ImProcessBtn.Bind(wx.EVT_BUTTON, self.ImProcess)
        self.ImMatchBtn.Bind(wx.EVT_BUTTON, self.ImMatch)
        self.ImOutputBtn.Bind(wx.EVT_BUTTON, self.ImOutput)

        self.AllCtrlSum = 1
        self.RunThread = 0
        pub.subscribe(self.SetImInputData, "ImInputData")
        pub.subscribe(self.SetImProcessData, "ImProcessData")
        pub.subscribe(self.SetImMatchData, "ImMatchData")
        pub.subscribe(self.SetphashData, "phashData")
        pub.subscribe(self.SetahashData, "ahashData")
        pub.subscribe(self.SetdhashData, "dhashData")
        pub.subscribe(self.SetwhashData, "whashData")
        pub.subscribe(self.SetAllCtrlSum, "AllCtrlSum")

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def ImInput(self, event):
        ImInput = ImInputDialog(self)
        with builtins.open("ImInputData.json", "r", encoding="UTF-8") as fp:
            ImInputData = json.load(fp)
        ImInput.ImInputChkList.SetImInPutList(ImInputData["FileInfoList"])
        ImInput.ImInputChkList.SetCheck(ImInputData["Check"])
        ImInput.FileInfoList = ImInputData["FileInfoList"]
        ImInput.FilePaths = ImInputData["FilePaths"]
        ImInput.Show()
        self.Enable(False)
        event.Skip()

    def ImProcess(self, event):
        ImProcess = ImProcessDialog(self)

        with builtins.open("ImProcessData.json", "r", encoding="UTF-8") as fp:
            ImProcessData = json.load(fp)
        ImProcess.widthText.SetValue(ImProcessData["width"])
        ImProcess.heightText.SetValue(ImProcessData["height"])
        ImProcess.ThreFactorText.SetValue(ImProcessData["ThreFactor"])
        ImProcess.ThreGrayText.SetValue(ImProcessData["ThreGray"])
        ImProcess.IterText.SetValue(ImProcessData["Iter"])
        ImProcess.SideLengthText.SetValue(ImProcessData["SideLength"])
        ImProcess.ThreKText.SetValue(ImProcessData["ThreK"])
        ImProcess.OpenSideText.SetValue(ImProcessData["OpenSide"])
        ImProcess.ClosedSideText.SetValue(ImProcessData["ClosedSide"])
        ImProcess.BlurSideText.SetValue(ImProcessData["BlurSide"])
        ImProcess.MinSizeText.SetValue(ImProcessData["Minsize"])
        ImProcess.Show()
        self.Enable(False)
        event.Skip()

    def ImMatch(self, event):
        ImMatch = ImMatchDialog(self)
        with builtins.open("ImMatchData.json", "r", encoding="UTF-8") as fp:
            ImMatchData = json.load(fp)
        ImMatch.ImInputChkList.SetMode(ImMatchData["Mode"])
        ImMatch.ImInputChkList.SetImInPutList(ImMatchData["FileInfoList"])
        ImMatch.ImInputChkList.SetCheck(ImMatchData["Check"])
        ImMatch.FileInfoList = ImMatchData["FileInfoList"]
        ImMatch.FilePaths = ImMatchData["FilePaths"]
        ImMatch.ManualChkBox.SetValue(ImMatchData["ManualChkVal"])
        ImMatch.AutoChkBox.SetValue(ImMatchData["AutoChkVal"])
        ImMatch.MathSelect.SetSelection(ImMatchData["MathSelect"])
        ImMatch.Show()
        self.Enable(False)

        event.Skip()

    def ImOutput(self, event):
        if Frame.ImInputData["Check"] == [] or Frame.ImMatchData["Check"] == []:
            wx.MessageDialog(self, message="请选择待识别的图像或匹配的图像库！", caption="警告！", style=wx.OK | wx.CENTRE).ShowModal()
            self.ImMatchBtn.Enable(True)
            self.ImOutputBtn.Enable(False)
            self.Enable(True)
        else:
            RunDialog(self).Show()
            self.RunThread = RunThread(self.AllCtrlSum)
            self.RunThread.start()
            self.Enable(False)
        event.Skip()

    def Close(self, event):
        ImInputData = {"FileInfoList": [], "Check": [], "FilePaths": []}
        with builtins.open("ImInputData.json", "w", encoding="UTF-8") as fp:
            json.dump(ImInputData, fp)
        ImProcessData = {"width": 75, "height": 170, "ThreFactor": 4, "ThreGray": 0.3, "Iter": 3, "SideLength": 11, "ThreK": 0.05,
                         "OpenSide": 3, "ClosedSide": 3, "BlurSide": 5, "Minsize": 20}
        with builtins.open("ImProcessData.json", "w", encoding="UTF-8") as fp:
            json.dump(ImProcessData, fp)
        ImMatchData = {"FileInfoList": [], "Check": [], "FilePaths": [], "ManualChkVal": True, "AutoChkVal": False,
                       "Mode": 'single', "MathSelect": 0}
        with builtins.open("ImMatchData.json", "w", encoding="UTF-8") as fp:
            json.dump(ImMatchData, fp)
        phashData = {"hash_size": 8, "highfreq_factor": 4, "THRESHOLD": 0.7}
        with builtins.open("phashData.json", "w", encoding="UTF-8") as fp:
            json.dump(phashData, fp)
        ahashData = {"hash_size": 8, "THRESHOLD": 0.7}
        with builtins.open("ahashData.json", "w", encoding="UTF-8") as fp:
            json.dump(ahashData, fp)
        dhashData = {"hash_size": 8, "THRESHOLD": 0.7}
        with builtins.open("dhashData.json", "w", encoding="UTF-8") as fp:
            json.dump(dhashData, fp)
        whashData = {"hash_size": 0, "image_scale": 0, "mode": 0, "remove_max_haar_ll": 0, "THRESHOLD": 0.7}
        with builtins.open("whashData.json", "w", encoding="UTF-8") as fp:
            json.dump(whashData, fp)
        event.Skip()

    def SetImInputData(self, ImInputData):
        Frame.ImInputData = ImInputData

    def SetImProcessData(self, ImProcessData):
        Frame.ImProcessData = ImProcessData

    def SetImMatchData(self, ImMatchData):
        Frame.ImMatchData = ImMatchData

    def SetphashData(self, phashData):
        Frame.phashData = phashData

    def SetahashData(self, ahashData):
        Frame.ahashData = ahashData

    def SetdhashData(self, dhashData):
        Frame.dhashData = dhashData

    def SetwhashData(self, whashData):
        Frame.whashData = whashData

    # 检查图像输入、图像处理、图像匹配这三步的数据是否有改动
    def SetAllCtrlSum(self, ImProcessSet=0, ImMatchSet=0):
        self.AllCtrlSum = sum([ImProcessSet, ImMatchSet])

    # 运行ImOutputDialog
    @staticmethod
    def RunImOutput(parent):
        ImOutput = ImOutputDialog(parent)
        ImOutput.SetImInfoList(RunThread.OriginName, RunThread.MatchName)
        ImOutput.ImPilList = RunThread.ImPilList
        ImOutput.ImShowList = RunThread.ImShowList
        ImOutput.LeftBtn.Enable(False)
        ImOutput.ImShowArea.SetBitmap(RunThread.ImShowList[0])
        ImOutput.ImInfoText.SetLabel("1、待识别的图像_" + RunThread.OriginName)
        ImOutput.ImMatchNameText.SetLabel(Frame.ImMatchData["FileInfoList"][RunThread.MaxIndex][0])
        ImOutput.SimilarityText.SetLabel(str(RunThread.similarityMax))
        ImOutput.IsMatchText.SetLabel(RunThread.answerList[RunThread.similarityMaxIndex])
        ImOutput.Show()


class RunThread(Thread):
    OriginName = ""
    MatchName = ""
    ImPilList = []
    ImShowList = []
    MaxIndex = 0
    similarityMax = 0
    similarityMaxIndex = 0
    answerList = 0

    def __init__(self, AllCtrlSum):
        Thread.__init__(self)
        self.STOP = 0
        self.AllCtrlSum = AllCtrlSum

    def run(self):
        # 计算进度
        count = 0
        if self.AllCtrlSum != 0:
            countSum = len(Frame.ImMatchData["FilePaths"]) + len(Frame.ImMatchData["Check"])
        else:
            countSum = len(Frame.ImMatchData["Check"])

        FVRT.WIDTH = Frame.ImProcessData["width"]
        FVRT.HEIGHT = Frame.ImProcessData["height"]
        FVRT.THREFACTOR = Frame.ImProcessData["ThreFactor"]
        FVRT.THREGRAY = Frame.ImProcessData["ThreGray"]
        FVRT.ITER = Frame.ImProcessData["Iter"]
        FVRT.SIDELENGTH = floor(Frame.ImProcessData["SideLength"])
        FVRT.THREK = Frame.ImProcessData["ThreK"]
        FVRT.OPENSIDE = floor(Frame.ImProcessData["OpenSide"])
        FVRT.CLOSEDSIDE = floor(Frame.ImProcessData["ClosedSide"])
        FVRT.BLURSIDE = floor(Frame.ImProcessData["BlurSide"])
        FVRT.MINSIZE = Frame.ImProcessData["Minsize"]
        index = Frame.ImInputData["Check"][0]
        ImInputChk = FVRT(Frame.ImInputData["FilePaths"][index])
        OriginName = "原图：“" + Frame.ImInputData["FileInfoList"][index][0] + "”"
        Im_1 = ImInputChk.GetImage()
        ImInputChk.SizeNorm(FVRT.WIDTH, FVRT.HEIGHT)
        Im_2 = ImInputChk.GetImage()
        ImInputChk.GrayNorm()
        Im_3 = ImInputChk.GetImage()
        ImInputChk.DirectValley(FVRT.THREFACTOR)
        Im_4 = ImInputChk.GetImage()
        ImInputChk.BlurEnhance(FVRT.THREGRAY, FVRT.ITER)
        Im_5 = ImInputChk.GetImage()
        ImInputChk.ThreSegment(FVRT.SIDELENGTH, FVRT.THREK)
        Im_6 = ImInputChk.GetImage()
        ImInputChk.Denoise(FVRT.OPENSIDE, FVRT.CLOSEDSIDE, FVRT.BLURSIDE)
        Im_7 = ImInputChk.GetImage()
        ImInputChk.Thin()
        Im_8 = ImInputChk.GetImage()
        ImInputChk.CleanSmallObject(FVRT.MINSIZE)
        Im_9 = ImInputChk.GetImage()
        ImPilList = [Im_1, Im_2, Im_3, Im_4, Im_5, Im_6, Im_7, Im_8, Im_9]
        ImList = []
        for i in ImPilList:
            ImList.append(self.PILtoBitmap(i))
        if self.AllCtrlSum != 0:
            ImDB.DelAll()
            for index in range(len(Frame.ImMatchData["FilePaths"])):
                Im = FVRT.OneKey(Frame.ImMatchData["FilePaths"][index])
                ImDB.AddIm(Frame.ImMatchData["FileInfoList"][index][0], Im)
                time.sleep(0.1)
                count = count + 1
                percent = floor(count / countSum * 100)
                pub.sendMessage("UpdateProgress", percent=percent)
                if self.STOP == 1:
                    return

        # 获取与之匹配的图像和待识别的图像的相似度和匹配值
        similarityList = []
        answerList = []
        indexList = []
        for index in Frame.ImMatchData["Check"]:
            ImageMatch = ImDB.GetIm(id=(index + 1))
            similarity, answer = self.GetMathResult(ImPilList[8], ImageMatch)
            indexList.append(index)
            similarityList.append(similarity)
            answerList.append(answer)
            time.sleep(0.1)
            count = count + 1
            percent = floor(count / countSum * 100)
            pub.sendMessage("UpdateProgress", percent=percent)
            if self.STOP == 1:
                return

        count = 0

        similarityMax = max(similarityList)
        similarityMaxIndex = similarityList.index(similarityMax)
        MaxIndex = indexList[similarityMaxIndex]

        # 从匹配路径获取与之匹配的图像（原图）用以展示
        ImMatchDisplay = FVRT(Frame.ImMatchData["FilePaths"][MaxIndex]).GetImage()
        ImPilList.append(ImMatchDisplay)
        Im_10 = self.PILtoBitmap(ImMatchDisplay)
        ImList.append(Im_10)
        MatchName = "、与之匹配的图像：“" + Frame.ImMatchData["FileInfoList"][MaxIndex][0] + "”"
        ImShowList = []
        for i in range(len(ImList)):
            width, height = ImList[0].Size
            if i == 0 or i == 9:
                ImShowList.append(self.SetBitmapSize(ImList[i], 500 * width / height, 500))
            else:
                ImShowList.append(self.SetBitmapSize(ImList[i], 500 * FVRT.WIDTH / height, 500 * FVRT.HEIGHT / height))
        RunThread.OriginName = OriginName
        RunThread.MatchName = MatchName
        RunThread.ImPilList = ImPilList
        RunThread.ImShowList = ImShowList
        RunThread.MaxIndex = MaxIndex
        RunThread.similarityMax = similarityMax
        RunThread.similarityMaxIndex = similarityMaxIndex
        RunThread.answerList = answerList

    def GetMathResult(self, ImageMatched, ImageMatch):
        MathString = ["感知哈希", "平均散列", "梯度散列", "小波散列"]
        MathSelectString = MathString[Frame.ImMatchData["MathSelect"]]
        similarity = 0
        answer = ""
        MatchObj = ImReg(ImageMatched, ImageMatch)
        if MathSelectString == "感知哈希":
            ImReg.THRESHOLD = Frame.phashData["THRESHOLD"]
            similarity, answer = MatchObj.phash(Frame.phashData["hash_size"], Frame.phashData["highfreq_factor"])
        elif MathSelectString == "平均散列":
            ImReg.THRESHOLD = Frame.ahashData["THRESHOLD"]
            similarity, answer = MatchObj.ahash(Frame.ahashData["hash_size"])
        elif MathSelectString == "梯度散列":
            ImReg.THRESHOLD = Frame.dhashData["THRESHOLD"]
            similarity, answer = MatchObj.dhash(Frame.dhashData["hash_size"])
        elif MathSelectString == "小波散列":
            ImReg.THRESHOLD = Frame.whashData["THRESHOLD"]
            hash_size = [8, 16, 32]
            image_scale = [None, 8, 16]
            mode = ["haar", "db4"]
            remove_max_haar_ll = [True, False]
            similarity, answer = MatchObj.whash(hash_size[Frame.whashData["hash_size"]],
                                                image_scale[Frame.whashData["image_scale"]],
                                                mode[Frame.whashData["mode"]],
                                                remove_max_haar_ll[Frame.whashData["remove_max_haar_ll"]])
        return similarity, answer

    # 将PIL.Image转为wx.Bitmap
    def PILtoBitmap(self, im):
        image = wx.Image(im.size[0], im.size[1])
        image.SetData(im.convert("RGB").tobytes())
        bitmap = image.ConvertToBitmap()
        return bitmap

    # 重新调整wx.Bitmap的尺寸
    def SetBitmapSize(self, bitmap, width, height):
        image = bitmap.ConvertToImage()
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = image.ConvertToBitmap()
        return result


if __name__ == '__main__':
    app = wx.App()
    Frame(None).Show()
    app.MainLoop()
