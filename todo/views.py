from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class TaskListView(LoginRequiredMixin, TemplateView):
    template_name = "todo/index.html"
