from django.shortcuts import render,redirect
from .models import Window,Door,Fire_door,Dym_door,Patio,Sl,Fasad,Ms,Windowsill,Otliv
from .forms import OrderForm
from django.http import HttpResponse
from . import models
from django.utils.translation import gettext as _


def products_home(request):
    return render(request, 'products/products_home.html')


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form = models.Order.objects.create(**form.cleaned_data)
            return redirect('/')
        else:
            return HttpResponse(_('Invalid form'))
    else:
        form = OrderForm()
        context = {'form': form}
        return render(request, 'products/callback.html', context)


def window(request):
    windows = Window.objects.all()
    return render(request, 'products/window.html', {'windows': windows})


def doors(request):
    door = Door.objects.all()
    return render(request, 'products/doors.html', {'door': door})


def fire_door(request):
    firedoor = Fire_door.objects.all()
    return render(request, 'products/fire_door.html', {'firedoor': firedoor})


def dym_door(request):
    dymdoor = Dym_door.objects.all()
    return render(request, 'products/dym_door.html', {'dymdoor': dymdoor})


def patio(request):
    patiodoor = Patio.objects.all()
    return render(request, 'products/patio.html', {'patiodoor': patiodoor})


def sl(request):
    sldoor = Sl.objects.all()
    return render(request, 'products/sl.html', {'sldoor': sldoor})


def fasad(request):
    f50 = Fasad.objects.all()
    return render(request, 'products/fasad.html', {'f50': f50})


def ms(request):
    mss = Ms.objects.all()
    return render(request, 'products/ms.html', {'mss': mss})


def windowsill(request):
    windowsill_1 = Windowsill.objects.all()
    return render(request, 'products/windowsill.html', {'windowsill_1': windowsill_1})


def otliv(request):
    otlivs = Otliv.objects.all()
    return render(request, 'products/otliv.html', {' otlivs':  otlivs})


def other(request):
    return render(request, 'products/other.html')


def callback(request):
    return render(request, 'products/callback.html')
