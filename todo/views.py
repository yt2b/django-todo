from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect

from todo.models import Task


class TaskListView(LoginRequiredMixin, TemplateView):
    template_name = "todo/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        if title:
            Task.objects.create(user=request.user, title=title)
        return redirect("index")


class TaskToggleView(View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs["id"])
        task.completed = not task.completed
        task.save()
        return redirect("index")


class TaskDeleteView(View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs["id"])
        task.delete()
        return redirect("index")


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response
