from django.forms import ModelForm
from .models import *


class InForm(ModelForm):
    class Meta:
        model = In
        fields = ['amount', 'description', 'category']



class OutForm(ModelForm):
    class Meta:
        model = Out
        fields = ['amount', 'description', 'category']