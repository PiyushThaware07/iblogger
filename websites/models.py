from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    content = RichTextField()



class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    msg = models.TextField()

    def __str__(self):
        return self.name

