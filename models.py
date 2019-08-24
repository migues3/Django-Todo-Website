from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    # The user who this contact belongs to
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.first_name + self.last_name
    
    def get_email(self):
        return self.email

# Users will be able to place their task to a specific category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Todo(models.Model):
    text = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.text
        return self.text

