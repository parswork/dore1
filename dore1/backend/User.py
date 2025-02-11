from .data_sent import data_sent
from .mongoDb import mongoDb


import os

class User():
    def __init__(self):
        self.data_sent=data_sent()
        self.mongoDb=mongoDb()
    
    def saveUser(self,data):
        model=self.mongoDb.readInformation("_id",data[0])
        if model!=False:
            return "این کاربر تکراری است"
        else :
            data11=self.mongoDb.configData1(data)
            print(data11)
            model2=self.mongoDb.saveData(data11)
            #data2=["lit_user_1997",data[0]]
            if model2==True:
                return "عملیات موفقیت آمیز بود"
            else : 
                return "خطای ناخواسته رخ داد لطفا مجددا تلاش کنید"
    def getReport(self,username,password):
        current_directory = os.getcwd()+"/file/output.txt"
       
       
        if username=="parswork" and password=="Parswork19971997":
            data=self.mongoDb.getAllData()
            
            file=open(current_directory,"w",encoding="utf8")
            for index,item in enumerate(data):
                file.write("================\n")
                for key, value in item.items():
                        file.write(f'Key: {key}, Value: {value}')
                        file.write("\n")
                     
                
            file.close()
            

            return current_directory
        else :
            return current_directory