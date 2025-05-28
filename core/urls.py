# core/urls.py
from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('profile/', views.personal_profile, name='personal_profile'),
    path('booking/', views.booking, name='booking'),
    path('assign/<int:timeslot_id>/', views.assign_timeslot, name='assign_timeslot'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name= 'dashboard'),
    path('basic_encrypt1/', views.dashboard, name= 'basic_encrypt1'),
]
