# Generated by Django 3.2.10 on 2021-12-30 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20211230_2111'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Todo_Model',
        ),
    ]