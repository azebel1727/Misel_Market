from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('src.urls')), # This tells Django to use your src/urls.py
]