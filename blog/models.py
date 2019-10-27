from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name_en = models.CharField(max_length=100,verbose_name="Name EN",null=False, unique=True)
    name_es = models.CharField(max_length=100,verbose_name="Name ES",null=False, unique=True)   
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ['created']
    
    def __str__(self):
        return self.name_en

class Post(models.Model):
    title_en = models.CharField(max_length=200, verbose_name="Title EN")
    title_es = models.CharField(max_length=200, verbose_name="Title ES")
    content_en = RichTextField(verbose_name="Content EN")
    content_es = RichTextField(verbose_name="Content ES")
    published = models.DateField(verbose_name="Published", default=now)
    views = models.IntegerField(verbose_name="Visits", default=0)
    image = models.ImageField(verbose_name="Image", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name=("Author"), on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categories", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ['-created']
    
    def __str__(self):
        return self.title_en