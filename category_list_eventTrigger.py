from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkinter.tix import Select
import wx
import wx.xrc
import GUI.category_list_page
import sys
import os
import scripts.inputManager
import scripts.jsonLibManager
import scripts.globalVar

input_manager = scripts.inputManager
creator = scripts.jsonLibManager
global_var = scripts.globalVar.globalVar

root = Tk()
root.withdraw()

class PageEvent(GUI.category_list_page.MyFrame1):
    
    def __init__(self, parent):
        GUI.category_list_page.MyFrame1.__init__(self, parent)
        pass
    
    def refresh_category_list(self, event):
        self.category_list.Clear()
        category_list_file = open("./categoryList.list", "r")
        category_list_elements =  category_list_file.readlines()
        format_category_list_file_manager = input_manager.outputManager.listFileContentFormatOutput("./categoryList.list", "category")
        print(format_category_list_file_manager)
        for i in format_category_list_file_manager:
            self.category_list.Append(i)
            
    # def sync_category_name(self, event):
    #     selected_category = self.category_list.GetString()
            
    def create_category(self, event):
        os.system("python .\\create_category_eventTrigger.py")
    
    def delete_category(self, event):
        target_categoory_location = self.category_list.GetSelection()
        category_list_item =  input_manager.outputManager.listFileContentFormatOutput("./categoryList.list", "category")
        target_category_name = category_list_item[target_categoory_location]
        answer = askyesno("Warning", "This will delete everything contain in this category. Are you sure you want to delete it?")
        if (answer == True):
            creator.createManager.GUIdeleteCategory(target_category_name)
        else:
            messagebox.showinfo("Progress cancled!", "You cancled the delete progress.")
        self.refresh_category_list()
        
    def modify_category(self, event):
        target_categoory_location = self.category_list.GetSelection()
        category_list_item =  input_manager.outputManager.listFileContentFormatOutput("./categoryList.list", "category")
        target_category_name = category_list_item[target_categoory_location]
        print(target_category_name)
        # global selected_category
        global_var.set("selected_category", target_category_name)
        os.system("python .\\modify_category_eventTrigger.py")
        
    def display_properties(self, event):
        target_categoory_location = self.category_list.GetSelection()
        category_list_item =  input_manager.outputManager.listFileContentFormatOutput("./categoryList.list", "category")
        target_category_name = category_list_item[target_categoory_location]
        print(target_category_name)
        # global selected_category
        global_var.set("selected_category", target_category_name)
        os.system("python .\\category_properties_eventTrigger.py")
        
    def open_about(self, event):
        os.system("python .\\about_eventTrigger.py")
        
    def clearData(self, event):
        self.Destroy()
        
    def enter_category(self, event):
        target_categoory_location = self.category_list.GetSelection()
        category_list_item =  input_manager.outputManager.listFileContentFormatOutput("./categoryList.list", "category")
        target_category_name = category_list_item[target_categoory_location]
        scripts.globalVar.globalVar.set("selected_category", target_category_name)
        os.system("python ./project_list_eventTrigger.py")
        self.Close()
        
    def export_category(self, event):
        os.system("python .\\export_category_eventTrigger.py")
        
    
        
    # def main():
    #     app = wx.App(False)
    #     page = PageEvent(None)
    #     page.Show(True)
    #     app.MainLoop()
        
    # if __name__ == "__main__":
    #     main()

app = wx.App(False)
page = PageEvent(None)
page.Show(True)
app.MainLoop()

