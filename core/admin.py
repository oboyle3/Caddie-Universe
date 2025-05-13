from django.contrib import admin

# Register your models here.
from .models import ListOfCaddies,  EndUsers
admin.site.register(ListOfCaddies)
#admin.site.register(TeeTimes)
admin.site.register(EndUsers)