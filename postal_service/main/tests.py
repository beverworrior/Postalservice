from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import PostalRecord
# Create your tests here.
class PostalRecordTestCase(TestCase):
    def setUp(self):
        PostalRecord.objects.create(
            sender="Alice",
            recipient="Bob",
            address="123 Main St",
            postal_code="12345"
        )

    def test_postal_record_creation(self):
        record = PostalRecord.objects.get(sender="Alice")
        self.assertEqual(record.recipient, "Bob")
        self.assertEqual(record.address, "123 Main St")