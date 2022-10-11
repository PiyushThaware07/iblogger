from django.shortcuts import render,HttpResponse
from blog.models import Category,Blogs
from .models import Contact
# Messages
from django.contrib import messages

# Create your views here.
def home(request):
    cats = Category.objects.all()
    context = {'cats':cats}
    return render(request, 'websites/home.html',context)

def about(request):
    return render(request, 'websites/about.html')

def contact(request):
    cats = Category.objects.all()
    context = {'cats':cats}
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')

        if len(name)<2 or len(email)<3:
            messages.error(request, "Please fill the form correctly")

        else:
            contact=Contact(name=name, email=email,msg=msg)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'websites/contact.html',context)

def code(request):
    return HttpResponse("code")

def search(request):

    cats = Category.objects.all()
    search_item = request.GET.get('query')
    if len(search_item) > 50:
        blog = Blogs.objects.none()
    else:
        blogTitle = Blogs.objects.filter(title__icontains = search_item)
        blogContent = Blogs.objects.filter(content__icontains = search_item)
        blogAuthor = Blogs.objects.filter(author__icontains = search_item)
        blog = blogTitle.union(blogContent,blogAuthor)

    if blog.count() == 0:
        messages.error(request, "Please fill the search correctly")
    dict = {'allPosts':blog,'query':search_item,'cats':cats}
    return render(request, 'websites/search.html',dict)