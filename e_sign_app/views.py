from django.shortcuts import render, redirect
from django.http import HttpResponse
import base64

def index(request):
    return render(request, 'index.html')
