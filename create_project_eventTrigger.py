import wx
import GUI.create_project_page
import scripts.jsonLibManager
import json
import os
import scripts.globalVar
from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()

class PageEvent(GUI.create_project_page.create_project):
    
    def __init__(self, parent):
        GUI.create_project_page.create_project.__init__(self, parent)
        
    def close_window(self, event):
        self.Destroy()
        
    def create_project(self, event):
        # check whether it meet the requirement of the form
        belong_category = scripts.globalVar.globalVar.get("selected_category")
        project_name = self.input_project_name.GetValue()
        description = self.input_project_description.GetValue()
        if (project_name == ""):
            messagebox.showinfo("Info", "You need to give a name")
        else:
            result = scripts.jsonLibManager.createManager.GUIcreateProject(project_name, belong_category, description)
            if (result == True):
                messagebox.showinfo("Success", "You create a new project successfully!")
                self.Close()
                self.Destroy()
            else:
                messagebox.showerror("Failed", "Something went wrong while creating a new project.")
        
app = wx.App(False)
page = PageEvent(None)
page.Show(True)
app.MainLoop()