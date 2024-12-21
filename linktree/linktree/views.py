from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest

from .models import Profile, Link


class LinkListView(ListView):
    model = Link


class CreateLinkView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy("link-list")


class UpdateLinkView(UpdateView):
    model = Link
    fields = ["name", "url"]
    success_url = reverse_lazy("link-list")


class DeleteLinkView(DeleteView):
    model = Link
    success_url = reverse_lazy("link-list")


def profile_view(request: HttpRequest, profile_slug: str):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()

    context = {"profile": profile, "links": links}

    return render(request, "linktree/profile.html", context)
