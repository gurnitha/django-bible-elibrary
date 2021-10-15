# core/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('', include('app.accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
]
