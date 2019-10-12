from django.db import models
from django.utils.timezone import now
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField

class WorkTeam(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name",null=False)
    lastname = models.CharField(max_length=200, verbose_name="LastName",null=False) # Personel Name
    job = models.CharField(max_length=200, verbose_name="Job")
    info = RichTextField(verbose_name="Info") # Info about him or her
    phone_number = PhoneNumberField(verbose_name="Phone Number",null=False, blank=False, unique=True)
    email = models.EmailField(verbose_name="Email", max_length=254, default=False)
    photo = models.ImageField(verbose_name="Photo", upload_to="our_team") # Image of him or her
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    class Meta:
        verbose_name = "Associates"
        verbose_name_plural = "Work Team"
        ordering = ['-created']

    def __str__(self):
        return self.name    

class Who_We_Are(models.Model):
    title = models.CharField(verbose_name="Who We Are",default="Who We Are",editable=False, max_length=150)
    content = RichTextField(verbose_name="Content")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    class Meta:
        verbose_name = "Who we are"
        verbose_name_plural = "Who we are"
    
    def __str__(self):
        return self.title