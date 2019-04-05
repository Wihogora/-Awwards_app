from django.test import TestCase
from .models import Project,Profile,Rates

# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.awwward= Profile( )
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.awwward,Profile))
