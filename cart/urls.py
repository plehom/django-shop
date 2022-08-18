from django.urls import path
from . import views

urlpatterns = [
    path("",views.cart,name="cart"),
    path("add/",views.add_to_cart,name="add_to_cart")
]
