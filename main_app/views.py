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

class NewTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'categories', 'discription', 'date', 'time', 'complete']
    template_name = "newTask.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect('/tasks')

class TaskDetail(DetailView):
    model = Task
    template_name = "taskDetail.html"

@method_decorator(login_required, name="dispatch")
class TaskUpdate(UpdateView):
    template_name = "taskUpdate.html"
    model = Task
    fields = ['title', 'categories', 'discription', 'date', 'time', 'complete']

    def get_success_url(self):
        return reverse('taskDetail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name="dispatch")
class TaskDelete(DeleteView):
    model = Task
    template_name = 'taskDeleted.html'
    success_url = "/tasks/"

@login_required
def Profile(request, username):
    user = User.objects.get(username=username)
    tasks = Task.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'tasks': task})

#Django Auth
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            return render(request, 'signup.html', {'form': form})    
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
                    return render(request, 'login.html', {'form': form})
            else:
                print('The username and/or password is incorrect.')
                return render(request, 'login.html', {'form': form})
        else: 
            return render(request, 'signup.html', {'form': form})
    else: 
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})