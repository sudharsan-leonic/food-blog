# Generated by Django 3.2.4 on 2021-06-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default=None, upload_to='uploads/'),
        ),
    ]
