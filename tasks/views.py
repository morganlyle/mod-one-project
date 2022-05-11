# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from tasks.models import Task

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]
    successful_url = reverse_lazy("home")
