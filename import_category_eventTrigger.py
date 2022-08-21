import wx
import GUI.Export.import_category_page
import scripts.globalVar
import scripts.inputManager
import scripts.jsonLibManager
import os
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkinter.filedialog import askdirectory
from tkinter import *

root = Tk()
root.withdraw()

class PageEvent(GUI.Export.import_category_page.import_category):
    
    def __init__(self, parent):
        GUI.Export.import_category_page.import_category.__init__(self, parent)
        
    def choose_folder_location(self, event):
        target_src = askdirectory()
        self.input_folder_location.SetValue(target_src)
        
    def import_category(self, event):
        target_src = self.input_folder_location.GetValue()
        result = scripts.jsonLibManager.createManager.GUIimportItem(target_src)
        if (result == True):
            messagebox.showinfo("Success", "Your category imported to Union Project successfully!")
        else:
            messagebox.showerror("Error", "Error while importing your category: You need to change the category\'s name")
            
    def close_window(self, event):
        self.Destroy()
        
app = wx.App(False)
page = PageEvent(None)
page.Show(True)
app.MainLoop()