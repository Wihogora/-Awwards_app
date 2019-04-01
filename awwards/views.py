from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Projects, Rates
from . forms import ProfileUploadForm,ProfileForm,ImageForm,ImageUploadForm,ProjectsForm
from django.http  import HttpResponse
from django.conf import settings

# Create your views here.
