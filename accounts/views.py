from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from accounts.forms import FluentRegistrationForm

# Create your views here.

def login_view(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('accounts/login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def loggedin_view(request):
    return render_to_response('accounts/loggedin.html',
                              {'full_name': request.user.username})

def invalid_view(request):
    return render_to_response('accounts/invalid.html')

def logout_view(request):
    logout(request)
    return render_to_response('accounts/logout.html')

def register_user(request):
    if request.method == 'POST':
        form = FluentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = FluentRegistrationForm()
    print args
    return render_to_response('accounts/register.html', args)


def register_success(request):
    return render_to_response('accounts/register_success.html')