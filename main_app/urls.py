from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('tasks/', views.Tasks.as_view(), name="tasks"),
    path('tasks/new/', views.NewTask.as_view(), name="newTask"),
    path('tasks/<int:pk>', views.TaskDetail.as_view(), name="taskDetail"),
    path('tasks/<int:pk>/update', views.TaskUpdate.as_view(), name="taskUpdate"),
    path('tasks/<int:pk>/delete', views.TaskDelete.as_view(), name="taskDelete"),
    path('user/<username>', views.Profile, name='profile'),
    path('login/', views.login, name='login'),
     path('logout/', views.logout, name='logout'),
]