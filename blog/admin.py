from django.contrib import admin

# Register your models here.
from . models import Blogs,Category
admin.site.register(Category)
admin.site.register(Blogs)

