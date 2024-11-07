from django.urls import path,include
from . import views

app_name= "base"
urlpatterns = [
    path('', views.home),
    path('feed/', views.feed, name="feed"),
    path('signup/', views.authView, name="authView"),
    path('accounts/', include('django.contrib.auth.urls')),
]
