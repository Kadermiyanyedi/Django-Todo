from django.shortcuts import redirect, reverse
from django.views.generic import CreateView, DetailView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *
from .models import *
from .decorators import *


@method_decorator(login_required, name='dispatch')
class TodoListView(ListView):
    model = Todo
    template_name = 'todoApp/index.html'
    queryset = Todo.objects.all()


@method_decorator(login_required, name='dispatch')
class TodoDetailView(DetailView):
	model=Todo
	login_required = True
	template_name = 'todoApp/detail.html'


@method_decorator(login_required, name='dispatch')
class TodoAdd(CreateView):
    model = Todo
    form_class = TodoModelForm
    success_url = reverse_lazy('index')
    template_name = 'todoApp/add.html'

    def form_valid(self, form):
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class TodoUpdate(UpdateView):
    model = Todo
    fields = ['title', 'details']
    template_name = 'todoApp/edit.html'
    success_url = reverse_lazy('index')


@method_decorator(login_required, name='dispatch')
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todoApp/delete.html'
    success_url = reverse_lazy('index')


@login_required(login_url='login')
def TodoComplete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')


@login_required(login_url='login')
def deleteCompleted(request):
    Todo.objects.filter(completed=True).delete()
    return redirect('index')


@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)
			return redirect('login')
			

	context = {'form':form}
	return render(request, 'user/register.html', context)


@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'user/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')


