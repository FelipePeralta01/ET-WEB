from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'index.html', context)

def mainstore(request):
    context = {}
    return render(request, 'mainstore.html', context)

def cart(request):
    context = {}
    return render(request, 'cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)

def profile(request):
    context = {}
    return render(request, 'profile.html', context)

def profileadmin(request):
    context = {}
    return render(request, 'profileadmin.html', context)

def register(request):
    context = {}
    return render(request, 'register.html', context)