from django.shortcuts import render
from django.http import HttpResponse

def firstname(request):
    return HttpResponse('MY NAME IS NAGATEJA')

def second(request):
    return HttpResponse('I COMPLETED MY BTECH IN MECHANICAL')