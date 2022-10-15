from django.shortcuts import render,HttpResponse,redirect
from blog.models import Category,Blogs
from .models import Contact,About
# Messages
from django.contrib import messages
# Signup
from django.contrib.auth.models import User
# signin
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    aboutus = About.objects.all()
    print(aboutus)
    cats = Category.objects.all()
    context = {'cats':cats,'about':aboutus}
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

def signup(request):
    cats = Category.objects.all()

    if request.method=="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your Account has been Successfully created")
        return redirect('/signin')
    return render(request, 'websites/signup.html',{'cats':cats})  

def signin(request):
    cats = Category.objects.all()

    if request.method =="POST":
        username = request.POST.get('uname')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            fname = user.first_name
            messages.success(request,f"Login Successfull , Welcome back {fname}")
            return render(request,"websites/home.html",{'fname':fname})
        else:
            messages.error(request, 'Invalid Inputs')
            return redirect('/signin')    

    return render(request, 'websites/signin.html',{'cats':cats})

def signout(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return redirect('/')
    return HttpResponse("Signout") 