from django.contrib import admin
from django.urls import path, include
from .views import ListUsers, CustomAuthToken, User_logout, UpdateProfileView
from . import views

from .views import ChangePasswordView

urlpatterns = [
    path('users/', ListUsers.as_view()),
    path('register/', views.register),
    path('login/', CustomAuthToken.as_view()),
#     path('user_login/', views.token_login),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('change_password/',
         ChangePasswordView.as_view(), name='change-password'),
    path('update_profile/', UpdateProfileView.as_view(),
         name='auth_update_profile'),
    path('logout/', User_logout),


]
