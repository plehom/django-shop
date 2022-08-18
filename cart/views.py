from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Cart,Item
from django.contrib.auth.models import User
from main.models import Product

# Create your views here.

def cart(request):
    if request.user.is_authenticated:
        usr = User.objects.get(id=request.user.id)
        cart = Cart.objects.get(user=request.user.id)
        items = Item.objects.filter(cart=cart)
    else:
        return HttpResponse("You have to be logged in to access cart !")
    if request.method == 'POST':
        i = Item.objects.get(id=request.POST["id"])
        i.delete()
    template = loader.get_template("cart.html")
    return HttpResponse(template.render({"items":items},request))

def add_to_cart(request):
    pr_id = request.POST["id"]

    product = Product.objects.get(id=pr_id)
    cart = Cart.objects.get(user=request.user.id)
    item = Item(product = product,cart = cart)
    item.save()
    return HttpResponse("ok")