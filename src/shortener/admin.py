from django.contrib import admin

# Register your models here.

#Relative import

from .models import KirrURL


admin.site.register(KirrURL)