from django.db import models


class User(models.Model):
    api_key = models.CharField(max_length=32)
    username = models.CharField(max_length=32, unique=True)
    description = models.TextField()


class Task(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    start_time = models.DateTimeField()
    deadline = models.DateTimeField()