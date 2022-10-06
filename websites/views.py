from django.shortcuts import render,HttpResponse
from blog.models import Category

# Create your views here.
def home(request):
    cats = Category.objects.all()
    context = {'cats':cats}
    return render(request, 'websites/home.html',context)

def about(request):
    return render(request, 'websites/about.html')

def code(request):
    return render(request, 'websites/code.html')