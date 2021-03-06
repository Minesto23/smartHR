# Generated by Django 2.2.6 on 2019-10-07 08:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Subtitle')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('image', models.ImageField(upload_to='services', verbose_name='Image')),
                ('icon', models.ImageField(upload_to='services', verbose_name='Icon')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ['-created'],
            },
        ),
    ]
