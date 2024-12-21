from django.urls import path

from .views import (
    LinkListView,
    CreateLinkView,
    UpdateLinkView,
    DeleteLinkView,
    profile_view,
)

urlpatterns = [
    path("", LinkListView.as_view(), name="link-list"),
    path("create/", CreateLinkView.as_view(), name="add-link"),
    path("update/<int:pk>", UpdateLinkView.as_view(), name="update-link"),
    path("delete/<int:pk>", DeleteLinkView.as_view(), name="delete-link"),
    path("<slug:profile_slug>", profile_view, name="profile"),
]
