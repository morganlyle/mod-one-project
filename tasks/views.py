# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from tasks.models import Task

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self):
        return reverse("show_project", args=[self.object.project.id])


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/mine.html"
    context_object_name = "show_my_tasks"
    successful_url = reverse_lazy("home")

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)
