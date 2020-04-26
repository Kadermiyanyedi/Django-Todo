from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, DetailView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import *
from .models import *

class TodoListView(ListView):
    model = Todo
    template_name = 'todoApp/index.html'
    queryset = Todo.objects.all()


class TodoDetailView(DetailView):
	model=Todo
	template_name = 'todoApp/detail.html'

    
class TodoAdd(CreateView):
    model = Todo
    form_class = TodoModelForm
    success_url = reverse_lazy('index')
    template_name = 'todoApp/add.html'

    def form_valid(self, form):
        return super().form_valid(form)

class TodoUpdate(UpdateView):
    model = Todo
    fields = ['title', 'details']
    template_name = 'todoApp/edit.html'
    success_url = reverse_lazy('index')


def TodoComplete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todoApp/delete.html'
    success_url = reverse_lazy('index')
