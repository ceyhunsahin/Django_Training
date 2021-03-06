# Generated by Django 3.2.11 on 2022-01-14 23:55

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0002_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First Name', max_length=100)),
                ('last_name', models.CharField(help_text='Last Name', max_length=100)),
                ('email', models.EmailField(help_text=' Your Email', max_length=254)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('message', models.TextField()),
            ],
        ),
    ]
