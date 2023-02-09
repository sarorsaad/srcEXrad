from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

from django.views import View 

def create_account_view(request):
  return render(request, 'account/create_account.html')

def register_submit(request):
    if request.method == 'POST':
        # Access form data and process it
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Create a new user object
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Assign user to admin or user group
            if form.cleaned_data['is_admin']:
                user.is_staff = True
            user.save()
            # Redirect to another page
            return redirect('account/register_success/')
    else:
        form = RegisterForm()
    return render(request, 'account/create_account.html', {'form': form})



class LoginAdminView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'account/admin_login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        return render(request, 'account/admin_login.html', {'form': form})


class LoginUserView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'account/user_login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'account/user_login.html', {'form': form})

def register_success(request):
    return render(request, 'account/register_success.html')