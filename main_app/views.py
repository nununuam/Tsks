from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView


# Create your views here.
class Cat:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

cats = [
    Cat("Mau", 5, "Female"),
    Cat("Garfield", 43, "Male"),
    Cat("Meowth", 25, "Male"),
    Cat("Salem", 500, "Male"),
]

class CatList(TemplateView):
    template_name = 'catlist.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cats"] = cats # this is where we add the key into our context object for the view to use
        return context

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