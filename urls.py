from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.add, name = "add"),
    path('complete/<todo_id>', views.complete, name = 'complete'),
    path('contacts', views.contacts, name='contacts'),
    path('editcontacts', views.editcontacts, name='editcontacts'),
    path('deletecontact/<contact_id>', views.deletecontact, name='deletecontact'),
    path('login', auth_views.LoginView.as_view(template_name="main/login.html"), name = "login"),
    path('logout', auth_views.LogoutView.as_view(template_name="main/logout.html"), name = "logout"),
    path('register', views.register, name = "register"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'main/password_reset.html'),
         name = 'password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name = 'main/password_reset_done.html'),
         name = 'password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name = 'main/password_reset_confirm.html'),
         name = 'password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name = 'main/password_reset_complete.html'),
         name = 'password_reset_complete'),
]