"""
urls的配置
"""
from django.urls import path

from .views.loginview import LoginView
from .views.logoutview import LogoutView
from .views.registerview import RegisterView

app_name = 'admin'
urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
]
