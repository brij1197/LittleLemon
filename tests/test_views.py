from django.test import TestCase
from restaurant.models import Menu
import json

class MenuViewTest(TestCase):
    def setup(self):
        item=Menu.objects.create(title="IceCream",price=80, inventory=100)
    def test_getall(self):
        self.assertEqual(json.dumps(Menu.objects.all()),"Icecream")