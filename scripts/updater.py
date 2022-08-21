# This file will update when a new version is release

import json

class updater():
    
    def update_project(target_project_properties_file:str):
        
        #open target properties file
        with open(target_project_properties_file, "r") as target_json_file:
            old_properties:dict = json.load(target_json_file)
        
        #modify properties
        #add isFinished property and projectVersion property
        old_properties["isFinished"] = False
        old_properties["projectVersion"] = "v2"
        
        #write out new properties
        with open(target_project_properties_file, "w") as target_json_file:
            json.dump(old_properties)