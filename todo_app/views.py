from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm

# List view - show all tasks
class TaskListView(ListView):
    model = Task
    template_name = 'todo_app/task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        # Order by created date (newest first)
        return Task.objects.order_by('-created_at')

# Detail view - show single task
class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo_app/task_detail.html'
    context_object_name = 'task'

# Create view - add new task
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo_app/task_form.html'
    success_url = reverse_lazy('task-list')

# Update view - edit task
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo_app/task_form.html'
    success_url = reverse_lazy('task-list')

# Delete view - remove task
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo_app/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
    context_object_name = 'task'

# Toggle completion status
def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task-list')
