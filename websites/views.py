from django.shortcuts import render,HttpResponse
from blog.models import Category
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