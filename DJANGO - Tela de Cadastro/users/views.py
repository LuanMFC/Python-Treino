from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def new_user(request):

    print(request)
    if request.method == 'POST':
        new_users = UserCreationForm(request.POST)
        if new_users.is_valid():
            new_users.save()
            return redirect("user_login")
        
    else:
        new_users = UserCreationForm()
    
    return render(
        request, 
        'new_user.html', 
        {'new_users': new_users}
    )


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            user = AuthenticationForm()
    else:
        user = AuthenticationForm()
    return render(
        request, 
        'login.html',
        {'user': user}
)

def user_logout(request):
    logout(request)
    return redirect(
        'user_login'
    )