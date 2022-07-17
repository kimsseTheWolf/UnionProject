import wx
import os
import scripts.globalVar
import GUI.Properties.project_properties_page
import scripts.inputManager
import json
from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()

class PageEvent(GUI.Properties.project_properties_page.project_properties):
    
    def __init__(self, parent):
        GUI.Properties.project_properties_page.project_properties.__init__(self, parent)
        pass
    
    def init_display_data(self, event):
        # gather the datas
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        selected_project = scripts.globalVar.globalVar.get("selected_project")
        if (selected_category == "" or selected_project == ""):
            messagebox.showerror("Error", "You need to select a project first, then continue!")
        else:
            with open("./" + selected_category + "/" + selected_project + "/config.json", "r") as config_json_file:
                project_properties_dict = json.load(config_json_file)
            description_file = open("./" + selected_category + "/" + selected_project + "/description.txt", "r")
            description_file_content = description_file.readlines()
            description_file.close()
            # format the output description content
            output_description_content = scripts.inputManager.outputManager.ListToString(description_file_content)
            
            # set value
            self.display_project_name.SetLabel("Name: " + project_properties_dict["name"])
            self.display_project_create_date.SetLabel("Create Date: " + project_properties_dict["create_date"])
            self.display_belong_category.SetLabel("Belong Category: " + selected_category)
            self.display_project_description.SetValue(output_description_content)
            
    def modify_project(self, event):
        self.Destroy()
        os.system("python .\\modify_project_eventTrigger.py")
        
    def close_dialog(self, event):
        self.Destroy()
        
app = wx.App(False)
page = PageEvent(None)
page.Show(True)
app.MainLoop()
