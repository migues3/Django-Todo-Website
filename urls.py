from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add, name = "add"),
    path('complete/<todo_id>', views.complete, name = 'complete'),
    path('deletecompleted', views.deletecompleted, name = 'deletecompleted'),
    path('deleteall', views.deleteall, name = "deleteall"),
    path('login', auth_views.LoginView.as_view(template_name="main/login.html"), name = "login"),
    path('logout', auth_views.LogoutView.as_view(template_name="main/logout.html"), name = "logout"),
    path('register', views.register, name = "register"),
]