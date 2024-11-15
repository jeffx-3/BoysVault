from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('feed/', views.feed, name="feed"),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
]