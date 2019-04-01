from django.contrib import admin
from .models import Profile, Projects, Rates

# Register your models here.
admin.site.register(Profile)
admin.site.register(Projects)
admin.site.register(Rates)
