from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import logout
from .forms import RegForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
    form = RegForm()    
    template = loader.get_template("register.html")
    return HttpResponse(template.render({"form":form},request))

def log_out(request):
    logout(request)
    return redirect('index')


