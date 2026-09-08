from django.shortcuts import render

# Create your views here.
from main.models import Experience


def show_main(request):
    context = {
        "name": "Muhammad Taufiq Ramadhan",
        "npm": "2506536143",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at Universitas Indonesia. Learning, building, and figuring things out along the way."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Muhammad Taufiq Ramadhan",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
