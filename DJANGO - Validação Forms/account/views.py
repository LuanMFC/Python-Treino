from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def register(request):
    if request.method == "POST":
        register_user = UserCreationForm(request.POST)
        if register_user.is_valid():
            register_user.save()
            return redirect("list_cars")
    
    else:
        register_user = UserCreationForm()

    return render(
        request,
        "register.html",
        {"register_user": register_user},	
    )

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("list_cars")
        else:
            user = AuthenticationForm()
        
    else:
        user = AuthenticationForm()
    return render(
        request, 
        "login.html",
        {"user": user}
    )

def user_logout(request):
    logout(request)
    return redirect("list_cars")