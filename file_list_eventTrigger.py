import wx
import os
import GUI.file_list_page
import scripts.inputManager
import scripts.fileManager
import scripts.globalVar
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkinter.filedialog import askopenfilenames

root = Tk()
root.withdraw()

class PageEvent(GUI.file_list_page.file_list):
    
    def __init__(self, parent):
        GUI.file_list_page.file_list.__init__(self, parent)
        
    def init_data(self, event):
        # gather data
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        selected_project = scripts.globalVar.globalVar.get("selected_project")
        target_list_file_location = open("./" + selected_category + "/" + selected_project + "/fileList.list", "r")
        print(target_list_file_location)
        file_list = target_list_file_location.readlines()
        format_file_list = scripts.inputManager.outputManager.listFileContentFormatOutput(file_list, "project")
        print(format_file_list)
        for i in format_file_list:
            self.list_fileList.Append(i)
            
    def refresh(self, event):
        self.list_fileList.Clear()
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        selected_project = scripts.globalVar.globalVar.get("selected_project")
        target_list_file_location = open("./" + selected_category + "/" + selected_project + "/fileList.list", "r")
        file_list = target_list_file_location.readlines()
        print(file_list)
        format_file_list = scripts.inputManager.outputManager.listFileContentFormatOutput(file_list, "project")
        for i in file_list:
            self.list_fileList.Append(i)
            
    def open_file(self, event):
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        selected_project = scripts.globalVar.globalVar.get("selected_project")
        target_file_location = self.list_fileList.GetSelection()
        file_list = open("./" + selected_category + "/" + selected_project +"/fileList.list", "r")
        file_item = file_list.readlines()
        print(file_item)
        new_file_item = []
        for i in file_item:
            i = i.rstrip("\n")
            new_file_item.append(i)
        print(file_item)
        target_file_name = new_file_item[target_file_location]
        print(target_file_name)
        scripts.fileManager.fileManager.openFile(selected_category, selected_project, target_file_name)
    
    def delete_file(self, event):
        result = messagebox.askyesno("Warning", "You are going to delete this file. Are you sure you want to continue? This progress will not be able to reverse.")
        if (result == True):
            selected_category = scripts.globalVar.globalVar.get("selected_category")
            selected_project = scripts.globalVar.globalVar.get("selected_project")
            target_file_location = self.list_fileList.GetSelection()
            file_list = open("./" + selected_category + "/" + selected_project +"/fileList.list", "r")
            file_item = file_list.readlines()
            print(file_item)
            new_file_item = []
            for i in file_item:
                i = i.rstrip("\n")
                new_file_item.append(i)
            print(file_item)
            target_file_name = new_file_item[target_file_location]
            print(target_file_name)
            scripts.fileManager.fileManager.deleteFile(selected_category, selected_project, target_file_name)
        else:
            messagebox.showinfo("Info", "Progress cancled!")
            
    def openFileLocation(self, event):
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        selected_project = scripts.globalVar.globalVar.get("selected_project")
        target_file_location = self.list_fileList.GetSelection()
        file_list = open("./" + selected_category + "/" + selected_project +"/fileList.list", "r")
        file_item = file_list.readlines()
        print(file_item)
        new_file_item = []
        for i in file_item:
            i = i.rstrip("\n")
            new_file_item.append(i)
        print(file_item)
        target_file_name = new_file_item[target_file_location]
        print(target_file_name)
        location = ".\\" + selected_category + "\\" + selected_project + "\\" + target_file_name
        command = "start " + location
        os.system(command)
    
    def create_file(self, event):
        os.system("python .\\create_file_eventTrigger.py")
            
    def display_category_properties(self, event):
        os.system("python .\\category_properties_eventTrigger.py")
        
    def display_project_properties(self, event):
        os.system("python .\\project_properties_eventTrigger.py")
        
    def display_about(self, event):
        os.system("python .\\about_eventTrigger.py")
        
    def import_file(self, event):
        os.system("python .\\import_file_eventTrigger.py")
        
app = wx.App(False)
page = PageEvent(None)
page.Show(True)
app.MainLoop()