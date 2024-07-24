from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Shipment, PostalRecord

class PostalRecordForm(forms.ModelForm):
    class Meta:
        model = PostalRecord
        fields = ['sender', 'recipient', 'address', 'postal_code', 'city', 'country', 'weight', 'description']

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['postal_record', 'status', 'tracking_number']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']