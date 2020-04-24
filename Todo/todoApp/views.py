from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import CreateView, DetailView,ListView
from django.urls import reverse_lazy
from .forms import *
from .models import *

class TodoListView(ListView):
    model = Todo
    template_name = 'todoApp/index.html'
    queryset = Todo.objects.all()
    context_object_name = 'todo_list'

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

def TodoComplete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def TodoDelete(request, todo_id):
    todo= get_object_or_404(Todo, pk=todo_id)  
    template_name = 'todoApp/delete.html'
    if request.method=='POST':
        todo.delete()
        return redirect('index')

    return render(request, template_name, {'object':todo})
