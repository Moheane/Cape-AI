from django.shortcuts import render
from .models import personal_details
import redis


# Create your views here.
def HomePage(request):
    return render(request, 'portfolio/home.html',)

def AboutPage(request):
  
    context = { 
        'personal_details' : personal_details.objects.all()
     }
    return render(request, 'portfolio/about.html', context)
