from django.shortcuts import render
from .models import *


# Create your views here.

def about_view(request):
    context = {
        'general_info': GeneralModel.objects.all().first(),
        "activate":"active"
    }
    return render(request, 'about.html', context)


def skills_view(request):
    context = {
        'general_info': GeneralModel.objects.all().first(),
        'skills_general': SkillsModel.objects.all().first(),
        'job_skills': JobSkills.objects.all(),
        "activate_skills":"active"
    }
    return render(request, 'skills.html',context)

def experience_view(request):
    context = {
        'general_info': GeneralModel.objects.all().first(),
        'experience': ExperienceModel.objects.all(),
        'activate_ex':"active"
    }
    return render(request, 'experience.html', context)


def education_view(request):
    context = {
        'general_info': GeneralModel.objects.all().first(),
        'education': EducationModel.objects.all(),
        'activate_edu': "active"
    }
    return render(request, 'education.html', context)


def portfolio_view(request):
    context = {
        'general_info': GeneralModel.objects.all().first(),
        'projects': PortfolioModel.objects.all(),
        'activate_port': "active"

    }
    return render(request, 'portfolio.html', context)