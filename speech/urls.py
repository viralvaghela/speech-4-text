
from django.contrib import admin
from django.urls import path, include

from speech import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('submitpoint', views.submitpoint, name='submitpoint'),
    path('practice', views.practice, name='practice'),
    path('logout', views.logout, name='logout')

]
