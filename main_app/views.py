from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 


# Create your views here.


class Home(View):
    def get(self, request):
        return HttpResponse("Welcome to Tsks")

class Tasks(View):
    def get(self, request):
        return HttpResponse("Tasks Page")

class addCategories(View):
    def get(self, request):
        return HttpResponse("New Categories")
        
class NewTask(View):
    def get(self, request):
        return HttpResponse("New Task Page")

class editAndDelete(View):
    def get(self, request):
        return HttpResponse("Edit and Delete Page")