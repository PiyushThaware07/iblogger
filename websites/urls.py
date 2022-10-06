from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    # Url mapping
    path('about',views.about,name='about-index'),
    path('contact',views.contact,name='contact-index'),
    path('code',views.code,name='code-index'),
]