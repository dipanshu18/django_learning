from django.urls import path
from .views import index, job_detail

urlpatterns = [
    path("", index, name="home"),
    path("<int:id>/", job_detail, name="detail"),
]
