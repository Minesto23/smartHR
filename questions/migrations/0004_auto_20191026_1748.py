# Generated by Django 2.2.6 on 2019-10-26 21:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20191026_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content_en',
            field=ckeditor.fields.RichTextField(verbose_name='Content EN'),
        ),
        migrations.AlterField(
            model_name='question',
            name='content_es',
            field=ckeditor.fields.RichTextField(verbose_name='Content ES'),
        ),
    ]
