from django.shortcuts import render
from . models import Blogs,Category

# Create your views here.
def index(request):
    blog = Blogs.objects.all()
    print(blog)
    recent = Blogs.objects.all().order_by('-timeStamp')
    cat = Category.objects.all()
    context = {'catkey':cat,'blogkey':blog,'recentkey':recent}
    return render(request, 'blog/index.html',context)

def ReadCat(request,id):
    allCats = Category.objects.all()
    cats = Category.objects.get(cat_id=id) 
    blog = Blogs.objects.filter(category=cats)  
    context = {'catkey':cats,'blogkey':blog,'allcats':allCats}
    return render(request, 'blog/ReadCat.html',context)

def blogPost(request,slug):
    post = Blogs.objects.filter(slug=slug).first()
    allCats = Category.objects.all()
    mydict = {'post':post,'allcats':allCats}
    return render(request, 'blog/blogPost.html',mydict)     