from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def your_signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('index')  # Redirect to the index page
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
