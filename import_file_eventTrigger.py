import wx
import os
import GUI.import_file_page
import scripts.inputManager
import scripts.fileManager
import scripts.globalVar
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkinter.filedialog import askopenfilenames

root = Tk()
root.withdraw()

class PageEvent(GUI.import_file_page.import_file_dialog):
    
    def __init__(self, parent):
        GUI.import_file_page.import_file_dialog.__init__(self, parent)
        
    def choose_files(self, event):
        result = askopenfilenames(title = "Select files...")
        target_file_list = []
        self.m_listBox2.Clear()
        for i in result:
            self.m_listBox2.Append(i)
            target_file_list.append(i)
        scripts.globalVar.globalVar.set("target_import_file", target_file_list)
            
            
    def import_files(self, event):
        target_files = scripts.globalVar.globalVar.get("target_import_file")
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        selected_project = scripts.globalVar.globalVar.get("selected_project")
        print(selected_category, "|", selected_project)
        
        for i in target_files:
            result = scripts.fileManager.fileManager.GUIimportFile(selected_category, selected_project, i)
            if (result == True):
                pass
            else:
                messagebox.showerror("Error", "We can\'t progress for you. Please try again later.")
                scripts.fileManager.fileManager.deleteFile(selected_category, selected_project, i)
        messagebox.showinfo("Success", "Progress Done!")
        self.Destroy()
        
    def close_window(self, event):
        self.Destroy()
        
app = wx.App(False)
page = PageEvent(None)
page.Show(True)
app.MainLoop()