from tkinter import *
from tkinter import messagebox
import wx
import wx.xrc
import GUI.create_category_page
import sys
import os
import scripts.jsonLibManager
import GUI.Dialog.info_dialog_trigger

create_manager = scripts.jsonLibManager.createManager
dialog = GUI.Dialog.info_dialog_trigger
root = Tk()
root.withdraw()

class PageEvent(GUI.create_category_page.CreateCategoryWindow):
    
    def __init__(self, parent):
        GUI.create_category_page.CreateCategoryWindow.__init__(self, parent)
        pass
    
    def exit_window(self, event):
        self.Close()  
        self.Destroy()
        
    def create_new_category(self, event):
        # check whether it meet the requirement of the form
        category_name = self.input_category_name.GetValue()
        description = self.input_description.GetValue()
        if (category_name == ""):
            messagebox.showinfo("Info", "You need to give a name")
        else:
            result = create_manager.GUIcreateCategory(category_name, description)
            if (result == True):
                messagebox.showinfo("Success", "You create a new category successfully!")
                self.Close()
                self.Destroy()
            else:
                messagebox.showerror("Failed", "Something went wrong while creating a new category.")
            
app = wx.App(False)
page = PageEvent(None)
page.Show(True)
app.MainLoop()