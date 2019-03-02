# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import time
from threading import Thread
from pubsub import pub
from FVRT import *
###########################################################################
# Class RunDialog
###########################################################################


class RunDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"运行进度", pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer51 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel42 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer52 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel45 = wx.Panel(self.m_panel42, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer54 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel46 = wx.Panel(self.m_panel45, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer55 = wx.BoxSizer(wx.VERTICAL)

        fgSizer11 = wx.FlexGridSizer(0, 4, 0, 20)
        fgSizer11.SetFlexibleDirection(wx.BOTH)
        fgSizer11.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.RunGauge = wx.Gauge(self.m_panel46, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size(-1, -1), wx.GA_HORIZONTAL)
        self.RunGauge.SetValue(0)
        fgSizer11.Add(self.RunGauge, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer13 = wx.FlexGridSizer(0, 3, 0, 8)
        fgSizer13.SetFlexibleDirection(wx.BOTH)
        fgSizer13.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText43 = wx.StaticText(self.m_panel46, wx.ID_ANY, u"已完成：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText43.Wrap(-1)
        fgSizer13.Add(self.m_staticText43, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.PercentText = wx.StaticText(self.m_panel46, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size(20, -1), wx.ALIGN_RIGHT)
        self.PercentText.Wrap(-1)
        fgSizer13.Add(self.PercentText, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.m_staticText45 = wx.StaticText(self.m_panel46, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText45.Wrap(-1)
        fgSizer13.Add(self.m_staticText45, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        fgSizer11.Add(fgSizer13, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.FinishBtn = wx.Button(self.m_panel46, wx.ID_ANY, u"完成", wx.DefaultPosition, wx.DefaultSize, 0)
        self.FinishBtn.Enable(False)

        fgSizer11.Add(self.FinishBtn, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        self.CancelBtn = wx.Button(self.m_panel46, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer11.Add(self.CancelBtn, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer55.Add(fgSizer11, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 20)

        self.m_panel46.SetSizer(bSizer55)
        self.m_panel46.Layout()
        bSizer55.Fit(self.m_panel46)
        bSizer54.Add(self.m_panel46, 1, wx.ALIGN_CENTER, 5)

        self.m_panel45.SetSizer(bSizer54)
        self.m_panel45.Layout()
        bSizer54.Fit(self.m_panel45)
        bSizer52.Add(self.m_panel45, 1, wx.ALIGN_CENTER, 5)

        self.m_panel42.SetSizer(bSizer52)
        self.m_panel42.Layout()
        bSizer52.Fit(self.m_panel42)
        bSizer51.Add(self.m_panel42, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer51)
        self.Layout()
        bSizer51.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.FinishBtn.Bind(wx.EVT_BUTTON, self.OnFinish)
        self.CancelBtn.Bind(wx.EVT_BUTTON, self.OnCancel)

        pub.subscribe(self.UpdateProgress, "UpdateProgress")

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnClose(self, event):
        self.Parent.RunThread.STOP = 1
        ImDB.DelAll()
        self.Destroy()
        self.Parent.ImMatchBtn.Enable(True)
        self.Parent.ImOutputBtn.Enable(False)
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        event.Skip()

    def OnFinish(self, event):
        self.Destroy()
        self.Parent.RunImOutput(self.Parent)
        self.Parent.Enable(False)
        event.Skip()

    def OnCancel(self, event):
        self.Parent.RunThread.STOP = 1
        ImDB.DelAll()
        self.Destroy()
        self.Parent.ImMatchBtn.Enable(True)
        self.Parent.ImOutputBtn.Enable(False)
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        event.Skip()

    def UpdateProgress(self, percent):
        self.RunGauge.SetValue(percent)
        self.PercentText.SetLabel(str(percent))
        if percent == 100:
            self.FinishBtn.Enable(True)


class TestThread(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.start()

    def run(self):
        for i in range(101):
            time.sleep(0.1)
            pub.sendMessage("UpdateProgress", percent=i)


if __name__ == '__main__':
    app = wx.App()
    RunDialog(None).Show()
    TestThread()
    app.MainLoop()
