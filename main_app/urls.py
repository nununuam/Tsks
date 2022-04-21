from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('tasks/', views.Tasks.as_view(), name="tasks"),
    path('addCategories/', views.addCategories.as_view(), name="categories"),
    path('newTask/', views.NewTask.as_view(), name="newTask"),
    path('editAndDelete/', views.editAndDelete.as_view(), name="editAndDelete"),
    path('cats/', views.CatList.as_view(), name="cat-list"),
]