from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import PersonalUserCreationForm

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('indexPage')
    form = PersonalUserCreationForm()
    if request.method == 'POST':
        form = PersonalUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Un nouveau compte viens d\'etre créé pour ' + user )
            return redirect('loginPage')
    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('indexPage')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('indexPage')
        else:
            messages.info(request, 'Nom d\'utilisateur OU mot de passe incorrect')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='loginPage')
def logoutCurrentUser(request):
    if request.user.is_anonymous:
        return redirect('indexPage')
    logout(request)
    return redirect('indexPage')
