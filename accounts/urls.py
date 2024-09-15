#accounts\urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import RegisterView, LoginView, LogoutView,ProfileView
from django.contrib.auth.forms import PasswordResetForm

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]