import time

class timeManager():
    
    def getCurrentTime():
        return time.strftime("%Y/%m/%d", time.asctime)