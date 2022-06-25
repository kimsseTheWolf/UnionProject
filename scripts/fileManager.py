import json
import time
import os
import shutil
import socket

class basicFileManager():
    
    # add the new file to the list file
    def addListFileItem(self, selectedCategory, selectedProject, fileName):
        target_list_file_direction = "./" + selectedCategory + "/" + selectedProject + "/fileList.list"
        target_list_file = open(target_list_file_direction, "a")
        target_list_file.writelines(fileName + "\n")
        target_list_file.close()
        
    # help to create a new json desciprtion file for the imported files
    def createFileJSONDescription(self, selectedCategory, selectedProject, fileName, originFileLocation):
        target_json_file_direction = "./" + selectedCategory + "/" + selectedProject + "/" + fileName + "/config.json"
        target_json_file = open(target_json_file_direction, "w")
        # gather create time
        create_time = time.asctime(time.localtime(time.time()))
        # gather last edited time
        last_edit_time = time.asctime(time.localtime(time.time()))
        # set file readable state
        isAccessable = "true"
        # gather the settings from the data folder
        with open("./data/settings.json", "r") as setting_json_file:
            settings =  json.load(setting_json_file)
        # detect whether saving history is enabled
        if (settings["auto_save_file_history"] == "true"):
            auto_save_history = "true"
        else:
            auto_save_history = "false"
        # gather the pyhsical location name for this device (at ::data/info.json)
        with open("./data/info.json", "r") as info_json_file:
            data = info_json_file.readlines()
            json_data = ""
            for i in data:
                json_data = json_data + i
            info = json.loads(json_data)
            phy_loc_name = info["local_physical_location"]
        # create new tulple for the json
        input_json_data = {
            "Name": fileName,
            "CreateTime": create_time,
            "LastEditTime": last_edit_time,
            "Accessibility": isAccessable,
            "AutoSave": auto_save_history,
            "PhysicalFileLocation": phy_loc_name,
            "FileLocation": originFileLocation
        }
        # convert tulple to json data
        target_json_file.writelines(json.dumps(input_json_data))
        target_json_file.close()
        
    # help to create an description file for the imported files
    def createDescriptionFile(self, selectedCategory, selectedProject, fileName):
        target_description_file_direction = "./" + selectedCategory + "/" + selectedProject + "/" + fileName + "/description.txt"
        target_description_file = open(target_description_file_direction, "w")
        result = ""
        print("Please enter the description for your current file. If no, then press enter.")
        result = input(result)
        target_description_file.writelines(result)
        target_description_file.close()
        
    # delete the hole file from the category, but not in your origin.
    def deleteFile(self, selectedCategory, selectedProject, fileName):
        target_direction = "./" + selectedCategory + "/" + selectedProject + "/" + fileName
        shutil.rmtree(target_direction)
        
basic_file_manager = basicFileManager()

class fileManager():
    
    # import a file
    def importFile(selectedCategory, selectedProject, localFileDirection):
        
        inprogram_location = "./" + selectedCategory + "/" + selectedProject + "/"
        win_inprogram_location = ".\\" + selectedCategory + "\\" + selectedProject + "\\"
        
        # gather the target file
        # detect whether this file is exist. (if yes, then run the EXCEPT part!)
        
        if (os.path.exists(localFileDirection) == True):
            print("we have found your target file. Start progressing...")
            # gather the file origin name
            file_name = os.path.basename(localFileDirection)
            # check whether the file has already exist and decide the continuity
            if (os.path.exists(inprogram_location + file_name) == True):
                print("This file has already exist. Try renaming the file name and try again.")
                pass
            else:
                # add an item to the list file of the project (fileList.list)
                basic_file_manager.addListFileItem(selectedCategory, selectedProject, file_name)
                # create a folder for the file
                os.mkdir(inprogram_location + file_name)
                # copy the file to the system directory and save there
                # change all the symbol "/" to "\" to support the cmd
                new_fileLocation = ""
                for i in localFileDirection:
                    if (i == "/"):
                        new_fileLocation = new_fileLocation + "\\"
                    else:
                        new_fileLocation = new_fileLocation + i
                print(new_fileLocation)
                os.system("copy " + new_fileLocation + " " + win_inprogram_location + file_name)
                # generate single file's json properties.
                basic_file_manager.createFileJSONDescription(selectedCategory, selectedProject, file_name, localFileDirection)
                # add an discription file for this imported file
                basic_file_manager.createDescriptionFile(selectedCategory, selectedProject, file_name)
                print("Create Successfully! : " + file_name)
                pass
        else:
            print("This file does not exist!")
    
    # delete a file
    def deleteFile (selectedCategory, selectedProject, fileName):
        
        target_file_location = "./" + selectedCategory + "/" + selectedProject + "/"
        # delete the file folder
        basic_file_manager.deleteFile(selectedCategory, selectedProject, fileName)
        # remove this file item from the list file
        list_file = open(target_file_location + "/fileList.list", "r")
        list_file_item = list_file.readlines()
        list_file.close()
        try:
            # delete item
            list_file_item.remove(fileName + "\n")
            # write the new data to the list file
            list_file = open(target_file_location + "/fileList.list", "w")
            for i in list_file_item:
                list_file.writelines(i)
            list_file.close()
            
            print("File deleted from the project successfully! File in the source will not be delete!")
        except:
            print("Error: File does not exist.")
            
    # open a file
    def openFile (selectedCategory, selectedProject, fileName):
        
        target_file_location = "./" + selectedCategory + "/" + selectedProject + "/" + fileName + "/" + fileName
        win_target_file_location = ".\\" + selectedCategory + "\\" + selectedProject + "\\" + fileName + "\\" + fileName
        
        # open the file
        try:
            os.startfile(win_target_file_location)
            print("File opened...")
        except:
            print("System can\'t open the file for you for some reason. Please contact the technical support!")