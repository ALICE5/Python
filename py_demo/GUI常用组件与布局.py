import wx
class Frame1(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,parent = superior, title = 'Hello world in wxPython')
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text1 = wx.TextCtrl(panel,value='Hello,world!',size=(200,180),style=wx.TE_MULTILINE)
        sizer.Add(self.text1,0,wx.ALIGN_TOP|wx.EXPAND)
        button = wx.Button(panel,label='Click Me')
        sizer.Add(button)
        panel.SetSizerAndFit(sizer)
        panel.Layout()
        self.Bind(wx.EVT_BUTTON,self.OnClick,button)
    def OnClick(self,text):
        self.text1.AppendText('\nHello,world!')

if __name__ == '__main__':
    app = wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop()

# 使用sizer的步骤：
# 1- 创建自动调用尺寸的容器
# 2- 创建sizer
# 3- 创建子窗口
# 4- 使用sizer的Add()方法将每个子窗口添加给sizer
# 5- 调用容器的SetSizer(sizer)方法