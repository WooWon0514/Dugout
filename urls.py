from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # 여기를 이렇게 수정!
    path('teams/', include('teams.urls')),
    path('players/', include('players.urls')),
]