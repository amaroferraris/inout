from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import InForm, OutForm
# Create your views here.

def home(request):
    in_results = In.objects.all()
    out_results = Out.objects.all()


    amountIn = []
    for amount in in_results:
        amount_in = amount
        amountIn.append(amount_in.amount)

    totalIn = sum(amountIn)



    amountOut = []
    for amount in out_results:
        amount_out = amount
        amountOut.append(amount_out.amount)

    totalOut = sum(amountOut)

    print(In.objects.all())

    total = totalIn - totalOut



    context = {'in_results':in_results, 'out_results':out_results, 'total':total}
    return render(request, 'home.html', context)




# CREATE

def createIn(request):

    form = InForm()
    if request.method == 'POST':
        form = InForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}

    return render(request, 'in_form.html', context)


def createOut(request):

    form = OutForm()
    if request.method == 'POST':
        form = OutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request, 'out_form.html', context)




# UPDATE

def updateIn(request, pk):

    get_in = In.objects.get(id=pk)
    form = InForm(instance=get_in)

    if request.method == 'POST':
        form = InForm(request.POST, instance=get_in)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'in_form.html', context)


def updateOut(request, pk):

    get_out = Out.objects.get(id=pk)
    form = OutForm(instance=get_out)

    if request.method == 'POST':
        form = OutForm(request.POST, instance=get_out)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'out_form.html', context)




# DELETE

def deleteIn(request, pk):

    get_in = In.objects.get(id=pk)
    if request.method == 'POST':
        get_in.delete()
        return redirect('/')

    context = {'item':get_in}
    return render(request, 'delete_in.html', context)


def deleteOut(request, pk):

    get_out = Out.objects.get(id=pk)
    if request.method == 'POST':
        get_out.delete()
        return redirect('/')
        
    context = {'item':get_out}
    return render(request, 'delete_out.html', context)

# https://youtu.be/EX6Tt-ZW0so?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&t=731