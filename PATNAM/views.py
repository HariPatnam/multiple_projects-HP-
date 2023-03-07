from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def PATNAM(request):
    return HttpResponse ('PATNAM IS A HARI SURNAME')

def PATNAM1 (request):
    return HttpResponse ('<marquee> <h1> HARI PATNAM IS A BRAND </h1> <marquee>')
