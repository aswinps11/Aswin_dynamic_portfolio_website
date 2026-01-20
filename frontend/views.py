from django.shortcuts import render, get_object_or_404
from .models import Portfolio, Service
from backend.models import HomeContent,Project

def index(request):
    # Get the home content from backend
    content, created = HomeContent.objects.get_or_create(id=1, defaults={'name': 'Your Name', 'role': 'Your Role'})
    projects = Project.objects.all().order_by('-id')
    return render(request, 'frontend/index.html', {
        'home_content': content, 
        'skills': content.skills.all(), 
        'resume': content.resume,
        'educations': content.educations.all(),
        'experiences': content.experiences.all(),
        'projects': projects,
    })

def portfolio_details(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    return render(request, 'frontend/portfolio-details.html', {'portfolio': portfolio})

def service_details(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'frontend/service-details.html', {'service': service})

def privacy(request):
    return render(request, 'frontend/privacy.html')

def terms(request):
    return render(request, 'frontend/terms.html')

def starter_page(request):
    return render(request, 'frontend/starter-page.html')
