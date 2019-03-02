import wx
from wx.lib.mixins.listctrl import CheckListCtrlMixin


class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin):
    Select=0

    def __init__(self, parent,mode=''):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        CheckListCtrlMixin.__init__(self)

        self.__mode=mode

        self.InsertColumn(0, "名称")
        self.InsertColumn(1, "尺寸")
        self.InsertColumn(2, "最后修改时间")

        self.SetColumnWidth(0, 250)
        self.SetColumnWidth(1, 100)
        self.SetColumnWidth(2, 200)

    #勾选项目的动作激活此方法
    def OnCheckItem(self, index, flag):
        if self.__mode=="single":
            if flag==True:
                CheckIndex=set([index])
                CheckAll = set()
                for i in range(self.GetItemCount()):
                    CheckAll.add(i)
                UnCheck=CheckAll-CheckIndex
                for i in UnCheck:
                    self.CheckItem(i,False)



    # 设置输入图像
    def SetImInPutList(self, ImList):
        self.DeleteAllItems()
        for data in ImList:
            index = self.InsertItem(self.GetItemCount(), data[0])
            self.SetItem(index, 1, data[1])
            self.SetItem(index, 2, data[2])

    #获取勾选的图像位置
    def GetCheck(self):
        CheckList=set()
        for i in range(self.GetItemCount()):
            if self.IsChecked(i):
                CheckList.add(i)
        return CheckList

    #设置单选/多选模式
    def SetMode(self,mode):
        self.__mode=mode

    #获取单选/多选模式
    def GetMode(self):
        return self.__mode

    #设置勾选的图像位置
    def SetCheck(self,CheckIndex):
        for i in CheckIndex:
            self.CheckItem(i, True)