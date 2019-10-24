# Generated by Django 2.2.6 on 2019-10-22 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_auto_20191021_1230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='model_quote',
            options={'ordering': ['day_code'], 'verbose_name': 'Quote Model', 'verbose_name_plural': 'Quotes Models'},
        ),
        migrations.AlterField(
            model_name='quote',
            name='phone_number',
            field=models.CharField(max_length=200, verbose_name='Phone Number'),
        ),
    ]
