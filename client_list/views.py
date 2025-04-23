from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("this is where the list of clients go.")
