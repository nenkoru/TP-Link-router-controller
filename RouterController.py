import requests


class RouterController:
    """
    Class to control TP-LINK router
    
    DEPENDENCTIES:
        requests
    """
    def __init__(self, 
    GATE="http://192.168.0.1",  
    headers = 
    { "Referer": r"http://192.168.0.1/", 
    "Cookie": r"Authorization=Basic YWRtaW46YWRtaW4"}): # this string is an encoded pair 'admin:admin'(
        # login:pass)
        self.GATE = GATE
        self.headers = headers
        self.__tasks = {
        "disconnect": "[ACT_PPP_DISCONN#1,1,1,0,0,0#0,0,0,0,0,0]0,0\r\n",
        "reboot": "[ACT_REBOOT#0,0,0,0,0,0#0,0,0,0,0,0]0,0\r\n",
        "logout": "[/cgi/logout#0,0,0,0,0,0#0,0,0,0,0,0]0,0\r\n",
        "info": "[IGD_DEV_INFO#0,0,0,0,0,0#0,0,0,0,0,0]0,0\r\n"
        } # be careful here, items of keys are very case(& letters)-sensitive


    def __exec(self, data, cgi="/cgi?7"):
        return requests.request("POST", "{0}{1}".format(self.GATE, cgi), headers=self.headers, data=data)

    def __cleanup(self):
        return self.__exec(self.__tasks["logout"], cgi="/cgi?8")

    def __request(self, task, cgi="/cgi?7"):
        r = self.__exec(task, cgi=cgi)
        self.__cleanup()
        return r

    def rebootRouter(self):
        return self.__request(self.__tasks["reboot"])

    def diconnectRouter(self):
        return self.__request(self.__tasks["disconnect"])

    def getInfo(self): 
        return self.__request(self.__tasks["info"], cgi="/cgi?1").text