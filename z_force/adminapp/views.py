from django.shortcuts import render
from django.http import HttpResponse


def hello_Z(request):
    return HttpResponse("Hello, Z-Force!")


def check_kwargs(request, **kwargs):
    return HttpResponse(f"kwargs:<br>{kwargs}")



