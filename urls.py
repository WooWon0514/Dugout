from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # 여기를 이렇게 수정!
    path('kbo/', include('kbo.urls')),
]