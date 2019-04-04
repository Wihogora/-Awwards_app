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


class Project(models.Model):
        title = models.CharField( max_length=200,null = True)
        image = models.ImageField(upload_to = "images/",null = True)
        description = models.TextField(max_length=200)
        link = models.URLField(null=True, blank=True, default='')
        user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="images")

       
        def __str__(self):
            return self.title

        def delete_image(self):
            self.delete()

        def save_image(self):
            self.save()

        def update_description(self,new_description):
            self.image_description = new_description
            self.save()
        @classmethod
        def all_images(cls):
            image = cls.objects.all()
            return image 


        @classmethod
        def get_image(cls, id):
            image = cls.objects.get(id=id)
            return image

        @classmethod
        def search_by_title(cls,search_term):
            project = cls.objects.filter(title__icontains = search_term)
            return project

    # class Meta:
    #     ordering = ['-pub_date']
class Rates(models.Model):
        design = models.IntegerField(blank=True, default=0)
        usability = models.IntegerField(blank=True, default=0)
        content = models.IntegerField(blank=True, default=0)
        overall_score = models.IntegerField(blank=True, default=0)
        project = models.ForeignKey(Project, on_delete=models.CASCADE)
        profile = models.ForeignKey(Profile, on_delete=models.CASCADE)