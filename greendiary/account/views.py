from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth
from .models import Profile

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect("diary:home")

    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            Profile.objects.create(user=user)
            auth.login(request, user)
            return redirect("diary:home")
        
    else :
        signup_form = UserCreationForm()

    return render(request, 'account/signup.html', {'signup_form':signup_form})

def login(request):
    if request.user.is_authenticated:
        return redirect("diary:home")

    if request.method == "POST":
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth.login(request, login_form.get_user())
        return redirect("diary:home")
        
    else:
        login_form = AuthenticationForm()
        
    return render(request, 'account/login.html', {'login_form':login_form})

def logout(request):
    auth.logout(request)
    return redirect("diary:home")