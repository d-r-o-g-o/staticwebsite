from django.contrib import admin

# Register your models here.
from .  models import Place
from . models import Names
admin.site.register(Place)
admin.site.register(Names)