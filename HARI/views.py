from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def HARI(request):
    return HttpResponse ('<h1> HARI IS A STUDENT </h1>')

def HARI1 (request):
    return HttpResponse ('<h1><marquee> HARI1 IS A MALE </marquee></h1>')

