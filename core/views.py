from django.shortcuts import render
from .models import ListOfCaddies
# Create your views here.
def landing_page(request):
    return render(request, "core/landing.html")