from django.urls import path
from . import views

urlpatterns = [
    path('app2', views.list_files),
]