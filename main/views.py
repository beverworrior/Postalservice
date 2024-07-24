from django.shortcuts import render
from .models import PostalRecord
# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def postal_services(request):
    records = PostalRecord.objects.all()
    return render(request, 'main/postal_services.html', {'records': records})
