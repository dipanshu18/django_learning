from django import forms
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.http import HttpRequest

from .models import Trip, Note


class HomeView(TemplateView):
    template_name = "trip/index.html"


@login_required
def trip_list(request: HttpRequest):
    trips = Trip.objects.filter(owner=request.user)
    context = {"trips": trips}

    return render(request, "trip/trip_list.html", context)


class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    fields = ["city", "country", "start_date", "end_date"]
    success_url = reverse_lazy("trip-list")

    def get_form(self):
        form = super().get_form()
        # Add date input widgets for start_date and end_date
        form.fields["start_date"].widget = forms.DateInput(attrs={"type": "date"})
        form.fields["end_date"].widget = forms.DateInput(attrs={"type": "date"})
        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TripDetailView(LoginRequiredMixin, DetailView):
    model = Trip

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context["object"]
        notes = trip.notes.all()
        context["notes"] = notes
        return context


class TripUpdateView(LoginRequiredMixin, UpdateView):
    model = Trip
    fields = ["city", "country", "start_date", "end_date"]

    def form_invalid(self, form):
        note = form.save()
        trip_id = note.trip.id
        self.success_url = reverse_lazy("trip-detail", kwargs={"pk": trip_id})
        return super().form_invalid(form)


class TripDeleteView(LoginRequiredMixin, DeleteView):
    model = Trip
    success_url = reverse_lazy("trip-list")


class TripNoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = "__all__"

    def get_form(self):
        form = super(TripNoteCreateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields["trip"].queryset = trips
        return form

    def form_valid(self, form):
        note = form.save()
        trip_id = note.trip.id
        self.success_url = reverse_lazy("trip-detail", kwargs={"pk": trip_id})
        return super().form_valid(form)


class TripNoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = "__all__"

    def get_form(self):
        form = super(TripNoteUpdateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields["trip"].queryset = trips
        return form

    def form_valid(self, form):
        note = form.save()
        trip_id = note.trip.id
        self.success_url = reverse_lazy("trip-detail", kwargs={"pk": trip_id})
        return super().form_valid(form)


class TripNoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note

    def get_success_url(self):
        note = self.get_object()
        trip_id = note.trip.id

        return reverse_lazy("trip-detail", kwargs={"pk": trip_id})
