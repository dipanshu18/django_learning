from django.shortcuts import render, HttpResponse
from django.http import HttpRequest


# Create your views here.
def index(request: HttpRequest):
    return HttpResponse("Hello, world!")


def article(request: HttpRequest, id: int):
    return HttpResponse(f"The article id: {id}")


def add(request: HttpRequest, num1: int, num2: int):
    return HttpResponse(f"The sum of {num1} + {num2} = {num1 + num2}")
