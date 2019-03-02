# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from CheckListCtrl import *
from phashDialog import *
from ahashDialog import *
from dhashDialog import *
from whashDialog import *
from FVRT import *
from PIL.Image import open as ImOpen
import os
import time
from pubsub import pub
import builtins
import json

###########################################################################
# Class ImMatchDialog
###########################################################################


class ImMatchDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"图像匹配", pos=wx.DefaultPosition, size=wx.Size(581, 714),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.MainPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.SelectImBtn = wx.Button(self.MainPanel, wx.ID_ANY, u"选择匹配的图像库", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.SelectImBtn, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        sbSizer21 = wx.StaticBoxSizer(wx.StaticBox(self.MainPanel, wx.ID_ANY, u"匹配模式"), wx.VERTICAL)

        gSizer21 = wx.GridSizer(1, 2, 0, 10)

        self.ManualChkBox = wx.CheckBox(sbSizer21.GetStaticBox(), wx.ID_ANY, u"手动模式", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.ManualChkBox.SetValue(True)
        gSizer21.Add(self.ManualChkBox, 0, wx.ALIGN_CENTER, 10)

        self.AutoChkBox = wx.CheckBox(sbSizer21.GetStaticBox(), wx.ID_ANY, u"自动模式", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        gSizer21.Add(self.AutoChkBox, 0, wx.ALIGN_CENTER, 10)

        sbSizer21.Add(gSizer21, 0, wx.ALL | wx.EXPAND, 10)

        bSizer5.Add(sbSizer21, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.ImInputChkList = CheckListCtrl(self.MainPanel, mode='single')
        bSizer5.Add(self.ImInputChkList, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.m_staticline2 = wx.StaticLine(self.MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer5.Add(self.m_staticline2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 10)

        sbSizer22 = wx.StaticBoxSizer(wx.StaticBox(self.MainPanel, wx.ID_ANY, u"匹配算法"), wx.VERTICAL)

        gSizer9 = wx.GridSizer(1, 3, 0, 10)

        self.m_staticText16 = wx.StaticText(sbSizer22.GetStaticBox(), wx.ID_ANY, u"选择匹配算法：", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        gSizer9.Add(self.m_staticText16, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        MathSelectChoices = [u"感知哈希", u"平均散列", u"梯度散列", u"小波散列"]
        self.MathSelect = wx.Choice(sbSizer22.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(160, -1),
                                    MathSelectChoices, 0)
        self.MathSelect.SetSelection(0)
        gSizer9.Add(self.MathSelect, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.MathOkBtn = wx.Button(sbSizer22.GetStaticBox(), wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer9.Add(self.MathOkBtn, 0, wx.ALIGN_CENTER, 5)

        sbSizer22.Add(gSizer9, 1, wx.ALL, 15)

        bSizer5.Add(sbSizer22, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        gSizer2 = wx.GridSizer(1, 3, 0, 0)

        self.PreBtn = wx.Button(self.MainPanel, wx.ID_ANY, u"上一步", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.PreBtn, 0, wx.ALIGN_LEFT, 5)

        self.CancelBtn = wx.Button(self.MainPanel, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.CancelBtn, 0, wx.ALIGN_CENTER, 5)

        self.NextBtn = wx.Button(self.MainPanel, wx.ID_ANY, u"下一步", wx.DefaultPosition, wx.DefaultSize, 0)
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
        self.SelectImBtn.Bind(wx.EVT_BUTTON, self.SelectIm)
        self.ManualChkBox.Bind(wx.EVT_CHECKBOX, self.OnManualChk)
        self.AutoChkBox.Bind(wx.EVT_CHECKBOX, self.OnAutoChk)
        self.MathOkBtn.Bind(wx.EVT_BUTTON, self.OnOk)
        self.PreBtn.Bind(wx.EVT_BUTTON, self.Pre)
        self.CancelBtn.Bind(wx.EVT_BUTTON, self.Cancel)
        self.NextBtn.Bind(wx.EVT_BUTTON, self.Next)

        self.FilePaths = []
        self.FileInfoList = []

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnClose(self, event):
        self.Destroy()
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        event.Skip()

    def SelectIm(self, event):
        pub.sendMessage("AllCtrlSum", ImMatchSet=1)
        ImFile = wx.FileDialog(self, message="选择待识别的图像", wildcard="*.bmp;*.jpg;*.png",
                               style=wx.FD_OPEN | wx.FD_MULTIPLE)
        ImFile.SetSize((10, 10))
        if ImFile.ShowModal() == wx.ID_OK:
            FileNames = ImFile.GetFilenames()
            FilePaths = ImFile.GetPaths()
            self.FilePaths = FilePaths
            FileInfoList = []
            for index in range(len(FilePaths)):
                mtime = os.path.getmtime(FilePaths[index])
                mtime = time.localtime(mtime)
                mtime = ("%d年%d月%d日 %d时%d分%d秒" % (mtime[0], mtime[1], mtime[2], mtime[3], mtime[4], mtime[5]))
                im = ImOpen(FilePaths[index])
                im_size = str(im.size[0]) + '×' + str(im.size[1])
                FileInfo = [FileNames[index], im_size, mtime]
                FileInfoList.append(FileInfo)
            self.ImInputChkList.SetImInPutList(FileInfoList)
            self.ImInputChkList.SetCheck([0])
            self.FileInfoList = FileInfoList
        ImFile.Destroy()
        event.Skip()

    def OnManualChk(self, event):
        val = self.ManualChkBox.GetValue()
        if val == True:
            self.AutoChkBox.SetValue(False)
            self.ImInputChkList.SetMode('single')
            for i in range(self.ImInputChkList.GetItemCount()):
                if self.ImInputChkList.IsChecked(i):
                    self.ImInputChkList.CheckItem(i, False)
            self.ImInputChkList.CheckItem(0, True)
        else:
            self.AutoChkBox.SetValue(True)
            self.ImInputChkList.SetMode('')
        event.Skip()

    def OnAutoChk(self, event):
        val = self.AutoChkBox.GetValue()
        if val == True:
            self.ManualChkBox.SetValue(False)
            self.ImInputChkList.SetMode('')
        else:
            self.ManualChkBox.SetValue(True)
            self.ImInputChkList.SetMode('single')
            for i in range(self.ImInputChkList.GetItemCount()):
                if self.ImInputChkList.IsChecked(i):
                    self.ImInputChkList.CheckItem(i, False)
            self.ImInputChkList.CheckItem(0, True)
        event.Skip()

    def OnOk(self, event):
        select = self.MathSelect.GetSelection()
        MathString = self.MathSelect.GetString(select)
        if MathString == "感知哈希":
            phash = phashDialog(self)
            with builtins.open("phashData.json", "r", encoding="UTF-8") as fp:
                phashData = json.load(fp)
            phash.hash_size.SetValue(phashData["hash_size"])
            phash.highfreq_factor.SetValue(phashData["highfreq_factor"])
            phash.THRESHOLD.SetValue(phashData["THRESHOLD"])
            phash.Show()
            self.Enable(False)
        elif MathString == "平均散列":
            ahash = ahashDialog(self)
            with builtins.open("ahashData.json", "r", encoding="UTF-8") as fp:
                ahashData = json.load(fp)
            ahash.hash_size.SetValue(ahashData["hash_size"])
            ahash.THRESHOLD.SetValue(ahashData["THRESHOLD"])
            ahash.Show()
            self.Enable(False)
        elif MathString == "梯度散列":
            dhash = dhashDialog(self)
            with builtins.open("dhashData.json", "r", encoding="UTF-8") as fp:
                dhashData = json.load(fp)
            dhash.hash_size.SetValue(dhashData["hash_size"])
            dhash.THRESHOLD.SetValue(dhashData["THRESHOLD"])
            dhash.Show()
            self.Enable(False)
        elif MathString == "小波散列":
            whash = whashDialog(self)
            with builtins.open("whashData.json", "r", encoding="UTF-8") as fp:
                whashData = json.load(fp)
            whash.hash_size.SetSelection(whashData["hash_size"])
            whash.image_scale.SetSelection(whashData["image_scale"])
            whash.mode.SetSelection(whashData["mode"])
            whash.remove_max_haar_ll.SetSelection(whashData["remove_max_haar_ll"])
            whash.THRESHOLD.SetValue(whashData["THRESHOLD"])
            whash.Show()
            self.Enable(False)
        event.Skip()

    def Pre(self, event):
        self.Destroy()
        self.Parent.ImProcessBtn.Enable(True)
        self.Parent.ImMatchBtn.Enable(False)
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        event.Skip()

    def Cancel(self, event):
        self.Destroy()
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        event.Skip()

    def Next(self, event):
        self.Destroy()
        self.Parent.ImMatchBtn.Enable(False)
        self.Parent.ImOutputBtn.Enable(True)
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        ImMatchData = {"FileInfoList": self.FileInfoList, "Check": list(self.ImInputChkList.GetCheck()), "FilePaths": self.FilePaths,
                       "ManualChkVal": self.ManualChkBox.GetValue(), "AutoChkVal": self.AutoChkBox.GetValue(),
                       "Mode": self.ImInputChkList.GetMode(), "MathSelect": self.MathSelect.GetSelection()}
        with builtins.open("ImMatchData.json", "w", encoding="UTF-8") as fp:
            json.dump(ImMatchData, fp)
        pub.sendMessage("ImMatchData", ImMatchData=ImMatchData)
        event.Skip()
