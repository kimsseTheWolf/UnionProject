from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
import wx
import wx.xrc
import GUI.Properties.category_properties_page
import sys
import os
import scripts.globalVar
import scripts.jsonLibManager
import scripts.inputManager
import json

root = Tk()
root.withdraw()

class PageEvent(GUI.Properties.category_properties_page.category_properties):
    
    def __init__(self, parent):
        GUI.Properties.category_properties_page.category_properties.__init__(self, parent)
        pass
    
    def init_display_data(self, event):
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        if (selected_category == False):
            messagebox.showerror("Error", "You need to select a category first, then continue!")
        else:
            # open the properties file and description file
            with open("./" + selected_category + "/config.json", "r") as config_json_file:
                category_properties_dict = json.load(config_json_file)
            description_file = open("./" + selected_category + "/description.txt", "r")
            description_file_content = description_file.readlines()
            description_file.close()
            # format the output description content
            output_description_content = scripts.inputManager.outputManager.ListToString(description_file_content)
            
            # set value
            self.display_category_name.SetLabel("Name:" + category_properties_dict["name"])
            self.display_category_create_date.SetLabel("Create Date:" + category_properties_dict["create_date"])
            self.display_category_description.SetValue(output_description_content)
            
    def modify_category(self, event):
        self.Destroy()
        os.system("python .\\modify_category_eventTrigger.py")
    
    def close_dialog(self, event):
        # scripts.globalVar.globalVar.delete("selected_category")
        self.Destroy()
        
app = wx.App(False)
page = PageEvent(None)
page.Show(True)
app.MainLoop()
