from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Projects, Rates
from . forms import ProfileUploadForm,ProfileForm,ImageForm,ImageUploadForm,ProjectsForm
from django.http  import HttpResponse
from django.conf import settings

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    title = 'Awwards'
    image_posts = Image.objects.all()
   

    print(image_posts)
    return render(request, 'index.html', {"title":title,"image_posts":image_posts})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.all()
    
    return render(request, 'profile.html',{"current_user":current_user,"profile":profile})