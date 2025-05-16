from django.contrib import admin

# Register your models here.
from .models import ListOfCaddies,  EndUsers, TeeTime, Caddie, Field
admin.site.register(ListOfCaddies)
admin.site.register(TeeTime)
admin.site.register(EndUsers)
admin.site.register(Caddie)
admin.site.register(Field)
