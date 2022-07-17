import wx
import GUI.create_file_page
import scripts.globalVar
import scripts.fileManager
from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()

class PageEvent(GUI.create_file_page.create_file_dialog):
    
    def __init__(self, parent):
        GUI.create_file_page.create_file_dialog.__init__(self, parent)
        pass
    
    def close_window(self, event):
        self.Destroy()
        
    def create_file(self, event):
        selected_category = scripts.globalVar.globalVar.get("selected_category")
        selected_project = scripts.globalVar.globalVar.get("selected_project")
        file_name = self.input_filename.GetValue()
        if (file_name == "description.txt" or file_name == "config.json"):
            messagebox.showerror("Error", "The file name you indicated will conflict with the system configuration file. Try another except decription.txt or config.json")
            pass
        else:
            result = scripts.fileManager.fileManager.createFile(selected_category, selected_project, file_name)
            if (result == True):
                messagebox.showinfo("Info", "Create Successfully!")
                self.Destroy()
            else:
                messagebox.showerror("Error", "Unable to create file. Check your file name and try again.")
            
app = wx.App(False)
page = PageEvent(None)
page.Show(True)
app.MainLoop()