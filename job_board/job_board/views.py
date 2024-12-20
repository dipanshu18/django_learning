from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest

from .models import JobPosting


def index(request: HttpRequest):
    jobs = JobPosting.objects.filter(is_active=True)
    context = {"jobs": jobs}
    return render(request, "job_board/index.html", context=context)


def job_detail(request: HttpRequest, id: int):
    job = get_object_or_404(JobPosting, id=id, is_active=True)
    context = {"job": job}
    return render(request, "job_board/details.html", context=context)
