# Generated by Django 4.0.4 on 2022-05-29 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.CharField(max_length=500, null=True),
        ),
    ]