from django.contrib import admin
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about' ),
    path('login/',views.login_user, name='login' ),
    path('register/',views.register, name='register'),
    path('start/',views.start, name='start'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('choose_plan/1/planfree.html/', views.plan_free, name='plan'),
    path('choose_plan/<int:plan_id>/', views.choose_plan, name='choose_plan'),
    
]
