from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # 여기를 이렇게 수정!
    path('', include('main.urls')),  # 메인페이지 루트에 매핑


]