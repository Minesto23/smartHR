from django.db import models
from ckeditor.fields import RichTextField

# Create your models here
class Question(models.Model):
    question = models.CharField(max_length=200, verbose_name="Question")
    content = RichTextField(verbose_name="Content")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['-created']

    def __str__(self):
        return self.question