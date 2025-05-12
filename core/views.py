from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, "core/landing.html")

def personal_profile_page(request):
    return render (request, "core/person.html")