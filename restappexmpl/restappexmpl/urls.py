from django.urls import path
from .views import users, user, tasks, delete_task

urlpatterns = [
    path("users/", users),
    path("users/<int:user_id>", user),
    path("users/<int:user_id>/tasks/", tasks),
    path("users/<int:user_id>/tasks/<int:task_id>", delete_task)
]

