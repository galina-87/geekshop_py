from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from authapp.forms import ShopAuthenticationForm, ShopRegisterForm, ShopUserProfileForm


def login(request):
    form = None
    redirect_url = request.GET.get('next', None)

    if request.method == "POST":
        form = ShopAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                redirect_url = request.POST.get('redirect_url', None)
                auth.login(request, user)
                if redirect_url:
                    return HttpResponseRedirect(redirect_url)
                return HttpResponseRedirect(reverse('main:index'))
    elif request.method == "GET":
        form = ShopAuthenticationForm()

    context = {
        'title_page': 'аутентификация',
        'form': form,
        'redirect_url': redirect_url,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def user_register(request):
    register_form = None
    if request.method == 'POST':
        register_form = ShopRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    elif request.method == 'GET':
        register_form = ShopRegisterForm()

    context = {
        'title_page': 'регистрация',
        'register_form': register_form
    }
    return render(request, 'authapp/user_register.html', context)


def user_profile(request):
    form = ShopUserProfileForm()

    if request.method == 'POST':
        form = ShopUserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:user_profile'))
    else:
        form = ShopUserProfileForm(instance=request.user)

    context = {
        'title_page': 'Профиль',
        'form': form
    }
    return render(request, 'authapp/user_profile.html', context)



