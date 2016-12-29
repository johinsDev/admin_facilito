from django.shortcuts import render
from django.shortcuts import redirect


from django.contrib.auth import authenticate
from django.contrib.auth import login as loginDjango
from django.contrib.auth import logout as logoutDjango
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .forms import LoginForm , RegisterForm


def show(request):
    pass


def login(request):
    if request.user.is_authenticated():
        return redirect('clients:dashboard')

    message = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            loginDjango(request, user)
            return redirect('clients:dashboard')
        else:
            message = "Username o password incorrectos."
    form = LoginForm()

    context = {
        'form': form,
        'message': message
    }
    return render(request, 'login.html', context)


@login_required(login_url='clients:login')
def dashboard(request):
    return render(request, 'dashboard.html', {})


@login_required(login_url='clients:login')
def logout(request):
    logoutDjango(request)
    return redirect('clients:login')


def create(request):

    if request.user.is_authenticated():
        return redirect('clients:dashboard')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            return redirect('clients:dashboard')

    return render(request, 'register.html', {'form': form})
