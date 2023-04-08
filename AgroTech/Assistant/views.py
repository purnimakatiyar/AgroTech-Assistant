from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def landing_page(request):
    return render(request, 'landing_page.html')
def supplier_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('supplier_dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
    
    # If GET request or authentication failed, show login form
    return render(request, 'supplier_login.html', {'form': UserCreationForm()})

def supplier_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in automatically after registration
            login(request, user)
            messages.success(request, 'Your account has been created successfully')
            return redirect('supplier_dashboard')
    else:
        form = UserCreationForm()
    
    return render(request, 'supplier_register.html', {'form': form})

def supplier_dashboard(request):
    return render(request, 'supplier_dashboard.html')