from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="blog-index"),
    path('<str:slug>',views.blogPost,name="blogPost"),
    path('cat/<int:id>/',views.ReadCat,name="blog-cat"),
]