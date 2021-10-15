# app/accounts/urls.py

# Django modules
from django.urls import path

# Locals
from app.accounts.views import register_view, login_view

# Appname
app_name = 'accounts'

urlpatterns = [
    path('accounts/register/', register_view, name='register'),
    path('accounts/login/', login_view, name='login'),
]
