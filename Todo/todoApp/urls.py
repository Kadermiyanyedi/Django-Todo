from django.urls import path
from todoApp.views import *
from . import views

urlpatterns = [

    path('', TodoListView.as_view(), name='index'),
    path('add/',TodoAdd.as_view(),name='todoAdd'),
    path('completed/<todo_id>', views.TodoComplete, name='complete'),
    path('delete/<todo_id>',views.TodoDelete,name='delete'),
    path('todo/<todo_id>/', views.DetailView.as_view(), name='detail'),

]
