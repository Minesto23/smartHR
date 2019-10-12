# Generated by Django 2.2.6 on 2019-10-12 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['created'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Visits'),
        ),
    ]
