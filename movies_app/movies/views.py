from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def index(request: HttpRequest):
    context = {
        "platforms": ["Netflix", "Amazon Prime", "Disney + Hotstar", "Hulu"],
        "genre": "Horror",
    }
    return render(request, "movies/index.html", context)


def about(request: HttpRequest):
    return render(request, "movies/about.html")
