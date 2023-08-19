from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="fish", price=12, inventory=5)
        self.assertEqual(item, "fish : 12")
        
        
#class MenuViewTest(TestCase):
    #def setUp(self):
        
