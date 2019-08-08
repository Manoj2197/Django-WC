from django.http import HttpResponse
from django.shortcuts import render

def show(request):
    return HttpResponse("Have A Good Day")
def welcome(request):
    return HttpResponse("Welcome")