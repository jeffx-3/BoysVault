from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

#home view

def home(request):
    return render(request, 'index.html')

#feed view
@login_required
def feed(request):
    return render(request, 'feed.html')

#authView
def authView(request):
    if request.method == "POST":
        form= UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {"form" :form})