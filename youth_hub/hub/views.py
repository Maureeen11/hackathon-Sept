from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, ProjectForm
from .models import Project, Mentor

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'hub/register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'hub/login.html', {'error': 'Invalid credentials'})
        login(request, user)
        return redirect('dashboard')
    return render(request, 'hub/login.html')

# Project Submission View
def submit_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.status = 'submitted'
            project.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'hub/submit_project.html', {'form': form})

# Dashboard View
def dashboard(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'hub/dashboard.html', {'projects': projects})
