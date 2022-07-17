import GUI.Others.about_page
import wx

class PageEvent (GUI.Others.about_page.about_window):
    
    def __init__(self, parent):
        GUI.Others.about_page.about_window.__init__(self, parent)
        
    def close(self, event):
        self.Destroy()
        
app = wx.App(False)
page = PageEvent(None)
page.Show(True)
app.MainLoop()