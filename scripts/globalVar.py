# This is the file for system to save and share the global vars
import json

class basicGlobalVarFeatures():
    
    def readData():
        with open("./data/globalVar.json", "r") as globalVarFile:
            result = json.load(globalVarFile)
        return result
    
    def writeData(data):
        # the data must be a touple
        try:
            with open("./data/globalVar.json", "w") as globalVarFile:
                json.dump(data, globalVarFile)
            return True
        except:
            return False
        
class globalVar():
    
    def get(key):
        returnResult = basicGlobalVarFeatures.readData()
        try:
            return returnResult[key]
        except:
            print("Error: Object not found!")
            return False
        
    def set(key, value):
        try:
            returnResult = basicGlobalVarFeatures.readData()
            returnResult[key] = value
            basicGlobalVarFeatures.writeData(returnResult)
            return True
        except:
            print("Error: Unable to add")
            return False
        
    def delete(key):
        returnResult = basicGlobalVarFeatures.readData()
        try:
            del returnResult[key]
            basicGlobalVarFeatures.writeData(returnResult)
            return True
        except:
            print("Error: Unable to delete")
            return False
        
    def clear():
        returnResult = basicGlobalVarFeatures.readData()
        returnResult.clear()
        basicGlobalVarFeatures.writeData(returnResult)