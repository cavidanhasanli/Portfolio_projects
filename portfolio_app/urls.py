from django.urls import path
from .views import *
urlpatterns = [
    path('', about_view, name='about_url'),
    path('skills/', skills_view, name='skills_url'),
    path('experience/', experience_view, name='experience_url'),
    path('education/', education_view, name='education_url'),
    path('portfolio/', portfolio_view, name='portfolio_url'),
]