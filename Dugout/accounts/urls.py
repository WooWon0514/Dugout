# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'  # 이 줄 꼭 추가!

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]