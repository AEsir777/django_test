from django.urls import path
from . import views

urlpatterns = [
    path('app2', views.App2ListView.as_view(), name = "file.list"),
    path('app2/<int:pk>', views.App2DetailView.as_view(), name="detail"),
    path('app2/upload', views.App2CreateView.as_view(), name = "upload.file")
]