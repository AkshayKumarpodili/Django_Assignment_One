from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('hello',views.fun),
    path('url/task',views.task_page)
]