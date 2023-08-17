from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Out)


@admin.register(In)
class InAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        # Handle related instances before deleting
        # For example, you can delete related 'In' instances before deleting the user
        related_ins = In.objects.filter(user_in=obj)
        related_ins.delete()

        # Continue with user deletion
        super().delete_model(request, obj)
