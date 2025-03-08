from django.shortcuts import render,redirect
from .backend.data_sent import data_sent
import os
from django.http import HttpResponse, Http404
from .backend.mongoDb import mongoDb
from .backend.User import User
from .backend.prameter import parameter
import mimetypes
from .models import UserModel
from .forms import RegisterForm



class Views():
    def __init__(self) -> None:
        self.data_sent=data_sent()
        self.mongoDb=mongoDb()
        self.User=User()
        self.UserModel=UserModel()
    def mainPage(self,request):
        return render(request, 'index.html')


    def addUser(self,request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()  
                message=self.data_sent.message_register_succ
                return render(request, 'message.html',{'message':message})
        else:
            form = RegisterForm()
    
        return render(request, 'index.html', {'form': form})
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