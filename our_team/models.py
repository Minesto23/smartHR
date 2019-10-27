from django.db import models
from django.utils.timezone import now
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField

class WorkTeam(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name",null=False)
    lastname = models.CharField(max_length=200, verbose_name="LastName",null=False) # Personel Name
    job_en = models.CharField(max_length=200, verbose_name="Job EN", null=False)
    job_es = models.CharField(max_length=200, verbose_name="Job ES", null=False)
    info_en = RichTextField(verbose_name="Info EN", null=False) # Info about him or her
    info_es = RichTextField(verbose_name="Info ES", null=False) # Info about him or her
    phone_number = models.CharField(verbose_name="Phone Number", max_length=100,null=False, blank=False, unique=True)
    email = models.EmailField(verbose_name="Email", max_length=254, default=False)
    photo = models.ImageField(verbose_name="Photo", upload_to="our_team", null=False) # Image of him or her
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    class Meta:
        verbose_name = "Associates"
        verbose_name_plural = "Work Team"
        ordering = ['-created']

    def __str__(self):
        return str(self.name+" "+self.lastname)    

class Who_We_Are(models.Model):
    title = models.CharField(verbose_name="Who We Are",default="Who We Are",editable=False, max_length=150)
    content_en = RichTextField(verbose_name="Content EN", default="")
    content_es = RichTextField(verbose_name="Content ES", default="")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    class Meta:
        verbose_name = "Who we are"
        verbose_name_plural = "Who we are"
    
    def __str__(self):
        return self.title