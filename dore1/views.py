from django.shortcuts import render
from .backend.data_sent import data_sent
import os
from django.http import HttpResponse, Http404
from .backend.mongoDb import mongoDb
from .backend.User import User
from .backend.prameter import parameter
import mimetypes



class Views():
    def __init__(self) -> None:
        self.data_sent=data_sent()
        self.mongoDb=mongoDb()
        self.User=User()
    def mainPage(self,request):
        return render(request, 'index.html')
    def saveData(self,request):
        data=[]
        data1= request.POST
        select = data1.dict()
        data.append(select["ncode"]) 
        data.append(select["username"])
        data.append(select['phonenumber'])
        data.append(select["rtahsil"])
        data.append(select['email'])
        data.append(select['arr'])
        print(data)
        message=self.User.saveUser(data)
        
        return render(request, 'message.html',{'message':message})
        

    def getReport(self,request):
        
        return render(request, 'report.html')
    def getReportOut(self,request):
        data1= request.POST
        select = data1.dict()
        username=select["username1"]
        password=select["password1"]
        parameter.data=self.User.getReport(username,password)
        if parameter.data==False:
            message="اطلاعات کاربری نادرست"
            return render(request, 'message.html',{'message':message})
        
        return render(request, 'output.html')

    def downloadextract(self,request):
        


        filepath =parameter.data
        

        path = open(filepath, 'rb')

        mime_type, _ = mimetypes.guess_type(filepath)

        response = HttpResponse(path, content_type=mime_type)
        head, tail = os.path.split(filepath)
        response['Content-Disposition'] = "attachment; filename=%s" % tail

        return response