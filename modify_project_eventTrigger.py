import wx
import GUI.modify_project_page
import scripts.globalVar
import scripts.jsonLibManager
from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()

class PageEvent(GUI.modify_project_page.modify_project):
    
    def __init__(self, parent):
        GUI.modify_project_page.modify_project.__init__(self, parent)
        
    def get_value(self, event):
        selected_project = scripts.globalVar.globalVar.get("selected_project")
        self.input_project_name.SetValue(scripts.globalVar.globalVar.get("selected_project"))
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        target_description_file = open("./" + selected_category + "/" + selected_project + "/description.txt", "r")
        description_content = target_description_file.readlines()
        for i in description_content:
            self.input_project_description.SetValue(self.input_project_description.GetValue() + i)
        pass
        
    def modify_project(self, event):
        current_project_name = scripts.globalVar.globalVar.get("selected_project")
        new_project_name = self.input_project_name.GetValue()
        belong_category = scripts.globalVar.globalVar.get("selected_category")
        description = self.input_project_description.GetValue()
        result =  scripts.jsonLibManager.createManager.GUImodifyProject(current_project_name, new_project_name, belong_category, description)
        if (result == True):
            messagebox.showinfo("Info", "You modified this project successfully!")
            self.Destroy()
        else:
            messagebox.showerror("Error", "Something went wrong while modifying the project. Please try again.")
            
    def close_window(self, event):
        self.Destroy()
        
app = wx.App(False)
page = PageEvent(None)
page.Show(True)
app.MainLoop()