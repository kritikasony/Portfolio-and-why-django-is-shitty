from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def home(request):
    return render(request, 'index.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def stories(request):
    return render(request, 'stories.html', {})

def projects(request):
    return render(request, 'myprojects.html', {})
