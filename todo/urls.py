from django.urls import path
from todo.views import TaskListView, SignupView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("signup/", SignupView.as_view(), name="signup"),
]
