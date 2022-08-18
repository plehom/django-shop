from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Product
from .forms import ProductForm
from cart.models import Cart
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        if Cart.objects.filter(user=request.user.id).exists():
            pass
        else:
            usr = User.objects.get(id=request.user.id)
            cart = Cart(user=usr)
            cart.save()
        if request.method == 'POST':
            product = Product.objects.get(id=request.POST["id"])
            product.delete()
    products = Product.objects.all()
    context = {
        "products":products
    }
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context,request))

def create(request):
    if request.user.is_superuser:

        template = loader.get_template("create.html")
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                
        form = ProductForm()
        context = {
            "form":form
        }
        return HttpResponse(template.render({"form":form},request))
    else:
        return HttpResponse(404)