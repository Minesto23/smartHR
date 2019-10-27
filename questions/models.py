from django.db import models
from ckeditor.fields import RichTextField

# Create your models here
class Question(models.Model):
    question_en = models.CharField(max_length=200, verbose_name="Question EN")
    question_es = models.CharField(max_length=200, verbose_name="Question ES")
    content_en = RichTextField(verbose_name="Content EN")
    content_es = RichTextField(verbose_name="Content ES")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['-created']

    def __str__(self):
        return self.question_en