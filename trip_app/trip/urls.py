from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    HomeView,
    trip_list,
    TripCreateView,
    TripDetailView,
    TripUpdateView,
    TripDeleteView,
    TripNoteCreateView,
    TripNoteUpdateView,
    TripNoteDeleteView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard/", trip_list, name="trip-list"),
    path("dashboard/trip/create/", TripCreateView.as_view(), name="add-trip"),
    path("dashboard/trip/<int:pk>/", TripDetailView.as_view(), name="trip-detail"),
    path(
        "dashboard/trip/<int:pk>/update/", TripUpdateView.as_view(), name="trip-update"
    ),
    path(
        "dashboard/trip/<int:pk>/delete/", TripDeleteView.as_view(), name="trip-delete"
    ),
    path("dashboard/note/add/", TripNoteCreateView.as_view(), name="add-note"),
    path(
        "dashboard/note/<int:pk>/update/",
        TripNoteUpdateView.as_view(),
        name="update-note",
    ),
    path(
        "dashboard/note/<int:pk>/delete/",
        TripNoteDeleteView.as_view(),
        name="delete-note",
    ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
