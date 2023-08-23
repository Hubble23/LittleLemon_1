from django.test import TestCase
from restaurant.views import Menu



class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="fish", price=12)
        self.assertEqual("fish : 12")
       
        