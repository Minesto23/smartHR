from django.db import models
from django.utils.timezone import now
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from django import forms



# Create your models here.
class Quote(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name",null=False)
    lastname = models.CharField(max_length=200, verbose_name="LastName",null=False)
    phone_number = models.CharField(verbose_name="Phone Number",null=False, blank=False, max_length=200)
    email = models.EmailField(verbose_name="Email", max_length=254, default=False)
    date = models.DateField(verbose_name="Date")
    turn = models.CharField(max_length=200, verbose_name="Turn")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(verbose_name="Updated Date", auto_now=True, auto_now_add=False)

    class Meta:
            verbose_name = "Quote"
            verbose_name_plural = "Quotes"
            ordering = ['-created']

    def __str__(self):
        return self.name   

class Turns(models.Model):
    name = models.CharField(verbose_name="Turn", max_length=200, unique=True)
    created = models.DateTimeField(verbose_name="Created Date", auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated Date", auto_now=True, auto_now_add=False)
    class Meta:
        verbose_name = "Turn"
        verbose_name_plural = "Turns"
        ordering = ['created']
    def __str__(self):
        return self.name
    

class Model_Quote(models.Model):
    day = models.CharField(max_length=200, verbose_name="Name",null=False)
    day_code = models.IntegerField(verbose_name="Code",default = 0)
    turn = models.ManyToManyField(Turns, verbose_name="Turns", related_name = "get_turns")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(verbose_name="Updated Date", auto_now=True, auto_now_add=False)
    
    class Meta:
            verbose_name = "Quote Model"
            verbose_name_plural = "Quotes Models"
            ordering = ['day_code']

    def __str__(self):
        return self.day  