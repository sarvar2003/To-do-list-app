from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User

from .models import Task

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'all_tasks'
    login_url = 'login'
    

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'new_task.html'
    fields = ['title', 'task']
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Task
    template_name = 'update_task.html'
    fields = ['title', 'task']
    success_url = reverse_lazy('task_list')
    login_url = 'login'

    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# Create your views here.
