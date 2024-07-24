from django.urls import path
from .views import home, about, postal_services

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('postal_services/', postal_services, name='postal_services'),
]
