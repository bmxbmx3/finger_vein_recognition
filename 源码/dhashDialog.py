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
import builtins
import json

###########################################################################
# Class dhashDialog
###########################################################################


class dhashDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"梯度散列", pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.MainPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel281 = wx.Panel(self.MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer341 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel291 = wx.Panel(self.m_panel281, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer351 = wx.BoxSizer(wx.HORIZONTAL)

        self.pan = wx.Panel(self.m_panel291, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer40 = wx.BoxSizer(wx.VERTICAL)

        gSizer12 = wx.GridSizer(2, 2, 10, 10)

        self.m_staticText18 = wx.StaticText(self.pan, wx.ID_ANY, u"哈希数值长度：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        gSizer12.Add(self.m_staticText18, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.hash_size = wx.SpinCtrl(self.pan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(80, -1),
                                     wx.SP_ARROW_KEYS, 4, 32, 8)
        gSizer12.Add(self.hash_size, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.m_staticText181 = wx.StaticText(self.pan, wx.ID_ANY, u"相似度阈值：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText181.Wrap(-1)
        gSizer12.Add(self.m_staticText181, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.THRESHOLD = wx.SpinCtrlDouble(self.pan, id=-1, size=wx.Size(80, -1), min=0.01, max=1, initial=0.7,
                                           inc=0.01)
        gSizer12.Add(self.THRESHOLD, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        bSizer40.Add(gSizer12, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.pan.SetSizer(bSizer40)
        self.pan.Layout()
        bSizer40.Fit(self.pan)
        bSizer351.Add(self.pan, 1, wx.ALIGN_CENTER, 5)

        self.m_panel291.SetSizer(bSizer351)
        self.m_panel291.Layout()
        bSizer351.Fit(self.m_panel291)
        bSizer341.Add(self.m_panel291, 1, wx.ALIGN_CENTER, 5)

        self.m_panel281.SetSizer(bSizer341)
        self.m_panel281.Layout()
        bSizer341.Fit(self.m_panel281)
        bSizer5.Add(self.m_panel281, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.m_staticline2 = wx.StaticLine(self.MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer5.Add(self.m_staticline2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 10)

        gSizer2 = wx.GridSizer(1, 2, 0, 0)

        self.OkBtn = wx.Button(self.MainPanel, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.OkBtn, 0, wx.ALIGN_LEFT, 5)

        self.CancelBtn = wx.Button(self.MainPanel, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.CancelBtn, 0, wx.ALIGN_RIGHT, 5)

        bSizer5.Add(gSizer2, 0, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        self.MainPanel.SetSizer(bSizer5)
        self.MainPanel.Layout()
        bSizer5.Fit(self.MainPanel)
        bSizer1.Add(self.MainPanel, 1, wx.EXPAND, 0)

        self.SetSizer(bSizer1)
        self.Layout()
        bSizer1.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.Onclose)
        self.OkBtn.Bind(wx.EVT_BUTTON, self.OnOk)
        self.CancelBtn.Bind(wx.EVT_BUTTON, self.OnCancel)

        self.THRESHOLD.SetDigits(2)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def Onclose(self, event):
        self.Destroy()
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        event.Skip()

    def OnOk(self, event):
        dhashData = {"hash_size": self.hash_size.GetValue(), "THRESHOLD": self.THRESHOLD.GetValue()}
        with builtins.open("dhashData.json", "w", encoding="UTF-8") as fp:
            json.dump(dhashData, fp)
        pub.sendMessage("dhashData", dhashData=dhashData)
        self.Destroy()
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        event.Skip()

    def OnCancel(self, event):
        self.Destroy()
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        event.Skip()
