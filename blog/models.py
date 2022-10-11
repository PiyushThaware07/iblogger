from django.db import models
# ckeditor
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    
    img = models.ImageField(default="")

    author = models.CharField(max_length=20,blank=True,default="Unknown")
    publish_date = models.DateField(auto_now=True)

    # category = models.CharField(max_length=100,null=True,default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #error occurs then commit and create new migrations
    readtime = models.IntegerField(default=10)

    slug = models.CharField(max_length=40)

    timeStamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title+" by "+self.author
    