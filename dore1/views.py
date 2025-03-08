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
from openpyxl import Workbook



class Views():
    def __init__(self) -> None:
        self.data_sent=data_sent()
        self.mongoDb=mongoDb()
        self.User=User()
        self.UserModel=UserModel()
    def mainPage(self,request):
        form = RegisterForm()
        return render(request, 'index.html', {'form': form})


    def addUser(self,request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()  
                message=self.data_sent.message_register_succ
                return render(request, 'message.html',{'message':message})
        else:
            pass
    
        return render(request, 'error.html', {'form': form})
        

    def getReport(self,request):
        
        return render(request, 'report.html')
    
    def getReportOut(self,request):

        if request.user.is_superuser:
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="users.xlsx"'
            workbook = Workbook()
            worksheet = workbook.active
            worksheet.title = 'Users'
            headers = ['Username', 'Email', 'Phone Number','NCode','rtahsi','Address']
            worksheet.append(headers)
            results = UserModel.objects.all()
            for user in results:
                worksheet.append([user.username, user.email, user.phonenumber,user.ncode,user.rtahsi,user.arr])  
            workbook.save(response)
            return response
        else :
            message=self.data_sent.message_limited
            return render(request, 'message.html',{'message':message})
            

   