import wx
import wx.xrc
from . import info_dialog
import sys
import os

def main():
    app = wx.App(False)
    page = PageEvent(None)
    page.Show(True)
    app.MainLoop()

class PageEvent(info_dialog.InfoDialog):
    
    def __init__(self, parent):
        info_dialog.InfoDialog.__init__(self, parent)
        pass
    
    def display(self, content):
        self.content.SetLabel(content)
        main()
        pass
    
    def exit(self, event):
        self.Close()
        self.Destroy()
    
    
        
    