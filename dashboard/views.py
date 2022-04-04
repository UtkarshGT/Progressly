from django.http import HttpResponse
from django.shortcuts import render

def explore(request):
    return HttpResponse("Explore")