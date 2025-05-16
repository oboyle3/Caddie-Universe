# core/urls.py
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('profile/', views.personal_profile, name='personal_profile'),


    
]


# from django.contrib import admin
# from django.urls import path
# from app.views import index
# from app import views
# from app.views import PlayerListAPIView

# urlpatterns = [
#     path('admin/', admin.site.urls),