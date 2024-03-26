from django.urls import path
from . import views
from .views import register, user_login, password_reset

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('password_reset/', password_reset, name='password_reset'),
    path('dashboard/', views.dashboard, name='dashboard')
]
