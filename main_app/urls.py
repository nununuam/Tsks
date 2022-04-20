from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('tasks/', views.Tasks.as_view(), name="tasks"),
    path('addCategories/', views.addCategories.as_view(), name="categories"),
    path('SumerBal/', views.SumerBal.as_view(), name="SumerBal"),
]