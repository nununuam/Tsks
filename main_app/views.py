from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Task, Categories
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
"""class Cat:
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
        return context"""

class Home(TemplateView):
    template_name = "home.html"

class Tasks(TemplateView):
     template_name = "tasks.html"
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         title = self.request.GET.get("title")
         context["tasks"] = Task.objects.all()
         print(context['tasks'])
         return context

class NewTask(CreateView):
    model = Task
    fields = ['title', 'categories', 'discription', 'date_time', 'complete']
    template_name = "newTask.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect('/tasks')

class TaskDetail(DetailView):
    model = Task
    template_name = "taskDetail.html"

class TaskUpdate(UpdateView):
    template_name = "update.html"
    model = Task
    fields = ['title', 'categories', 'discription', 'date_time', 'complete']

    def get_success_url(self):
        return reverse('taskDetail', kwargs={'pk': self.object.pk})

class TaskDelete(DeleteView):
    model = Task
    template_name = 'taskDeleted.html'
    success_url = "/tasks/"


#class addCategories(TemplateView):
 #    template_name = "addCategories.html"
        
