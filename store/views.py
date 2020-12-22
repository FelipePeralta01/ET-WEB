from django.shortcuts import redirect, render
#LOGIN
from django.contrib.auth import authenticate, login as login_, logout as logout_
from .models import *
#LISTVIEW
from django.views.generic.list import ListView
#FORMS
from .forms import *

def index(request):
    context = {}
    return render(request, 'index.html', context)


class mainstore(ListView):
    model = Product
    template_name = 'mainstore.html'
    paginate_by = 9
    context_object_name = 'products'

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

def login(request):
    context = {}
    if request.method == 'POST':
        if request.POST.get('accion') == 'Ingresar':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login_(request, user)
                return redirect('index')
    if request.user.is_authenticated:
        return redirect('cerrar_sesion')
    return render(request, 'login.html', context)

def cerrar_sesion(request):
    form = ProfuctForm()
    context = {
        'form':form
    }
    return render(request, 'cerrar_sesion.html', context)

def logout(request):
    logout_(request)
    return redirect('index')

class admin_products(ListView):
    model = Product
    template_name = 'admin_products.html'
    paginate_by = 9
    context_object_name = 'products'
    def post(self, request, *args, **kwargs):
        form = ProfuctForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('admin_products')

def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('admin_products')

def update_product(request, id):
    product = Product.objects.get(id=id)
    
    if request.method == 'POST':
        form_ = ProfuctForm(request.POST or None , instance=product)
        if form_.is_valid():
            form_.save()
    form = ProfuctForm(instance=product)
    context = {
        'form':form
    }
    return render(request, 'update_product.html',context)