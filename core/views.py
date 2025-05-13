from django.shortcuts import render
from .models import ListOfCaddies
# Create your views here.
def landing_page(request):
    return render(request, "core/landing.html")



def personal_profile_page(request):
    caddies = ListOfCaddies.objects.all()
    return render(request, "core/personal_user_page.html", {"caddies": caddies})
