from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import LicenceForm, RegisterForm
from .models import Licence_Data
from django.contrib.auth.models import User

# Create home_view here.
@login_required
def home_view(request):
    return render(request, 'licence_home/home.html')

# Create register_view here.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user_type = form.cleaned_data.get("user_type")
            user = User.objects.create_user(username=username, password=password, user_type=user_type)
            login(request, user)
            return redirect('home') 
    else:
        form= RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

# Create login_view here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
    else:
        error_message = "Invalid Credentials!"
    return render(request, 'accounts/login.html', {'error_message':error_message})

#Create logout_view here.
def logout_view(request):
    if request.method =="POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')

#Create Protected_view here.
'''class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    #'next' - to redirect URL
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'licence_home/user_form.html')
'''

#Create create_user_view
def user_create_view(request):
    if request.method == 'POST':
        form = LicenceForm(request.POST, request.FILES)
        if form.is_valid():
            resourse = form.save(commit=False)
            resourse.user = request.user
            resourse.save()
            return redirect('user_list')
    else:
        form= LicenceForm()
    return render(request, 'licence_home/user_form.html', {'form': form})

# Create user_view here.
def user_view(request):
    Users = Licence_Data.objects.all()
    return render(request, 'licence_home/user_list.html', {'Users':Users})

# Create update_view here.
def update_view(request, id):
    User = Licence_Data.objects.get(id=id)
    form=LicenceForm()
    if request.method == 'POST':
        form=LicenceForm(request.POST, instance=User) 
        if form.is_valid():
            form.save()
            return redirect('user_list')
    return render(request, 'licence_home/user_form.html', {'form': form}) 

# Create delete_view here.
def delete_view(request, id):
    User = Licence_Data.objects.get(id=id)
    if request.method == 'POST':
        User.delete()
        return redirect('user_list')
    return render(request, 'licence_home/user_confirm_delete.html', {'User': User})
