from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # post views
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    ]