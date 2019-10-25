# Generated by Django 2.2.6 on 2019-10-21 13:42

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model_Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('lastname', models.CharField(max_length=200, verbose_name='LastName')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone Number')),
                ('email', models.EmailField(default=False, max_length=254, verbose_name='Email')),
                ('date', models.DateField(verbose_name='Date')),
                ('turn', models.CharField(max_length=200, verbose_name='Turn')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
            ],
            options={
                'verbose_name': 'Quote Model',
                'verbose_name_plural': 'Quotes Models',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Turns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Turn')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
            ],
            options={
                'verbose_name': 'Turn',
                'verbose_name_plural': 'Turns',
                'ordering': ['created'],
            },
        ),
    ]