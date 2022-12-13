from django.contrib import admin

# Register your models here.

from .models import In, Out

admin.site.register(In)
admin.site.register(Out)