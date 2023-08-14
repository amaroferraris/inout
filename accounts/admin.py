from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(In)
admin.site.register(Out)