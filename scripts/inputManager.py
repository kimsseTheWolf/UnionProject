class inputManager():
    
    def __init__(self,current_Level):
        self.current_Level = current_Level
    
    def userInput(Message):
        respond = ""
        print(Message)
        print("?>", end="")
        respond = input(respond)
        return respond
    
    def ynInput(Message, defaultAnswerIsABoolean):
        respond = ""
        print(Message)
        print("?>", end="(y stands yes and n stands no)")
        try:
            if (respond == "y" or "Y"):
                return True
            elif (respond == "n" or "N"):
                return False
        except:
            print("This is an invaild answer, system will use the default answer")
            return defaultAnswerIsABoolean
    
    def readFile(File):
        target_file = open(File, "r")
        return_result = target_file.readlines()
        return return_result
    
    def readJSONInfo(File):
        try:
            target_file = open(File, "r")
            jsonInfo = target_file.readlines()
            print(jsonInfo)
        except:
            print()
            
class outputManager():
    
    def listFileContentFormatOutput(list_file_location, belong_type):
        try:
            target_list_file = open(list_file_location, "r")
            list_file_content =  target_list_file.readlines()
            # strip all the \n for all the elements inside the content list
            new_list_file_content = []
            for i in list_file_content:
                i = i.rstrip("\n")
                new_list_file_content.append(i)
            # output the elements for the user in a more beautiful way
            if (belong_type == "category"):
                print("You have created the following categories:")
            elif (belong_type == "project"):
                print("You have created the following projects:")
            elif (belong_type == "file"):
                print("You have created the following files:")
            else:
                print("Undefined items:")
                
            if (new_list_file_content[0] == ""):
                print("You haven\'t create anything yet...")
            else:
                for i in new_list_file_content:
                    print(i, end=", ")
                print("\n")
                
            return new_list_file_content
                
        except:
            print("You haven\'t create anything yet...")
            
    def ListToString(list:list):
        output_result = ""
        for i in list:
            output_result = output_result + i
        return output_result