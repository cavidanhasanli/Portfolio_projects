from django.shortcuts import render
from .models import *


# Create your views here.

def about_view(request):
    context = {
        'general_info': GeneralModel.objects.all().first()
    }
    return render(request, 'about.html', context)


def skills_view(request):
    context = {
        'general_info': GeneralModel.objects.all().first(),
        'skills_general': SkillsModel.objects.all().first(),
        'job_skills': JobSkills.objects.all()
    }
    return render(request, 'skills.html',context)

def experience_view(request):
    context = {
        'general_info': GeneralModel.objects.all().first(),
        'experience': ExperienceModel.objects.all()
    }
    return render(request, 'experience.html', context)


def education_view(request):
    context = {
        'general_info': GeneralModel.objects.all().first(),
        'education': EducationModel.objects.all()
    }
    return render(request, 'education.html', context)


def portfolio_view(request):
    context = {
        'general_info': GeneralModel.objects.all().first(),
        'projects': PortfolioModel.objects.all()

    }
    return render(request, 'portfolio.html', context)