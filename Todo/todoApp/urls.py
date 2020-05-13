from django.urls import path
from todoApp.views import *
from . import views

urlpatterns = [

    path('', TodoListView.as_view(),name='index'),
    path('add/',TodoAdd.as_view(),name='todoAdd'),
    path('delete/<int:pk>',views.TodoDeleteView.as_view(),name='delete'),
    path('detail/<int:pk>/', views.TodoDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', views.TodoUpdate.as_view(), name='todo-edit'),
    
    path('completed/<todo_id>', views.TodoComplete, name='complete'),
    path('delComplete/',views.deleteCompleted,name='completed-delete'),

    path('accounts/register/', views.registerPage, name="register"),
	path('accounts/login/', views.loginPage, name="login"),  
	path('logout/',views.logoutUser, name ="logout"),

]
