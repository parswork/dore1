from .data_sent import data_sent
from .mongoDb import mongoDb
from dore1.forms import RegisterForm
from dore1.models import UserModel
from django.http import HttpResponse
from openpyxl import Workbook


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
           
            if model2==True:
                return "عملیات موفقیت آمیز بود"
            else : 
                return "خطای ناخواسته رخ داد لطفا مجددا تلاش کنید"
    def getReport(self,username,password):
        current_directory = os.getcwd()+"/file/output.txt"
       
        username=username.replace(""," ")
        password=password.replace(""," ")
        if username=="parswork" and password=="Parswork19971997":
            data=self.mongoDb.getAllData()
            
            file=open(current_directory,"w",encoding="utf8")
            for index,item in enumerate(data):
                file.write("================\n")
                for key, value in item.items():
                        file.write(f'{key}, {value}')
                        file.write("\n")
                     
                
            file.close()
            

            return current_directory
        else :
            return False
    def getAllUser(self):
        results = UserModel.objects.all()
        print(results)
        for index,item in enumerate(results):
            print(item.email)
        