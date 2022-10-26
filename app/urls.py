from django.urls import path

from . import views

urlpatterns = [
    path('', views.AppView.as_view(), name = 'welcome_page'),
    path('app/authorize', views.AuthorizedView.as_view(), name = 'useless'),
    path('login', views.AppLoginView.as_view(), name = 'login'),
    path('logout', views.AppLogoutView.as_view(), name = 'logout'),
    path('signup', views.SignupView.as_view(), name='signup')
]
