from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="home"),
    path("signup", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", views.signuot, name="logout"),
    path("tasks/", views.tasks, name="tasks"),
    path("tasks/create/", views.create_task, name="create_task"),
    path("tasks/<int:id>/", views.detail_task, name="detail_task"),
    path("tasks/done/<int:id>", views.done_task, name="done_task"),
    path("tasks/delete/<int:id>", views.delete_task, name="delete_task"),
    path("tasks/edit/<int:id>", views.edit_task, name="edit_task"),
]
