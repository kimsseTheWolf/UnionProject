import wx
import json
import scripts.globalVar
import GUI.project_list_page
import scripts.inputManager
import os
import scripts.jsonLibManager
from tkinter import *
from tkinter.messagebox import askyesno
from tkinter import messagebox

root = Tk()
root.withdraw()

class PageEvent(GUI.project_list_page.projectList):
    
    def __init__(self, parent):
        GUI.project_list_page.projectList.__init__(self, parent)
        
    def init_data(self, event):
        # get the target category and read the contents inside
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        # get the json file data
        with open("./" + selected_category + "/config.json", "r") as selected_category_json:
            selected_category_info = json.load(selected_category_json)
        # get the description file
        category_description_file = open("./" + selected_category + "/description.txt", "r")
        category_description_list = category_description_file.readlines()
        category_description_file.close()
        category_description = scripts.inputManager.outputManager.ListToString(category_description_list)
        # set the properties data
        self.text_name.SetLabel("Name: " + selected_category)
        self.text_create_date.SetLabel("Create Date: " + selected_category_info["create_date"])
        self.text_description.SetLabel(category_description)
        # read and set the values of project list
        self.list_display_project_list.Clear()
        project_list_file = open("./" + selected_category + "/projectList.list", "r")
        project_list_elements = project_list_file.readlines()
        format_project_list = scripts.inputManager.outputManager.listFileContentFormatOutput("./" + selected_category + "/projectList.list", "project")
        for i in format_project_list:
            self.list_display_project_list.Append(i)
            
    def refresh_list(self, event):
        # get the target category and read the contents inside
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        # get the json file data
        with open("./" + selected_category + "/config.json", "r") as selected_category_json:
            selected_category_info = json.load(selected_category_json)
        # get the description file
        category_description_file = open("./" + selected_category + "/description.txt", "r")
        category_description_list = category_description_file.readlines()
        category_description_file.close()
        category_description = scripts.inputManager.outputManager.ListToString(category_description_list)
        # set the properties data
        self.text_name.SetLabel("Name: " + selected_category)
        self.text_create_date.SetLabel("Create Date: " + selected_category_info["create_date"])
        self.text_description.SetLabel(category_description)
        # read and set the values of project list
        self.list_display_project_list.Clear()
        project_list_file = open("./" + selected_category + "/projectList.list", "r")
        project_list_elements = project_list_file.readlines()
        format_project_list = scripts.inputManager.outputManager.listFileContentFormatOutput("./" + selected_category + "/projectList.list", "project")
        for i in format_project_list:
            self.list_display_project_list.Append(i)
        
    def return_category_list(self, event):
        self.Close()
        self.Destroy()
        os.system("python .\\category_list_eventTrigger.py")
        
    def check_category_properties(self, event):
        os.system("python .\\category_properties_eventTrigger.py")
        
    def create_project(self, event):
        os.system("python .\\create_project_eventTrigger.py")
        
    def delete_project(self, event):
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        target_project_location = self.list_display_project_list.GetSelection()
        project_list_item =  scripts.inputManager.outputManager.listFileContentFormatOutput("./" + selected_category + "/projectList.list", "project")
        target_project_name = project_list_item[target_project_location]
        answer = askyesno("Warning", "This will delete everything contain in this category. Are you sure you want to delete it?")
        if (answer == True):
            scripts.jsonLibManager.createManager.GUIdeleteProject(target_project_name, selected_category)
        else:
            messagebox.showinfo("Progress cancled!", "You cancled the delete progress.")
        self.refresh_list(None)
        
    def modify_project(self, event):
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        target_project_location = self.list_display_project_list.GetSelection()
        project_list_item =  scripts.inputManager.outputManager.listFileContentFormatOutput("./" + selected_category + "/projectList.list", "project")
        target_project_name = project_list_item[target_project_location]
        scripts.globalVar.globalVar.set("selected_project", target_project_name)
        os.system("python .\\modify_project_eventTrigger.py")
        
    def display_project_property(self, event):
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        target_project_location = self.list_display_project_list.GetSelection()
        project_list_item =  scripts.inputManager.outputManager.listFileContentFormatOutput("./" + selected_category + "/projectList.list", "project")
        target_project_name = project_list_item[target_project_location]
        scripts.globalVar.globalVar.set("selected_project", target_project_name)
        os.system("python .\\project_properties_eventTrigger.py")
        
    def open_about(self, event):
        os.system("python .\\about_eventTrigger.py")
        
    def enter_file_list(self, event):
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        target_project_location = self.list_display_project_list.GetSelection()
        project_list_item =  scripts.inputManager.outputManager.listFileContentFormatOutput("./" + selected_category + "/projectList.list", "project")
        target_project_name = project_list_item[target_project_location]
        scripts.globalVar.globalVar.set("selected_project", target_project_name)
        os.system("python .\\file_list_eventTrigger.py")
    
        
app = wx.App(False)
page = PageEvent(None)
page.Show(True)
app.MainLoop()