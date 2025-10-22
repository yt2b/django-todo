from django.urls import path
from todo.views import TaskListView, TaskToggleView, TaskDeleteView, SignupView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("toggle/<int:id>", TaskToggleView.as_view(), name="toggle"),
    path("delete/<int:id>", TaskDeleteView.as_view(), name="delete"),
]
