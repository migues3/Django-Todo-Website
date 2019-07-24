from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    text = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.text

