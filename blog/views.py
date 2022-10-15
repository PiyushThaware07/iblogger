from django.shortcuts import render
from . models import Blogs,Category
from websites.models import About
# Paginator 
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    aboutus = About.objects.all()[0:40]
    blog = Blogs.objects.all()

    # Paginator
    paginator = Paginator(blog, 4)
    page_number = request.GET.get('page')
    blog = paginator.get_page(page_number)
    totalPages = blog.paginator.num_pages

    recent = Blogs.objects.all().order_by('-timeStamp')
    cat = Category.objects.all()
    context = {'catkey':cat,'recentkey':recent,'blogkey':blog,'changePages':[n+1 for n in range(totalPages)],'about':aboutus}
    return render(request, 'blog/index.html',context)

def ReadCat(request,id):
    allCats = Category.objects.all()
    cats = Category.objects.get(cat_id=id) 
    blog = Blogs.objects.filter(category=cats) 

    paginator = Paginator(blog, 4)
    page_number = request.GET.get('page')
    blog = paginator.get_page(page_number)
    totalPages = blog.paginator.num_pages

    context = {'catkey':cats,'blogkey':blog,'allcats':allCats,'changePages':[n+1 for n in range(totalPages)]}
    return render(request, 'blog/ReadCat.html',context)

def blogPost(request,slug):
    post = Blogs.objects.filter(slug=slug).first()
    allCats = Category.objects.all()
    mydict = {'post':post,'allcats':allCats}
    return render(request, 'blog/blogPost.html',mydict)     