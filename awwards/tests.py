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

class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.awwward= Project()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.awwward,Project))

    # Testing Save Method
    def test_save_method(self):
        self.awwward.save_image()
        description= Project.objects.all()
        self.assertTrue(len(description) > 0)
