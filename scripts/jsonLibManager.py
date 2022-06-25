import json
import os
import time
import shutil
from xml.etree.ElementTree import ProcessingInstruction
from . import inputManager
from unicodedata import category

input_manager = inputManager.inputManager


class createManager():
    
    def readDescriptionFile(location):
        description_file = open(location, "r")
        description_content = description_file.readlines()
        output_description_content = []
        for i in description_content:
            i = i.rstrip("\n")
            output_description_content.append(i)
        print("Description:")
        for i in output_description_content:
            print(i)
            
            
    # help to create a category with adding a json configuration file
    def createCategory(CategoryName):
        try:
            # Create a new directory
            directoryName = "./" + CategoryName
            os.mkdir(directoryName)
            # Start to generate a basic category information and configuration file
            configuration = {
                "name": CategoryName,
                "create_date": time.asctime(time.localtime(time.time()))
            }
            # Create a json file and put all the config datas inside it and closed
            json_configuration = json.dumps(configuration)
            print(json_configuration)
            json_config_file = open(directoryName + "/config.json", "x")
            json_config_file.writelines(json_configuration)
            json_config_file.close()
            # Create the list file of their own
            project_list_file = open(directoryName + "/projectList.list", "x")
            project_list_file.close()
            # add an item inside the list file in order to list it later
            category_list_file = open("./categoryList.list", "a")
            category_list_file.writelines(CategoryName + "\n")
            category_list_file.close()
            # Create a description file for the category
            description_file = open(directoryName + "/description.txt", "w")
            respond = ""
            print("Please enter the descriptions for your new category. If you don\'t want to write anything, press Enter.")
            respond = input(respond)
            description_file.writelines(respond)
            description_file.close()
            # report result
            print(
                "You created a new directory successfully, the directory name is called:" + CategoryName)
        except:
            print("It seems that something went wrong while creating a new category, check your category\'s name and retry.")

    def deleteCategory(CategoryName):  # delete the specific cateogry
        try:
            # gather directory direction
            directoryName = "./" + CategoryName
            # ask the user whether to go ahead
            result = input_manager.ynInput(
                "Are you sure you want to delete this category? (All the programs or files will be removed and can not trace back!):" + CategoryName, False)
            if (result == True):
                shutil.rmtree(directoryName)  # force delete everything
                # delete the items from the list file
                # gather original category info to a list
                category_list_file = open("./categoryList.list", "r")
                category_list_origin = category_list_file.readlines()
                category_list_file.close()
                # create after-proceeded list and remove the item from the original list, them copy the left over to the new list
                category_list = []
                for i in category_list_origin:  # remove all the return symbol
                    i = i.rstrip("\n")
                    category_list.append(i)
                try:  # remove the specific category from the list
                    category_list.remove(CategoryName)
                except:
                    print("WARNING: No such category exisit in list file.")
                # write the new list to the origin list file
                category_list_file = open("./categoryList.list", "w")
                for i in category_list:
                    category_list_file.writelines(i + "\n")
                category_list_file.close()
            else:
                print("Progress cancled!")
        except:
            print("It seems that something went wrong while deleting the category:" +
                  CategoryName + ". Maybe this category is no longer exist!")

    def modifyCategory(CategoryName, modifyType):
        if (modifyType == "name"):
            try:
                # fetch the target json file
                target_json_file = "./" + CategoryName + "/config.json"
                # open and read the current data
                json_file = open(target_json_file, "r")
                current_json_config = json_file.readline()
                json_file.close()
                print("current configuration:" + current_json_config)
                # load the json datas in the variables, and modify the name (because the only item can be modified in category is name)
                latest_json_config = json.loads(current_json_config)
                new_name = input_manager.userInput("Enter the new name of your current category.")
                latest_json_config["name"] = new_name
                # put the latest data into json format and put into the files
                input_json_config = json.dumps(latest_json_config)
                json_file = open(target_json_file, "w")
                json_file.writelines(input_json_config)
                # close the file and complete
                json_file.close()
                # rename folder
                current_category_name = "./" + CategoryName
                latest_category_name = "./" + new_name
                os.rename(current_category_name, latest_category_name)
                # modify the name in the list file
                category_list_file = open("./categoryList.list", "r")
                category_list_origin = category_list_file.readlines()
                category_list_file.close()
                # create after-proceeded list and remove the item from the original list, them copy the left over to the new list
                category_list = []
                for i in category_list_origin:  # remove all the return symbol
                    i = i.rstrip("\n")
                    category_list.append(i)
                modify_target = category_list.index(CategoryName)
                category_list[modify_target] = new_name
                category_list_file = open("./categoryList.list", "w")
                for i in category_list:
                    category_list_file.writelines(i + "\n")
                category_list_file.close()
                # announce complete
                print("Modified successfully!")
            except:
                print("It seems that something went wrong while modifing the category\'s name.")
        elif (modifyType == "description"):
            try:
                respond = ""
                print("Please retype your new description for your current category")
                respond = input(respond)
                target_description_file_location = CategoryName + "/description.txt"
                target_description_file = open(target_description_file_location, "w")
                target_description_file.writelines(respond)
                target_description_file.close()
                print("Modified successfully!")
            except:
                print("Something went wrong")
                

    def checkCategoryExistence(CategoryName):
        # Fetch list file
        list_file = open("./categoryList.list", "r")
        # add all the names into list
        existed_categories = list_file.readlines()
        proceeded_existed_categories = []
        for i in existed_categories:
            i = i.rstrip("\n")
            proceeded_existed_categories.append(i)
        # print(proceeded_existed_categories)
        # check whether exist and return a value
        try:
            proceeded_existed_categories.index(CategoryName)
            return True
        except:
            return False

    def createProject(ProjectName, belongCategory):
        try:
            # create a new folder for the project inside the category folder
            direction_name = "./" + belongCategory + "/" + ProjectName
            os.mkdir(direction_name)
            # create config file for the project
            configuration = {
                "name": ProjectName,
                "create_date": time.asctime(time.localtime(time.time()))
            }
            # Create a json file and put all the config datas inside it and closed
            json_configuration = json.dumps(configuration)
            print(json_configuration)
            json_config_file = open(direction_name + "/config.json", "x")
            json_config_file.writelines(json_configuration)
            json_config_file.close()
            # Create the list file of their own
            project_list_file = open(direction_name + "/fileList.list", "x")
            project_list_file.close()
            # add an item inside the list file in order to list it later
            category_list_file = open(
                "./" + belongCategory + "/projectList.list", "a")
            category_list_file.writelines(ProjectName + "\n")
            category_list_file.close()
            # Create a description file
            respond = ""
            project_description_file = open(direction_name + "/description.txt", "w")
            print("Please enter the descriptions for your new category. If you don\'t want to write anything, press Enter.")
            respond = input(respond)
            project_description_file.writelines(respond)
            project_description_file.close()
            # report result
            print(
                "You created a new directory successfully, the directory name is called:" + ProjectName)
        except:
            print("It seems that something went wrong while creating a new program, check your program\'s name and retry.")

    def deleteProject(ProjectName, belongCategory):
        try:
            # gather directory direction
            directoryName = "./" + belongCategory + "/" + ProjectName
            print(directoryName)
            # ask the user whether to go ahead
            shutil.rmtree(directoryName)  # force delete everything
            # delete the items from the list file
            # gather original project info to a list
            project_list_file = open(
                "./" + belongCategory + "/projectList.list", "r")
            project_list_origin = project_list_file.readlines()
            project_list_file.close()
            # create after-proceeded list and remove the item from the original list, them copy the left over to the new list
            project_list = []
            for i in project_list_origin:  # remove all the return symbol
                i = i.rstrip("\n")
                project_list.append(i)
            try:  # remove the specific category from the list
                project_list.remove(ProjectName)
            except:
                print("WARNING: No such project exisit in list file.")
            # write the new list to the origin list file
            project_list_file = open(
                "./" + belongCategory + "/projectList.list", "w")
            for i in project_list:
                project_list_file.writelines(i + "\n")
            project_list_file.close()
        except:
            print("It seems that something went wrong while deleting the project:" +
                  ProjectName + ". Maybe this project is no longer exist!")

    def checkProjectExistance(ProjectName, belongCategory):
        # Fetch list file
        print(ProjectName, "|", belongCategory)
        list_file = open("./" + belongCategory + "/projectList.list", "r")
        # add all the names into list
        existed_projects = list_file.readlines()
        proceeded_existed_projects = []
        for i in existed_projects:
            i = i.rstrip("\n")
            proceeded_existed_projects.append(i)
        # check whether exist and return a value
        try:
            proceeded_existed_projects.index(ProjectName)
            return True
        except:
            return False

    def modifyProject(ProjectName, belongCategory, modifyType):
        if (modifyType == "name"):
            try:
                # fetch the target json file
                target_json_file = "./" + belongCategory + "/" + ProjectName + "/config.json"
                target_list_file = "./" + belongCategory + "/projectList.list"
                # open and read the current data
                json_file = open(target_json_file, "r")
                current_json_config = json_file.readline()
                json_file.close()
                print("current configuration:" + current_json_config)
                # load the json datas in the variables, and modify the name (because the only item can be modified in category is name)
                latest_json_config = json.loads(current_json_config)
                new_name = input_manager.userInput("Enter the new name of your current project.")
                latest_json_config["name"] = new_name
                # put the latest data into json format and put into the files
                input_json_config = json.dumps(latest_json_config)
                json_file = open(target_json_file, "w")
                json_file.writelines(input_json_config)
                # close the file and complete
                json_file.close()
                # rename folder
                current_project_name = "./" + belongCategory + "/" + ProjectName
                latest_project_name = "./" + belongCategory + "/" + new_name
                os.rename(current_project_name, latest_project_name)
                # modify the name in the list file
                project_list_file = open(target_list_file, "r")
                project_list_origin = project_list_file.readlines()
                project_list_file.close()
                # create after-proceeded list and remove the item from the original list, them copy the left over to the new list
                project_list = []
                for i in project_list_origin:  # remove all the return symbol
                    i = i.rstrip("\n")
                    project_list.append(i)
                modify_target = project_list.index(ProjectName)
                project_list[modify_target] = new_name 
                project_list_file = open(target_list_file, "w")
                for i in project_list:
                    project_list_file.writelines(i + "\n")
                project_list_file.close()
                # announce complete
                print("Modified successfully!")
            except:
                print("It seems that something went wrong while modifing the category\'s name.")
        elif (modifyType == "description"):
            try:
                target_description_file = "./" + belongCategory + "/" + ProjectName + "/description.txt"
                project_description_file = open(target_description_file, "w")
                respond = ""
                print("Please retype your new description for your current category")
                respond = input(respond)
                project_description_file.writelines(respond)
                project_description_file.close()
            except:
                print("Something went wrong")
