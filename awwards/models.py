from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
        username = models.CharField(default='User',max_length=40)
        profile_pic = models.ImageField(upload_to = "profile/",null=True)
        bio = models.TextField(default='',blank = True)
        user_project = models.CharField(max_length =40)
        user_contact = models.CharField(max_length =40)


        def __str__(self):
            return self.username

        def delete_profile(self):
            self.delete()

        def save_profile(self):
            self.save()

        @classmethod
        def search_profile(cls,search_term):
            got_profiles = cls.objects.filter(user_project__icontains = search_term)
            return got_profiles

