from django.shortcuts import render
from .models import Projects
# Create your views here.

def home_view(request):
    context = {}

    projects = Projects.objects.all()

    context['projects']=projects

    return render(request, 'home.html', context)