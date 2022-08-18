
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('',include('main.urls')),
    path('register/',include('registration.urls')),
    path('cart/',include('cart.urls')),
    path('logout/',views.log_out, name="logout"),
    path('orders/',include('orders.urls'))
]
