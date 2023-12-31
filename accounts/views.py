from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User

# Create your views here.
from .models import *
from .forms import InForm, OutForm, CreateUserForm
from .decorators import *

from django.views.decorators.clickjacking import xframe_options_exempt


# ADMIN PAGE
@admin_only
@login_required(login_url='login')
def adminPage(request):
    return render(request, 'admin')



# REGISTER
@unauthenticated_user
def registerUser(request):

    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name="users")
            user.groups.add(group)
            User.objects.create()

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')


    context = {'form':form}
    return render(request, 'register.html', context)


# LOGIN
@unauthenticated_user
def loginUser(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # group = User.objects.all()
            # for g in group:
            #     print(g.groups.all())

            # if request.user.groups == 'admin':
            #     print('hello admin')
            #     return redirect('home')
            # else:
            #     print('hello user')
            return redirect('user')
        else:
            messages.info(request, 'Username OR password is incorrect!')

    context = {}
    return render(request, 'login.html', context)



# LOGOUT
def logoutUser(request):
    logout(request)
    return redirect('login')



# HOME
@admin_only
@login_required(login_url='login')
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

    total = totalIn - totalOut



    context = {'in_results':in_results, 'out_results':out_results, 'total':total}
    return render(request, 'home.html', context)




# CREATE
@login_required(login_url='login')
def createIn(request):

    if request.method == 'POST':
        form = InForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_in = request.user
            instance.save()
            print("Creating in...")
            return redirect('/')
        
    else:
        form = InForm()

    return render(request, 'in_form.html', {'form':form})


@login_required(login_url='login')
def createOut(request):

    if request.method == 'POST':
        form = OutForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_out = request.user
            instance.save()
            return redirect('/')
        
    else:
        form = OutForm()

    return render(request, 'out_form.html', {'form':form})


# UPDATE
@login_required(login_url='login')
# @xframe_options_exempt
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


@login_required(login_url='login')
def updateOut(request, pk):

    get_out = Out.objects.get(id=pk)
    form = OutForm(instance=get_out)

    if request.method == 'POST':
        form = OutForm(request.POST, instance=get_out)
        if form.is_valid():
            form.save()
        print(request.POST)
        return redirect('/')

    context = {'form':form}
    return render(request, 'out_form.html', context)


# DELETE
@login_required(login_url='login')
def deleteIn(request, pk):

    get_in = In.objects.get(id=pk)
    if request.method == 'POST':
        get_in.delete()
        return redirect('/')

    context = {'item':get_in}
    return render(request, 'delete_in.html', context)

@login_required(login_url='login')
def deleteOut(request, pk):

    get_out = Out.objects.get(id=pk)
    print(get_out)
    if request.method == 'POST':
        get_out.delete()
        return redirect('/')
        
    context = {'item':get_out}
    return render(request, 'delete_out.html', context)




# USER
@login_required(login_url='login')
def userPage(request
            #  , pk
             ):

    # inOut

    in_results = request.user.in_set.all()
    out_results = request.user.out_set.all()

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

    total = totalIn - totalOut

    # saracatunga = in_results.id


    # # Update FORMS

    #     # IN

    # get_in = In.objects.get(id=pk)
    # in_form = InForm(instance=get_in)

    # if request.method == 'POST':
    #     in_form = InForm(request.POST, instance=get_in)
    #     if in_form.is_valid():
    #         in_form.save()
    #         return redirect('/')

    #     # OUT
    
    # get_out = Out.objects.get(id=pk)
    # out_form = OutForm(instance=get_out)

    # if request.method == 'POST':
    #     out_form = OutForm(request.POST, instance=get_out)
    #     if out_form.is_valid():
    #         out_form.save()
    #         return redirect('/')+

    context = {'in_results':in_results, 'out_results':out_results, 'total':total, 
            #    'saracatunga':saracatunga
            #    'in_form':in_form, 'out_form': out_form,
               }
    return render(request, 'user.html', context)