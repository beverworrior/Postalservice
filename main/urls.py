from django.urls import path
from .views import home, about, postal_services, shipment_status, user_login, user_logout, register, add_shipment, update_shipment


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('postal_services/', postal_services, name='postal_services'),
    path('shipment_status/', shipment_status, name='shipment_status'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('add_shipment/', add_shipment, name='add_shipment'),
    path('update_shipment/<int:pk>/', update_shipment, name='update_shipment'),
]
