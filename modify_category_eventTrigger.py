from tkinter import *
from tkinter import messagebox
import wx
import wx.xrc
import GUI.modify_category_page
import category_list_eventTrigger
import sys
import os
import scripts.jsonLibManager
import scripts.globalVar

creator = scripts.jsonLibManager
# get the target modify category

# initialize tk GUI
root = Tk()
root.withdraw()

selected_category = scripts.globalVar.globalVar.get("selected_category")

class PageEvent(GUI.modify_category_page.ModifyCategoryWindow):
    
    def __init__(self, parent):
        GUI.modify_category_page.ModifyCategoryWindow.__init__(self, parent)
        pass
    
    def setInputValue(self, event):
        self.input_category_name.SetValue(selected_category)
        target_description_file = open(selected_category + "/description.txt", "r")
        description_content = target_description_file.readlines()
        for i in description_content:
            self.input_description.SetValue(self.input_description.GetValue() + i)
        pass
    
    def exit_window(self, event):
        self.Close()  
        self.Destroy()
        pass
    
    def modify_category(self, event):
        modified_category_name = self.input_category_name.GetValue()
        modified_category_description = self.input_description.GetValue()
        result =  creator.createManager.GUImodifyCategory(selected_category, modified_category_name, modified_category_description)
        if (result == True):
            messagebox.showinfo("Success!", "Modified successfully!")
            self.Destroy()
        else:
            messagebox.showerror("Error", "An error ocure while moifing your category. Please try again!")


app = wx.App(False)
page = PageEvent(None)
page.Show(True)
app.MainLoop()