from django.contrib import admin

# Register your models here.
from . models import Contact,About
admin.site.register(Contact)
admin.site.register(About)