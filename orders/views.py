from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .forms import OrderForm
from cart.models import Item,Cart
from .models import OrderedProducts,Order
# Create your views here.

def checkout(request):
    if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                print(form.instance.id)
                form.save()
                print(form.instance.id)
                cart = Cart.objects.get(user=request.user.id)
                item = Item.objects.filter(cart=cart.id)
                for i in item:
                    op = OrderedProducts(order=form.instance,product=i.product)
                    op.save()
                    i.delete()
                    return HttpResponse ("You ordered succesfully !")
                    print(op)
    cart = Cart.objects.get(user=request.user.id)
    item = Item.objects.filter(cart=cart.id)
    if item.exists():
        suma = 0
        for i in item:
            suma = suma + i.product.price
        form = OrderForm(initial = {'full_price':suma})
        context = {
            "form":form
        }
        template = loader.get_template("checkout.html")
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponse("Your cart is empty and you can't order !")

def manage(request):
    if request.user.is_superuser:
        order = Order.objects.all()
        op = OrderedProducts.objects.all()
    context = {
        "order":order,
        "op":op
    }
    template = loader.get_template("manage.html")

    return HttpResponse(template.render(context,request))

def order_details(request,id):
    if request.user.is_superuser:
        if request.method =="POST":
            id = request.POST["id"]
            order = Order.objects.get(id=id)
            order.delete()
            op = OrderedProducts.objects.filter(order=id)
            op.delete()
            return HttpResponseRedirect("manage")
        order = Order.objects.get(id=id)
        ordered_products = OrderedProducts.objects.filter(order=order.id)
        context = {
            "order":order,
            "op":ordered_products
        }
        template = loader.get_template("details.html")
        return HttpResponse(template.render(context,request))
    
    else:
        return HttpResponse("<h1>You are not allowed to access this page !</h1>")


