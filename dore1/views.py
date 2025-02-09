from django.shortcuts import render
from backend.data_sent import data_sent
import os
from django.http import HttpResponse, Http404
import mimetypes



class Views():
    def __init__(self) -> None:
        self.data_sent=data_sent()
 
    def mainPage(self,request):
        return render(request, 'home.html')
    