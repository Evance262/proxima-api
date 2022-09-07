"""proxima_api URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from core.views import CardView

urlpatterns = [
    path('api-auth/',
         include('rest_framework.urls',)),
    path('admin/', admin.site.urls),
    path('', CardView.as_view(), name='test')
]
