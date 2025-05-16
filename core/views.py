from django.shortcuts import redirect, render
from .models import ListOfCaddies, Caddie, Field
# Create your views here.
def landing_page(request):
    return render(request, "core/landing.html")

def personal_profile(request):
    #get the caddies and failds from the database
    caddies = Caddie.objects.all()
    fields = Field.objects.all()
    #check if the form was submitted (posst request)
    if request.method == 'POST':
        #get the name value from the submitted form
        caddiename = request.POST.get('caddiename')
        #get fieldname value from the submtted form
        fieldname = request.POST.get('fieldname')
        if caddiename:
            #create and save a new Caddie object
            Caddie.objects.create(name=caddiename)
            # redirect to the same page
            return redirect('personal_profile')
        if fieldname:
            #create and same a new Field object
            Field.objects.create(name=fieldname)
            # redirect to same page
            return redirect('personal_profile')
           
    return render(request, 'core/personal_user_page.html', {
        'caddies': caddies,
        'fields': fields
    })