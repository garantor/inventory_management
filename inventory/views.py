from django.shortcuts import render, redirect
from .models import *
from.forms import *
# Create your views here.


def index(requests):
    return render(requests, 'index.html')

def display_laptops(requests):
    items = Laptop.objects.all()
    context = {
        'items': items,
        'header': 'Laptops',
    }
    return render(requests, 'index.html', context)

def display_desktops(requests):
    items = Desktop.objects.all()
    context = {
        'items': items,
        'header': 'Desktops',
    }
    return render(requests, 'index.html', context)

def display_mobiles(requests):
    items = Mobile.objects.all()
    context = {
        'items': items,
        'header': 'Mobiles',
    }
    return render(requests, 'index.html', context)


def add_device(request, cls):
    if request.method == 'POST':
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')



    else:
        form = cls
        return render(request, 'add_new.html', {'form':form})


def add_desktop(request):
    return add_device(request, DesktopForm)


def add_laptop(request):
    return add_device(request, LaptopForm)


def add_mobile(request):
    return add_device(request, MobileForm)