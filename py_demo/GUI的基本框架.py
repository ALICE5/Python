#  wxPython 对于所有需要的UI组件的支持 执行快速 还支持跨平台运行
import wx
# app = wx.App()
# frame = wx.Frame(None,title='Hello, World!')
# frame.Show(True)
# app.MainLoop()

# class MyApp(wx.App):
#     def OnInit(self):
#         frame = wx.Frame(None,title='Hello, World!')
#         frame.Show()
#         return True


"""
mouse event handling  

"""

class Frame1(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,parent=superior,title='Example',pos=(100,200),size=(350,200))
        self.panel = wx.Panel(self)
        # text1 = wx.TextCtrl(self.panel,value='Hello,World!',size=(350,200))
        self.panel.Bind(wx.EVT_LEFT_UP,self.OnClick)

    def OnClick(self,event):
        posm = event.GetPosition()
        wx.StaticText(parent=self.panel,label='Hello,Alice!',pos=(posm.x,posm.y))

if __name__ == '__main__':
    app = wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop()

# 组件：组件容器、动态组件、静态组件、其它组件
# Frame > Panel > Text Control

# 事件处理机制
# 若出错 则在Shell中输入del app