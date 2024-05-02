from django.urls import path
from webapp import views
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('items/', views.items, name='items'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
]