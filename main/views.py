from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    return HttpResponse('Welcome to my World.')

def index(request):
    return HttpResponse("This page is for...")
