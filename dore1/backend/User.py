from .data_sent import data_sent
from .mongoDb import mongoDb



class User():
    def __init__(self):
        self.data_sent=data_sent()
        self.mongoDb=mongoDb()
    def saveUser(self,data):
        model=self.mongoDb.readInformation("_id",data[0])
        if model!=False:
            return "این کاربر تکراری است"
        else :
            data1=self.mongoDb.configData1(data)
            model2=self.mongoDb.saveData(data1)
            #data2=["lit_user_1997",data[0]]
            if model2==True:
                return "عملیات موفقیت آمیز بود"
            else : 
                return "خطای ناخواسته رخ داد لطفا مجددا تلاش کنید"
    def getReport(self,username,password):
        if username=="parswork" and password=="Parswork19971997":
            data=self.mongoDb.getAllData()
            return True,data
        else :
            return False,"Error 401"