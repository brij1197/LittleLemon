from django.test import TestCase
from restaurant.models import Menu,Booking
from datetime import datetime
from django.utils import timezone

class MenuTest(TestCase):
    def test_get_item(self):
        item=Menu.objects.create(title="IceCream",price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
        
class BookingTest(TestCase):
    def test_create_booking(self):
        booking=Booking.objects.create(
            name='Arthur',
            no_of_guests=4,
            bookingdate=datetime(2023, 10, 1, 18, 8, 7, 127325,timezone.utc)
        )
        self.assertEqual(str(booking),"Arthur")
        
    def test_default_name(self):
        booking = Booking.objects.create(
            no_of_guests=4,
            bookingdate=datetime(2023, 10, 1, 18, 8, 7, 127325,timezone.utc)
        )
        self.assertNotEqual(booking.name, "John")