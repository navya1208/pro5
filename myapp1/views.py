from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def child(request):
    return render(request,"child.html")

def home(request):
  return render(request,"myapp1/home.html",{'name':"Navya"})

def base(request):
  return render(request,"myapp1/base.html")