"""
urls的配置
"""
from django.urls import path

from .views.loginview import LoginView
from .views.logoutview import LogoutView

app_name = 'admin'
urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]