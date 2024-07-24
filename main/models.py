from django.db import models

# Create your models here.
class PostalRecord(models.Model):
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} to {self.recipient}'