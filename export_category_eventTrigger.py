import wx
import GUI.Export.export_category_page
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

class PageEvent(GUI.Export.export_category_page.export_category):
    
    def __init__(self, parent):
        GUI.Export.export_category_page.export_category.__init__(self, parent)
        
    def init_data(self, event):
        # gather essential data
        category_list = scripts.inputManager.outputManager.listFileContentFormatOutput("./categoryList.list", "category")
        category_list.append("All Categories")
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        # apply the essential data
        self.btn_category_choices_list.SetItems(category_list)
        
    def close_window(self, event):
        self.Destroy()
        
    def open_file_picker(self, event):
        target_dst = askdirectory()
        self.input_export_dst_display.SetValue(target_dst)
        
    def export_category(self, event):
        target_category = self.btn_category_choices_list.GetValue()
        dst = self.input_export_dst_display.GetValue()
        if (target_category == "All Categories"):
            pass
        else:
            target_category_location = "./" + target_category
            result = scripts.jsonLibManager.createManager.GUIexportItem(target_category_location, dst, target_category)
            if (result == True):
                messagebox.showinfo("Success!", "Your categories exported successfully!")
                self.Destroy()
            else:
                messagebox.showerror("Failed", "An error occured while exporting your category. You category in-app will still useable. Please try again later.")
        
        
app = wx.App(False)
page = PageEvent(None)
page.Show(True)
app.MainLoop()