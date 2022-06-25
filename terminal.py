import json
import scripts.jsonLibManager #inside the folder shell
import scripts.inputManager #inside the folder shell
import scripts.fileManager
import sys

#TODO: 

version = "Version Beta 1.0.7 - Windows (PreRealse)"

print("Welcome to use Union Project Manager Terminal!" + version)
print("If you want to create, enter \"create\" + category name")
print("If you want to add, enter \"add\"")
print("The allowed category names are: category, project, files")
print("Enter updateLog to check what\'s new in our program.")

creator = scripts.jsonLibManager.createManager #insert the port: class: createManager
input_manager = scripts.inputManager.inputManager #insert the port: class: inputManager
output_manager = scripts.inputManager.outputManager #insert the port class: outputManager
file_manager = scripts.fileManager.fileManager #insert the port: class: fileManager
current_Level = "category"
selected_category = ""
selected_project = ""

while True:
    print(selected_category + ":" + selected_project, end = "")
    respond = "" #initialize respond string
    respond =  input_manager.userInput("")
    # print(respond)
    #create command
    if (respond[0:6] == "create"):
        if (respond[6:].find("category") == True): 
            #create category
            categoryName = respond[16:]
            creator.createCategory(categoryName)
        elif (respond[6:].find("project") == True):
            #create project
            if (selected_category != ""):
                projectName = respond[15:]
                creator.createProject(projectName, selected_category)
            else:
                print("You need to select a category, then use this create command.")
        elif (respond[6:].find("file") == True):
            # create file command, and notify user this is not importing files.
            print("Please notice that this is a place where create a file! If you want to import your own file. Please use \"add\" command")
            
    #add command
    if (respond[0:3] == "add"):
        if (respond[3:].find("file") == True):
            #add a file
            if (selected_category != "" and selected_project != ""):
                target_file_location = respond[9:]
                print(target_file_location)
                file_manager.importFile(selected_category, selected_project, target_file_location)
            else:
                print("You need to select a category and a project, then use this add command!")
                
    #open command
    if (respond[0:4] == "open"):
        if (respond[4:].find("file") == True):
            # open the file by using the system way
            if (selected_category != "" and selected_project != ""):
                file_name = respond[10:]
                file_manager.openFile(selected_category, selected_project, file_name)
            else:
                print("You need to select a category and a project, then use this open command!")
        

    #list command
    elif (respond[0:4] == "list"):
        if (respond[4:].find("category") == True):#list category
            output_manager.listFileContentFormatOutput("./categoryList.list", "category")
        elif (respond[4:].find("project") == True):
            if (selected_category != ""):
                output_manager.listFileContentFormatOutput("./" + selected_category + "/projectList.list", "project")
            else:
                print("You need to select a category, then use this list command.")
        elif (respond[4:].find("file") == True):
            if (selected_category != "" and selected_project != ""):
                output_manager.listFileContentFormatOutput("./" + selected_category + "/" + selected_project + "/fileList.list", "file")
            else:
                print("You need to select a category and a project, then use this list command.")
    
    #info command
    elif (respond[0:4] == "info"):
        if (respond[4:].find("category") == True):
            targetCategoryName = respond[14:]
            print(targetCategoryName)
            targetCategoryInfoLocation = "./" + targetCategoryName + "/config.json"
            input_manager.readJSONInfo(targetCategoryInfoLocation)
            creator.readDescriptionFile(targetCategoryName + "/description.txt")
        elif (respond[4:].find("project") == True):
            if (selected_category != ""):
                targetProjectName = respond[13:]
                print(targetProjectName)
                targetProjectInfoLocation = "./" + selected_category + "/" + targetProjectName + "/config.json"
                input_manager.readJSONInfo(targetProjectInfoLocation)
                creator.readDescriptionFile("./" + selected_category + "/" + targetProjectName + "/description.txt")
            else:
                print("You need to select a category, then use this create command.")
        elif (respond[4:].find("file")):
            if (selected_category != "" and selected_project != ""):
                target_file_name = respond[10:]
                print(target_file_name)
                target_file_location = "./" + selected_category + "/" + selected_project + "/" + target_file_name + "/config.json"
                input_manager.readJSONInfo(target_file_location)
                creator.readDescriptionFile(target_file_location + "/description.txt")
                pass
            else:
                print("You need to select a category and a project, then use this info command.")
                
            
    #modify command
    elif (respond[0:6] == "modify"):
        if (respond[6:].find("category") == True):
            if (respond[15:].find("name") == True):
                targetCategoryName = respond[21:]
                print(targetCategoryName)
                creator.modifyCategory(targetCategoryName, "name")
            elif (respond[15:].find("description") == True):
                targetCategoryName = respond[28:]
                print(targetCategoryName)
                creator.modifyCategory(targetCategoryName, "description")
        elif (respond[6:].find("project") == True):
            if (selected_category != ""):
                if (respond[14:].find("name") == True):
                    targetProjectName = respond[20:]
                    print(targetProjectName)
                    creator.modifyProject(targetProjectName, selected_category, "name")
                elif (respond[14:].find("description") == True):
                    targetProjectName = respond[34:]
                    print(targetProjectName)
                    creator.modifyProject(targetProjectName, selected_category, "description")
            else:
                print("You need to select a category, then use this create command.")
            
    #delete command
    elif (respond[0:6] == "delete"):
        if (respond[6:].find("category") == True):
            targetCategoryName = respond[16:]
            print(targetCategoryName)
            creator.deleteCategory(targetCategoryName)
            selected_category = ""
        elif (respond[6:].find("project") == True):
            if (selected_category != ""):
                targetProjectName = respond[15:]
                print(targetProjectName)
                creator.deleteProject(targetProjectName, selected_category)
            else:
                print("You need to select a category, then use this create command.")
        elif (respond[6:].find("file") == True):
            if (selected_category != "" and selected_project != ""):
                targetFileName = respond[12:]
                file_manager.deleteFile(selected_category, selected_project, targetFileName)
            
    #select command (IMPORTANT: All the sublevels procedures will check this value first!)
    elif (respond[0:6] == "select"):
        if (respond[6:].find("category") == True):
            target_selected_category = respond[16:]
            # print(target_selected_category)
            result =  creator.checkCategoryExistence(target_selected_category)
            if (result == True):
                selected_category = target_selected_category
                print("You selected a category: " + selected_category)
            else:
                print("Something went wrong while selecting your category: No such category. Check your name and try again.")
        elif (respond[6:].find("project") == True):
            if (selected_category != ""):
                target_selected_projects = respond[15:]
                # print(target_selected_category)
                result = creator.checkProjectExistance(target_selected_projects, selected_category)
                if (result == True):
                    selected_project = target_selected_projects
                    print("You selected a project: " + selected_project)
                else:
                    print("Something went wrong while selecting your category: No such category. Check your name and try again.")
            else:
                print("You need to select a category, then use this select command.")
                
    #deselect command
    elif (respond[0:8] == "deselect"):
        if (selected_project != ""):
            selected_project = ""
            pass
        elif (selected_category != ""):
            selected_category = ""
            pass
        else:
            print("You didn\'t select a category or a project yet...")
            
    elif (respond[0:7] == "version"):
        print(version)
                
    
    #exit command
    elif (respond == "exit"):
        exit("Exiting Union Project Manager Terminal. You can use the main.py file in this directory next time.")
        
    elif (respond == "updateLog"):
        print("Current version:" + version)
        updateLog = open("./updateLog", "r")
        output_list = updateLog.readlines()
        final_output_list = []
        for i in output_list:
            i.rstrip("\n")
            print(i)
        
    else:
        print("No such file or command to execute, check your spelling and try again.")
        
    del respond