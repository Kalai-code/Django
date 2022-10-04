from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello There")

def echo_hello(request):
    return render(request,"hello.html")

def echo_name(request):
    return render(request, "helloname.html", {'name':'Kalai'})
