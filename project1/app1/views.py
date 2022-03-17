from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
def home(response):
    return render(response, 'app1/templates/html.html')