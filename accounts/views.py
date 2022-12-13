from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    in_results = In.objects.all()
    out_results = Out.objects.all()

    context = {'in_results':in_results, 'out_results':out_results}

    return render(request, 'home.html', context)

def login(request):
    return render(request, 'login.html')

# def get_in(request):
#     in_results = In.objects.all()

#     return render(request, './templates/accounts/home.html', {'in_results':in_results})