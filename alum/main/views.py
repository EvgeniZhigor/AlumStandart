from django.shortcuts import render


def index(request):
    return render(request,'main/index.html')


def contact(request):
    return render(request,'main/contact.html')


def payment(request):
    return render(request,'main/payment.html')
