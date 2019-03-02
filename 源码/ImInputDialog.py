# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from PIL.Image import open as ImOpen
import os
import time
from CheckListCtrl import *
from pubsub import pub
import builtins
import json

###########################################################################
# Class ImImputDialog
###########################################################################


class ImInputDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"图像输入", pos=wx.DefaultPosition, size=wx.Size(590, 500),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.MainPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.SelectImBtn = wx.Button(self.MainPanel, wx.ID_ANY, u"选择待识别的图像", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.SelectImBtn, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.ImInputChkList = CheckListCtrl(self.MainPanel, mode='single')
        bSizer5.Add(self.ImInputChkList, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.m_staticline2 = wx.StaticLine(self.MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer5.Add(self.m_staticline2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 10)

        gSizer2 = wx.GridSizer(1, 3, 0, 0)

        self.PreBtn = wx.Button(self.MainPanel, wx.ID_ANY, u"上一步", wx.DefaultPosition, wx.DefaultSize, 0)
        self.PreBtn.Enable(False)

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
        ImFile = wx.FileDialog(self, message="选择待识别的图像", wildcard="*.bmp;*.jpg;*.png", style=wx.FD_OPEN | wx.FD_MULTIPLE)
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

    def Cancel(self, event):
        self.Destroy()
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        event.Skip()

    def Next(self, event):
        self.Destroy()
        self.Parent.ImInputBtn.Enable(False)
        self.Parent.ImProcessBtn.Enable(True)
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        ImInputData = {"FileInfoList": self.FileInfoList, "Check": list(self.ImInputChkList.GetCheck()), "FilePaths": self.FilePaths}
        with builtins.open("ImInputData.json", "w", encoding="UTF-8") as fp:
            json.dump(ImInputData, fp)
        pub.sendMessage("ImInputData", ImInputData=ImInputData)
        event.Skip()
