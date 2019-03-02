# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from pubsub import pub
from FVRT import *
from Frame import *
from zipfile import *
import os
import re
###########################################################################
# Class ImOutputDialog
###########################################################################


class ImOutputDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"图像输出", pos=wx.DefaultPosition, size=wx.Size(800, 800),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.MainPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        gSizer17 = wx.GridSizer(1, 3, 0, 0)

        self.LeftBtn = wx.BitmapButton(self.MainPanel, wx.ID_ANY, wx.Bitmap(u"left.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        gSizer17.Add(self.LeftBtn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT | wx.ALL, 10)

        bSizer51 = wx.BoxSizer(wx.VERTICAL)

        self.ImShowArea = wx.StaticBitmap(self.MainPanel, wx.ID_ANY, wx.NullBitmap,
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer51.Add(self.ImShowArea, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM, 15)

        self.ImInfoText = wx.StaticText(self.MainPanel, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ImInfoText.Wrap(-1)
        bSizer51.Add(self.ImInfoText, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer17.Add(bSizer51, 1, wx.ALIGN_CENTER, 5)

        self.RightBtn = wx.BitmapButton(self.MainPanel, wx.ID_ANY, wx.Bitmap(u"right.bmp", wx.BITMAP_TYPE_ANY),
                                        wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
        gSizer17.Add(self.RightBtn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 10)

        bSizer5.Add(gSizer17, 1, wx.ALL | wx.EXPAND, 10)

        self.m_staticline21 = wx.StaticLine(self.MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        bSizer5.Add(self.m_staticline21, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        SizeNormSizer = wx.StaticBoxSizer(wx.StaticBox(self.MainPanel, wx.ID_ANY, u"匹配信息"), wx.VERTICAL)

        bSizer33 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel25 = wx.Panel(SizeNormSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        bSizer342 = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_1 = wx.Panel(self.m_panel25, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer16 = wx.GridSizer(3, 2, 10, 10)

        self.m_staticText43 = wx.StaticText(self.panel_1, wx.ID_ANY, u"与之匹配的图像：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText43.Wrap(-1)
        gSizer16.Add(self.m_staticText43, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.ImMatchNameText = wx.StaticText(self.panel_1, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ImMatchNameText.Wrap(-1)
        gSizer16.Add(self.ImMatchNameText, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.m_staticText44 = wx.StaticText(self.panel_1, wx.ID_ANY, u"相似度：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText44.Wrap(-1)
        gSizer16.Add(self.m_staticText44, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.SimilarityText = wx.StaticText(self.panel_1, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.SimilarityText.Wrap(-1)
        gSizer16.Add(self.SimilarityText, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.m_staticText46 = wx.StaticText(self.panel_1, wx.ID_ANY, u"是否匹配：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText46.Wrap(-1)
        gSizer16.Add(self.m_staticText46, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.IsMatchText = wx.StaticText(self.panel_1, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.IsMatchText.Wrap(-1)
        gSizer16.Add(self.IsMatchText, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.panel_1.SetSizer(gSizer16)
        self.panel_1.Layout()
        gSizer16.Fit(self.panel_1)
        bSizer342.Add(self.panel_1, 1, wx.ALIGN_CENTER, 5)

        self.m_panel25.SetSizer(bSizer342)
        self.m_panel25.Layout()
        bSizer342.Fit(self.m_panel25)
        bSizer33.Add(self.m_panel25, 1, wx.ALIGN_CENTER, 5)

        SizeNormSizer.Add(bSizer33, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        bSizer5.Add(SizeNormSizer, 0, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        self.m_staticline2 = wx.StaticLine(self.MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer5.Add(self.m_staticline2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        gSizer2 = wx.GridSizer(1, 4, 0, 0)

        self.PreBtn = wx.Button(self.MainPanel, wx.ID_ANY, u"上一步", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.PreBtn, 0, wx.ALIGN_LEFT, 5)

        self.SaveImBtn = wx.Button(self.MainPanel, wx.ID_ANY, u"保存图像", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.SaveImBtn, 0, wx.ALIGN_CENTER, 5)

        self.CancelBtn = wx.Button(self.MainPanel, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.CancelBtn, 0, wx.ALIGN_CENTER, 5)

        self.NextBtn = wx.Button(self.MainPanel, wx.ID_ANY, u"下一步", wx.DefaultPosition, wx.DefaultSize, 0)
        self.NextBtn.Enable(False)

        gSizer2.Add(self.NextBtn, 0, wx.ALIGN_RIGHT, 5)

        bSizer5.Add(gSizer2, 0, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        self.MainPanel.SetSizer(bSizer5)
        self.MainPanel.Layout()
        bSizer5.Fit(self.MainPanel)
        bSizer1.Add(self.MainPanel, 1, wx.EXPAND, 0)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.LeftBtn.Bind(wx.EVT_BUTTON, self.OnLeft)
        self.RightBtn.Bind(wx.EVT_BUTTON, self.OnRight)
        self.PreBtn.Bind(wx.EVT_BUTTON, self.Pre)
        self.SaveImBtn.Bind(wx.EVT_BUTTON, self.Save)
        self.CancelBtn.Bind(wx.EVT_BUTTON, self.Cancel)

        self.ImPilList = []
        self.ImShowList = []
        self.name = "、待识别的图像_"
        self.ImInfoList = []
        self.count = 0
        self.OriginName = 0
        self.MatchName = 0

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnClose(self, event):
        self.Destroy()
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        self.Parent.AllCtrlSum = 0
        event.Skip()

    def OnLeft(self, event):
        self.count = self.count - 1
        if self.count == 9:
            self.ImInfoText.SetLabel(str(self.count + 1) + self.ImInfoList[self.count])
        else:
            self.ImInfoText.SetLabel(str(self.count + 1) + self.name + self.ImInfoList[self.count])
        self.ImShowArea.SetBitmap(self.ImShowList[self.count])
        if self.count == 0:
            self.LeftBtn.Enable(False)
        else:
            self.RightBtn.Enable(True)
        self.Layout()
        self.Refresh()
        event.Skip()

    def OnRight(self, event):
        self.count = self.count + 1
        if self.count == 9:
            self.ImInfoText.SetLabel(str(self.count + 1) + self.ImInfoList[self.count])
        else:
            self.ImInfoText.SetLabel(str(self.count + 1) + self.name + self.ImInfoList[self.count])
        self.ImShowArea.SetBitmap(self.ImShowList[self.count])
        if self.count == (len(self.ImShowList) - 1):
            self.RightBtn.Enable(False)
        else:
            self.LeftBtn.Enable(True)
        self.Layout()
        self.Refresh()
        event.Skip()

    # 设置原图的名称
    def SetImInfoList(self, OriginName, MatchName):
        self.ImInfoList = [OriginName, "尺寸归一化", "灰度归一化", "方向谷型检测", "模糊增强", "阈值分割", "去噪", "细化", "去除残余斑点", MatchName]
        self.OriginName = OriginName
        self.MatchName = MatchName

    def Pre(self, event):
        self.Destroy()
        self.Parent.ImMatchBtn.Enable(True)
        self.Parent.ImOutputBtn.Enable(False)
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        self.Parent.AllCtrlSum = 0
        event.Skip()

    def Save(self, event):
        ImSave = wx.FileDialog(self, message="选择压缩文件保存的位置", wildcard="*.zip", style=wx.FD_SAVE, defaultFile="指静脉图像匹配结果.zip")
        ImSave.SetSize((10, 10))
        if ImSave.ShowModal() == wx.ID_OK:
            DIR = ImSave.GetDirectory()
            ImNameList = []
            for i in range(len(self.ImInfoList)):
                if i == 9:
                    ImNameList.append(str(i + 1) + self.ImInfoList[i] + ".bmp")
                else:
                    ImNameList.append(str(i + 1) + self.name + self.ImInfoList[i] + ".bmp")
            for i in range(len(self.ImInfoList)):
                self.ImPilList[i].convert('L').save(DIR + "\\" + ImNameList[i])
            defaultFileName = ImSave.GetFilename()
            NameMatch = re.search("\.zip", defaultFileName)
            if NameMatch is None:
                defaultFileName = defaultFileName + "\.zip"
            with ZipFile(DIR + "\\" + defaultFileName, 'w', ZIP_DEFLATED) as ImZip:
                for i in range(len(ImNameList)):
                    ImZip.write(DIR + "\\" + ImNameList[i], ImNameList[i])
            for i in range(len(self.ImInfoList)):
                os.remove(DIR + "\\" + ImNameList[i])
        ImSave.Destroy()
        self.Parent.AllCtrlSum = 0
        event.Skip()

    def Cancel(self, event):
        self.Destroy()
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        self.Parent.AllCtrlSum = 0
        event.Skip()
