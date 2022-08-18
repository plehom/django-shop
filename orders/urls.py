from django.urls import path
from . import views

urlpatterns = [
    path('',views.checkout,name="checkout"),
    path('manage/',views.manage,name="manage"),
    path('details/<int:id>',views.order_details,name="details")
]


