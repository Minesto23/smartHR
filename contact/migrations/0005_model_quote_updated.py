# Generated by Django 2.2.6 on 2019-10-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_quote_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_quote',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
    ]
