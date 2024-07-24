from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import PostalRecord, Shipment
from django.contrib.auth.forms import AuthenticationForm
from .forms import ShipmentForm, CustomUserCreationForm
# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def postal_services(request):
    records = PostalRecord.objects.all()
    return render(request, 'main/postal_services.html', {'records': records})

@login_required
def shipment_status(request):
    shipments = Shipment.objects.filter(user=request.user)
    return render(request, 'main/shipment_status.html', {'shipments': shipments})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shipment_status')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def add_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment = form.save(commit=False)
            shipment.user = request.user
            shipment.save()
            return redirect('shipment_status')
    else:
        form = ShipmentForm()
    return render(request, 'main/add_shipment.html', {'form': form})

@login_required
def update_shipment(request, pk):
    shipment = Shipment.objects.get(pk=pk)
    if request.method == 'POST':
        form = ShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return redirect('shipment_status')
    else:
        form = ShipmentForm(instance=shipment)
    return render(request, 'main/update_shipment.html', {'form': form})