from django.urls import path

from .views import index, route_link, create_link

urlpatterns = [
    path("", index, name="home"),
    path("<str:link_slug>/", route_link, name="route-link"),
    path("link/create/", create_link, name="create-link"),
]
