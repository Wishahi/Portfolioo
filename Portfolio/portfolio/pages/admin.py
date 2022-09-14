from django.contrib import admin

# Register your models here.
from .models import Information


# Register your models here.

admin.site.register(Information)
list_display =('id', 'uni_name', 'degree', 'grade', 'place', 'year')