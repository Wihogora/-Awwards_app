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

@login_required(login_url='/accounts/login/')
def single_image(request,image_id):
	image = image.objects.get(id= image_id)

	return render(request, 'profile/single_image.html',{"image":image})


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search_image.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_image.html',{"message":message})


@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user 
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                requested_profile.profile_pic = form.cleaned_data['profile_pic']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.username = form.cleaned_data['username']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()
    except:
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(profile_pic = form.cleaned_data['profile_pic'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()


    return render(request,'upload_profile.html',{"title":title,"current_user":current_user,"form":form})
