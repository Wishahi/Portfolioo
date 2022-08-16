from django.contrib import admin
from .models import AnimalProfile, FamilyProfile

# Register your models here.
admin.site.register(AnimalProfile)
admin.site.register(FamilyProfile)