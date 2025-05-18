from django.db import IntegrityError
from django.shortcuts import redirect, render
from .models import Caddie, Field, Assignment, PlayerScore

def landing_page(request):
    playerscores = PlayerScore.objects.all()
    return render(request, "core/landing.html", {
        'playerscores': playerscores  # This makes it available in the template
    })
def booking(request):
    return render(request, "core/booking.html", {
        
    })
def personal_profile(request):
    caddies = Caddie.objects.all()
    fields = Field.objects.all()
    assignments = Assignment.objects.all()

    if request.method == 'POST':
        if 'caddiename' in request.POST:
            caddiename = request.POST.get('caddiename')
            if caddiename:
                Caddie.objects.create(name=caddiename)
            return redirect('personal_profile')

        elif 'fieldname' in request.POST:
            fieldname = request.POST.get('fieldname')
            if fieldname:
                Field.objects.create(name=fieldname)
            return redirect('personal_profile')

        elif 'assign' in request.POST:
            caddie_id = request.POST.get('caddie_id')
            field_id = request.POST.get('field_id')
            try:
                caddie = Caddie.objects.get(id=caddie_id)
                field = Field.objects.get(id=field_id)
                Assignment.objects.create(caddie=caddie, field=field)
            except (Caddie.DoesNotExist, Field.DoesNotExist):
                pass
            except IntegrityError:
                pass
            return redirect('personal_profile')

    return render(request, 'core/personal_user_page.html', {
        'caddies': caddies,
        'fields': fields,
        'assignments': assignments,
    })
