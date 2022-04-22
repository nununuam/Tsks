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
    path('tasks/<int:pk>/edit', views.Update.as_view(), name="update"),
    #path('addCategories/', views.addCategories.as_view(), name="categories"),
   # path('cats/', views.CatList.as_view(), name="cat-list"),
]