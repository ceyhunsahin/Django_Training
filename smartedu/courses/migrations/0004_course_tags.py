# Generated by Django 3.2.11 on 2022-01-12 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.Tag'),
        ),
    ]
