from django import forms
from django.forms import ModelForm
from .models import Profile, Projects, Rates


class ProfileForm(forms.ModelForm):
	model = Profile
	username = forms.CharField(label='Username',max_length = 30)
	
	bio = forms.CharField(label='Image Caption',max_length=500)
	profile_pic = forms.ImageField(label = 'Image Field')


class ProfileUploadForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		exclude = ['user']

# class ImageForm(forms.ModelForm):
# 	class Meta:
# 		model = Image
		
# 		exclude = ['user']

# class ImageUploadForm(forms.ModelForm):
# 	class Meta:
# 		model = Image
		
# 		exclude = ['user']

class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Projects

        fields = ['title', 'image', 'image2', 'image3', 'decription', 'link']
