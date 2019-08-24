from django.contrib import admin
from .models import Todo, Contact, Category

# Register your models here.
admin.site.register(Todo)
admin.site.register(Contact)
admin.site.register(Category)