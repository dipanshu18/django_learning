from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import HttpRequest
from django.urls import reverse

from .models import Link
from .forms import LinkForm


def index(request: HttpRequest):
    links = Link.objects.all()

    context = {"links": links}
    return render(request, "url_shortner/index.html", context=context)


def route_link(request: HttpRequest, link_slug: str):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()

    return redirect(link.url)


def create_link(request: HttpRequest):
    if request.method == "POST":
        form = LinkForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse("home"))
    else:
        form = LinkForm()

    context = {"form": form}
    return render(request, "url_shortner/create.html", context)
