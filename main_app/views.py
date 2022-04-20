from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView


# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

class Tasks(TemplateView):
     template_name = "tasks.html"

class addCategories(TemplateView):
     template_name = "addCategories.html"
        
class NewTask(TemplateView):
    template_name = "newTasks.html"

class editAndDelete(TemplateView):
     template_name = "editAndDelete.html"