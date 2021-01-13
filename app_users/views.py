from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app_products.forms import ProductSearchForm
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
            messages.success(
                request, 'Un nouveau compte vient d\'être créé pour ' + user
            )
            return redirect('loginPage')
    context = {'search_form': ProductSearchForm(), 'form': form}

    return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('indexPage')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        next_url = request.GET.get('next', '/')
        if user is not None:
            login(request, user)
            if next_url != '/':
                return redirect(next_url)
            return redirect('profilePage')
        else:
            messages.error(
                request, 'Nom d\'utilisateur OU mot de passe incorrect'
            )
    context = {'search_form': ProductSearchForm()}
    return render(request, 'login.html', context)


@login_required()
def logoutCurrentUser(request):
    logout(request)
    return redirect('indexPage')


@login_required()
def profile(request):
    context = {'search_form': ProductSearchForm()}
    return render(request, 'profile.html', context)
