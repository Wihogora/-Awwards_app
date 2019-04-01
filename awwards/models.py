from django.db import models
from django.conf import settings
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


class Projects(models.Model):
        title = models.CharField(User, max_length=200)
        image1 = ImageField(manual_crop='1280x720')
        image2 = ImageField(null=True, manual_crop='1280x720')
        image3 = ImageField(null=True, manual_crop='1280x720')
        decription = models.TextField(max_length=200)
        link = models.URLField(null=True, blank=True, default='')
        user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="images")

        @classmethod
        def get_all_projects(cls):
            projects = Projects.objects.all()
            return projects

        @classmethod
        def get_post(cls, id):
            projects = Projects.objects.filter(user=id)
            return projects

        class Meta:
            ordering = ['-id']

        def __str__(self):
            return self.title

class Rating(models.Model):
        design = models.IntegerField(blank=True, default=0)
        usability = models.IntegerField(blank=True, default=0)
        content = models.IntegerField(blank=True, default=0)
        overall_score = models.IntegerField(blank=True, default=0)
        project = models.ForeignKey(Project, on_delete=models.CASCADE)
        profile = models.ForeignKey(profile, on_delete=models.CASCADE)