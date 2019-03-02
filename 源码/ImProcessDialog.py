# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from math import *
import builtins
import json
from pubsub import pub

###########################################################################
# Class ImProcessDialog
###########################################################################


class ImProcessDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"图像处理", pos=wx.DefaultPosition, size=wx.Size(1000, 400),
                           style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.MainPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        gSizer9 = wx.GridSizer(2, 4, 10, 15)

        SizeNormSizer = wx.StaticBoxSizer(wx.StaticBox(self.MainPanel, wx.ID_ANY, u"1、尺寸归一化"), wx.VERTICAL)

        bSizer33 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel25 = wx.Panel(SizeNormSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        bSizer34 = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_1 = wx.Panel(self.m_panel25, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer2 = wx.FlexGridSizer(2, 2, 10, 10)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(self.panel_1, wx.ID_ANY, u"变换后 宽：", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ST_NO_AUTORESIZE)
        self.m_staticText1.Wrap(-1)
        fgSizer2.Add(self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.widthText = wx.SpinCtrl(self.panel_1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(80, -1),
                                     wx.SP_ARROW_KEYS, 10, 2000, 75)
        fgSizer2.Add(self.widthText, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.m_staticText2 = wx.StaticText(self.panel_1, wx.ID_ANY, u"变换后 高：", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ST_NO_AUTORESIZE)
        self.m_staticText2.Wrap(-1)
        fgSizer2.Add(self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.heightText = wx.SpinCtrl(self.panel_1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(80, -1),
                                      wx.SP_ARROW_KEYS, 10, 2000, 170)
        fgSizer2.Add(self.heightText, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.panel_1.SetSizer(fgSizer2)
        self.panel_1.Layout()
        fgSizer2.Fit(self.panel_1)
        bSizer34.Add(self.panel_1, 1, wx.ALIGN_CENTER, 5)

        self.m_panel25.SetSizer(bSizer34)
        self.m_panel25.Layout()
        bSizer34.Fit(self.m_panel25)
        bSizer33.Add(self.m_panel25, 1, wx.ALIGN_CENTER, 5)

        SizeNormSizer.Add(bSizer33, 1, wx.EXPAND, 5)

        gSizer9.Add(SizeNormSizer, 1, wx.EXPAND, 5)

        GrayNormSizer = wx.StaticBoxSizer(wx.StaticBox(self.MainPanel, wx.ID_ANY, u"2、灰度归一化"), wx.VERTICAL)

        bSizer331 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel251 = wx.Panel(GrayNormSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   wx.TAB_TRAVERSAL)
        bSizer341 = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_2 = wx.Panel(self.m_panel251, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer21 = wx.FlexGridSizer(1, 1, 10, 10)
        fgSizer21.SetFlexibleDirection(wx.BOTH)
        fgSizer21.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText11 = wx.StaticText(self.panel_2, wx.ID_ANY, u"参数：无", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ST_NO_AUTORESIZE)
        self.m_staticText11.Wrap(-1)
        fgSizer21.Add(self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.panel_2.SetSizer(fgSizer21)
        self.panel_2.Layout()
        fgSizer21.Fit(self.panel_2)
        bSizer341.Add(self.panel_2, 1, wx.ALIGN_CENTER, 5)

        self.m_panel251.SetSizer(bSizer341)
        self.m_panel251.Layout()
        bSizer341.Fit(self.m_panel251)
        bSizer331.Add(self.m_panel251, 1, wx.ALIGN_CENTER, 5)

        GrayNormSizer.Add(bSizer331, 1, wx.EXPAND, 5)

        gSizer9.Add(GrayNormSizer, 1, wx.EXPAND, 5)

        DirectValleySizer = wx.StaticBoxSizer(wx.StaticBox(self.MainPanel, wx.ID_ANY, u"3、方向谷型检测"), wx.VERTICAL)

        bSizer332 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel252 = wx.Panel(DirectValleySizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   wx.TAB_TRAVERSAL)
        bSizer342 = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_3 = wx.Panel(self.m_panel252, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer22 = wx.FlexGridSizer(1, 2, 10, 10)
        fgSizer22.SetFlexibleDirection(wx.BOTH)
        fgSizer22.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText12 = wx.StaticText(self.panel_3, wx.ID_ANY, u"灰度 放大系数：", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ST_NO_AUTORESIZE)
        self.m_staticText12.Wrap(-1)
        fgSizer22.Add(self.m_staticText12, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.ThreFactorText = wx.SpinCtrlDouble(self.panel_3, id=-1, size=wx.Size(80, -1), min=0.1, max=10, initial=4,
                                                inc=0.1)
        fgSizer22.Add(self.ThreFactorText, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.panel_3.SetSizer(fgSizer22)
        self.panel_3.Layout()
        fgSizer22.Fit(self.panel_3)
        bSizer342.Add(self.panel_3, 1, wx.ALIGN_CENTER, 5)

        self.m_panel252.SetSizer(bSizer342)
        self.m_panel252.Layout()
        bSizer342.Fit(self.m_panel252)
        bSizer332.Add(self.m_panel252, 1, wx.ALIGN_CENTER, 5)

        DirectValleySizer.Add(bSizer332, 1, wx.EXPAND, 5)

        gSizer9.Add(DirectValleySizer, 1, wx.EXPAND, 5)

        BlurEnhanceSizer = wx.StaticBoxSizer(wx.StaticBox(self.MainPanel, wx.ID_ANY, u"4、模糊增强"), wx.VERTICAL)

        bSizer333 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel253 = wx.Panel(BlurEnhanceSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                   wx.TAB_TRAVERSAL)
        bSizer343 = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_4 = wx.Panel(self.m_panel253, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer23 = wx.FlexGridSizer(2, 2, 10, 10)
        fgSizer23.SetFlexibleDirection(wx.BOTH)
        fgSizer23.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText13 = wx.StaticText(self.panel_4, wx.ID_ANY, u"隶属度 分割界限：", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ST_NO_AUTORESIZE)
        self.m_staticText13.Wrap(-1)
        fgSizer23.Add(self.m_staticText13, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.ThreGrayText = wx.SpinCtrlDouble(self.panel_4, id=-1, size=wx.Size(80, -1), min=0.1, max=1, initial=0.3,
                                              inc=0.1)
        fgSizer23.Add(self.ThreGrayText, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.m_staticText21 = wx.StaticText(self.panel_4, wx.ID_ANY, u"迭代次数：", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ST_NO_AUTORESIZE)
        self.m_staticText21.Wrap(-1)
        fgSizer23.Add(self.m_staticText21, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.IterText = wx.SpinCtrl(self.panel_4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(80, -1),
                                    wx.SP_ARROW_KEYS, 1, 10, 3)
        fgSizer23.Add(self.IterText, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.panel_4.SetSizer(fgSizer23)
        self.panel_4.Layout()
        fgSizer23.Fit(self.panel_4)
        bSizer343.Add(self.panel_4, 1, wx.ALIGN_CENTER, 5)

        self.m_panel253.SetSizer(bSizer343)
        self.m_panel253.Layout()
        bSizer343.Fit(self.m_panel253)
        bSizer333.Add(self.m_panel253, 1, wx.ALIGN_CENTER, 5)

        BlurEnhanceSizer.Add(bSizer333, 1, wx.EXPAND, 5)

        gSizer9.Add(BlurEnhanceSizer, 1, wx.EXPAND, 5)

        ThreSegmentSizer = wx.StaticBoxSizer(wx.StaticBox(self.MainPanel, wx.ID_ANY, u"5、阈值分割"), wx.VERTICAL)

        bSizer3331 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel2531 = wx.Panel(ThreSegmentSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        bSizer3431 = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_5 = wx.Panel(self.m_panel2531, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer231 = wx.FlexGridSizer(2, 2, 10, 10)
        fgSizer231.SetFlexibleDirection(wx.BOTH)
        fgSizer231.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText131 = wx.StaticText(self.panel_5, wx.ID_ANY, u"Niblack 模板边长：", wx.DefaultPosition,
                                             wx.DefaultSize, wx.ST_NO_AUTORESIZE)
        self.m_staticText131.Wrap(-1)
        fgSizer231.Add(self.m_staticText131, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.SideLengthText = wx.SpinCtrlDouble(self.panel_5, id=-1, size=wx.Size(80, -1), min=3, max=29, initial=11,
                                                inc=2)
        fgSizer231.Add(self.SideLengthText, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.m_staticText211 = wx.StaticText(self.panel_5, wx.ID_ANY, u"补偿权值：", wx.DefaultPosition, wx.DefaultSize,
                                             wx.ST_NO_AUTORESIZE)
        self.m_staticText211.Wrap(-1)
        fgSizer231.Add(self.m_staticText211, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.ThreKText = wx.SpinCtrlDouble(self.panel_5, id=-1, size=wx.Size(80, -1), min=0.01, max=5, initial=0.05,
                                           inc=0.01)
        fgSizer231.Add(self.ThreKText, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.panel_5.SetSizer(fgSizer231)
        self.panel_5.Layout()
        fgSizer231.Fit(self.panel_5)
        bSizer3431.Add(self.panel_5, 1, wx.ALIGN_CENTER, 5)

        self.m_panel2531.SetSizer(bSizer3431)
        self.m_panel2531.Layout()
        bSizer3431.Fit(self.m_panel2531)
        bSizer3331.Add(self.m_panel2531, 1, wx.ALIGN_CENTER, 5)

        ThreSegmentSizer.Add(bSizer3331, 1, wx.EXPAND, 5)

        gSizer9.Add(ThreSegmentSizer, 1, wx.EXPAND, 5)

        DenoiseSizer = wx.StaticBoxSizer(wx.StaticBox(self.MainPanel, wx.ID_ANY, u"6、去噪"), wx.VERTICAL)

        bSizer33311 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel25311 = wx.Panel(DenoiseSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TAB_TRAVERSAL)
        bSizer34311 = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_6 = wx.Panel(self.m_panel25311, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer2311 = wx.FlexGridSizer(3, 2, 10, 10)
        fgSizer2311.SetFlexibleDirection(wx.BOTH)
        fgSizer2311.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1311 = wx.StaticText(self.panel_6, wx.ID_ANY, u"开运算 模板边长：", wx.DefaultPosition, wx.DefaultSize,
                                              wx.ST_NO_AUTORESIZE)
        self.m_staticText1311.Wrap(-1)
        fgSizer2311.Add(self.m_staticText1311, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.OpenSideText = wx.SpinCtrlDouble(self.panel_6, id=-1, size=wx.Size(80, -1), min=3, max=15, initial=3,
                                              inc=2)
        fgSizer2311.Add(self.OpenSideText, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.m_staticText2111 = wx.StaticText(self.panel_6, wx.ID_ANY, u"闭运算 模板边长：", wx.DefaultPosition, wx.DefaultSize,
                                              wx.ST_NO_AUTORESIZE)
        self.m_staticText2111.Wrap(-1)
        fgSizer2311.Add(self.m_staticText2111, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.ClosedSideText = wx.SpinCtrlDouble(self.panel_6, id=-1, size=wx.Size(80, -1), min=3, max=15, initial=3,
                                                inc=2)
        fgSizer2311.Add(self.ClosedSideText, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.m_staticText21111 = wx.StaticText(self.panel_6, wx.ID_ANY, u"中值滤波 模板边长：", wx.DefaultPosition,
                                               wx.DefaultSize, wx.ST_NO_AUTORESIZE)
        self.m_staticText21111.Wrap(-1)
        fgSizer2311.Add(self.m_staticText21111, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.BlurSideText = wx.SpinCtrlDouble(self.panel_6, id=-1, size=wx.Size(80, -1), min=3, max=15, initial=5,
                                              inc=2)
        fgSizer2311.Add(self.BlurSideText, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.panel_6.SetSizer(fgSizer2311)
        self.panel_6.Layout()
        fgSizer2311.Fit(self.panel_6)
        bSizer34311.Add(self.panel_6, 1, wx.ALIGN_CENTER, 5)

        self.m_panel25311.SetSizer(bSizer34311)
        self.m_panel25311.Layout()
        bSizer34311.Fit(self.m_panel25311)
        bSizer33311.Add(self.m_panel25311, 1, wx.ALIGN_CENTER, 5)

        DenoiseSizer.Add(bSizer33311, 1, wx.EXPAND, 5)

        gSizer9.Add(DenoiseSizer, 1, wx.EXPAND, 5)

        ThinSizer = wx.StaticBoxSizer(wx.StaticBox(self.MainPanel, wx.ID_ANY, u"7、细化"), wx.VERTICAL)

        bSizer3311 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel2511 = wx.Panel(ThinSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        bSizer3411 = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_21 = wx.Panel(self.m_panel2511, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer211 = wx.FlexGridSizer(1, 1, 10, 10)
        fgSizer211.SetFlexibleDirection(wx.BOTH)
        fgSizer211.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText111 = wx.StaticText(self.panel_21, wx.ID_ANY, u"参数：无", wx.DefaultPosition, wx.DefaultSize,
                                             wx.ST_NO_AUTORESIZE)
        self.m_staticText111.Wrap(-1)
        fgSizer211.Add(self.m_staticText111, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.panel_21.SetSizer(fgSizer211)
        self.panel_21.Layout()
        fgSizer211.Fit(self.panel_21)
        bSizer3411.Add(self.panel_21, 1, wx.ALIGN_CENTER, 5)

        self.m_panel2511.SetSizer(bSizer3411)
        self.m_panel2511.Layout()
        bSizer3411.Fit(self.m_panel2511)
        bSizer3311.Add(self.m_panel2511, 1, wx.ALIGN_CENTER, 5)

        ThinSizer.Add(bSizer3311, 1, wx.EXPAND, 5)

        gSizer9.Add(ThinSizer, 1, wx.EXPAND, 5)

        CleanSmallObjectSizer = wx.StaticBoxSizer(wx.StaticBox(self.MainPanel, wx.ID_ANY, u"8、去除残余斑点"), wx.VERTICAL)

        bSizer3321 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel2521 = wx.Panel(CleanSmallObjectSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        bSizer3421 = wx.BoxSizer(wx.HORIZONTAL)

        self.panel_6 = wx.Panel(self.m_panel2521, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer221 = wx.FlexGridSizer(1, 2, 10, 10)
        fgSizer221.SetFlexibleDirection(wx.BOTH)
        fgSizer221.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText121 = wx.StaticText(self.panel_6, wx.ID_ANY, u"圈定面积：", wx.DefaultPosition, wx.DefaultSize,
                                             wx.ST_NO_AUTORESIZE)
        self.m_staticText121.Wrap(-1)
        fgSizer221.Add(self.m_staticText121, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.MinSizeText = wx.SpinCtrl(self.panel_6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(80, -1),
                                       wx.SP_ARROW_KEYS, 10, 10000, 20)
        fgSizer221.Add(self.MinSizeText, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, 5)

        self.panel_6.SetSizer(fgSizer221)
        self.panel_6.Layout()
        fgSizer221.Fit(self.panel_6)
        bSizer3421.Add(self.panel_6, 1, wx.ALIGN_CENTER, 5)

        self.m_panel2521.SetSizer(bSizer3421)
        self.m_panel2521.Layout()
        bSizer3421.Fit(self.m_panel2521)
        bSizer3321.Add(self.m_panel2521, 1, wx.ALIGN_CENTER, 5)

        CleanSmallObjectSizer.Add(bSizer3321, 1, wx.EXPAND, 5)

        gSizer9.Add(CleanSmallObjectSizer, 1, wx.EXPAND, 5)

        bSizer5.Add(gSizer9, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.m_staticline2 = wx.StaticLine(self.MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer5.Add(self.m_staticline2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 10)

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
        self.PreBtn.Bind(wx.EVT_BUTTON, self.Pre)
        self.CancelBtn.Bind(wx.EVT_BUTTON, self.Cancel)
        self.NextBtn.Bind(wx.EVT_BUTTON, self.Next)
        self.widthText.Bind(wx.EVT_SPINCTRL, self.widthChg)
        self.heightText.Bind(wx.EVT_SPINCTRL, self.heightChg)
        self.ThreFactorText.Bind(wx.EVT_SPINCTRLDOUBLE, self.ThreFactorChg)
        self.ThreGrayText.Bind(wx.EVT_SPINCTRLDOUBLE, self.ThreGrayChg)
        self.IterText.Bind(wx.EVT_SPINCTRL, self.IterChg)
        self.SideLengthText.Bind(wx.EVT_SPINCTRLDOUBLE, self.SideLengthChg)
        self.ThreKText.Bind(wx.EVT_SPINCTRLDOUBLE, self.ThreKChg)
        self.OpenSideText.Bind(wx.EVT_SPINCTRLDOUBLE, self.OpenSideChg)
        self.ClosedSideText.Bind(wx.EVT_SPINCTRLDOUBLE, self.ClosedSideChg)
        self.BlurSideText.Bind(wx.EVT_SPINCTRLDOUBLE, self.BlurSideChg)
        self.MinSizeText.Bind(wx.EVT_SPINCTRL, self.MinSizeChg)

        self.ThreFactorText.SetDigits(1)
        self.ThreGrayText.SetDigits(1)
        self.ThreKText.SetDigits(2)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnClose(self, event):
        self.Destroy()
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        event.Skip()

    def Pre(self, event):
        self.Destroy()
        self.Parent.ImInputBtn.Enable(True)
        self.Parent.ImProcessBtn.Enable(False)
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
        self.Parent.ImProcessBtn.Enable(False)
        self.Parent.ImMatchBtn.Enable(True)
        self.Parent.Enable(True)
        self.Parent.SetFocus()
        ImProcessData = {"width": self.widthText.GetValue(), "height": self.heightText.GetValue(), "ThreFactor": self.ThreFactorText.GetValue(),
                         "ThreGray": self.ThreGrayText.GetValue(), "Iter": self.IterText.GetValue(), "SideLength": self.SideLengthText.GetValue(),
                         "ThreK": self.ThreKText.GetValue(), "OpenSide": self.OpenSideText.GetValue(), "ClosedSide": self.ClosedSideText.GetValue(),
                         "BlurSide": self.BlurSideText.GetValue(), "Minsize": self.MinSizeText.GetValue()}
        with builtins.open("ImProcessData.json", "w", encoding="UTF-8") as fp:
            json.dump(ImProcessData, fp)
        pub.sendMessage("ImProcessData", ImProcessData=ImProcessData)
        event.Skip()

    def widthChg(self, event):
        pub.sendMessage("AllCtrlSum", ImProcessSet=1)

    def heightChg(self, event):
        pub.sendMessage("AllCtrlSum", ImProcessSet=1)

    def ThreFactorChg(self, event):
        pub.sendMessage("AllCtrlSum", ImProcessSet=1)

    def ThreGrayChg(self, event):
        pub.sendMessage("AllCtrlSum", ImProcessSet=1)

    def IterChg(self, event):
        pub.sendMessage("AllCtrlSum", ImProcessSet=1)

    def SideLengthChg(self, event):
        pub.sendMessage("AllCtrlSum", ImProcessSet=1)
        val = self.SideLengthText.GetValue()
        val = floor(val)
        if val % 2 == 0:
            val = val - 1
        self.SideLengthText.SetValue(val)

    def ThreKChg(self, event):
        pub.sendMessage("AllCtrlSum", ImProcessSet=1)

    def OpenSideChg(self, event):
        pub.sendMessage("AllCtrlSum", ImProcessSet=1)
        val = self.OpenSideText.GetValue()
        val = floor(val)
        if val % 2 == 0:
            val = val - 1
        self.OpenSideText.SetValue(val)

    def ClosedSideChg(self, event):
        pub.sendMessage("AllCtrlSum", ImProcessSet=1)
        val = self.ClosedSideText.GetValue()
        val = floor(val)
        if val % 2 == 0:
            val = val - 1
        self.ClosedSideText.SetValue(val)

    def BlurSideChg(self, event):
        pub.sendMessage("AllCtrlSum", ImProcessSet=1)
        val = self.BlurSideText.GetValue()
        val = floor(val)
        if val % 2 == 0:
            val = val - 1
        self.BlurSideText.SetValue(val)

    def MinSizeChg(self, event):
        pub.sendMessage("AllCtrlSum", ImProcessSet=1)
