from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def Index(Request):
    return render(Request,"index.html")

def detail(Request,post_id):
    return render(Request,"detail.html")

def username(Request):
    return HttpResponse("this is username page")

def old_url(Request):
    return redirect("new_url")

def new_url(Request):
    return HttpResponse("This is the new URL")

