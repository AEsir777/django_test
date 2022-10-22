from django.urls import path

from . import views

urlpatterns = [
    path('app', views.get_request),
    path('app/authorize', views.authorize)
]
