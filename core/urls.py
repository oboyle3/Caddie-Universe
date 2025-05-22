# core/urls.py
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('profile/', views.personal_profile, name='personal_profile'),
    path('booking/', views.booking, name='booking'),
    path('assign/<int:timeslot_id>/', views.assign_timeslot, name='assign_timeslot'),
]
