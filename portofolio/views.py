from django.shortcuts import render


def landing_page(request):
    return render(request, "index.html")

def skill_page(request):
    return render(request, "skill.html")

def project_page(request):
    return render(request, "project.html")