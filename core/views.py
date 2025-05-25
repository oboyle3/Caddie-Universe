from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from .models import Booking, Caddie, EndUsers, Field, Assignment, PlayerScore, schedule
from django.contrib.auth.decorators import login_required

def landing_page(request):
    playerscores = PlayerScore.objects.all()
    return render(request, "core/landing.html", {
        'playerscores': playerscores  # This makes it available in the template
    })
def booking(request):
    schedule_list = schedule.objects.all()
    bookings = Booking.objects.select_related('user', 'timeslot').all()
    return render(request, "core/booking.html", {
        'schedule' : schedule_list,
        'bookings': bookings,
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



def assign_timeslot(request, timeslot_id):
    timeslot = get_object_or_404(schedule, id=timeslot_id)
    users = EndUsers.objects.all()

    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user = get_object_or_404(EndUsers, id=user_id)
        Booking.objects.create(user=user, timeslot=timeslot)
        return redirect('booking')  # or redirect to a success page

    return render(request, "core/assign.html", {
        "timeslot": timeslot,
        "users": users,
    })

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html', {
        'user': request.user
    })