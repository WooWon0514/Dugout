# accounts/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'  # 이 줄 꼭 추가!

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('signup/', views.signup_view, name='signup'),
]