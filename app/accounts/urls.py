# app/accounts/urls.py

# Django modules
from django.urls import path

# Locals
from app.accounts.views import register_view

# Appname
app_name = 'accounts'

urlpatterns = [
    path('register/', register_view, name='register'),
]
