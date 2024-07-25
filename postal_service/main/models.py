from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostalRecord(models.Model):
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50, default='Unknown')
    country = models.CharField(max_length=50, default='Unknown')
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} to {self.recipient}'

class Shipment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    postal_record = models.ForeignKey(PostalRecord, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    tracking_number = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Shipment {self.tracking_number} - {self.status}'