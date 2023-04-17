"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import TaskCreate,ShowTask,TaskUpdate,TaskDelete
urlpatterns=[
   
    path('taskcreate/',TaskCreate.as_view(),name='task'),
    # path('tasklist/',ShowTask.as_view(),name='tasklist'),
    path('todo_list',views.todolist,name='todo_list'),
    path('todolist',ShowTask.as_view(),name='todo_list'),
    path('todo_update/<int:pk>/', TaskUpdate.as_view(), name='todo_update'),
    path('todo_delete/<int:pk>',TaskDelete.as_view(),name='todo_delete'),
    ]
   