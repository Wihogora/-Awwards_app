from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    
    url('^$',views.index, name='index'),
    url(r'^image/(\d+)', views.single_project, name='single_project'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^single_project/(\d+)', views.single_project, name='single_project'),
    url(r'^upload_project/', views.upload_project, name='upload_project'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^upload/profile', views.upload_profile, name='upload_profile'),


]

if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

