# Generated by Django 4.1 on 2022-11-15 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0012_alter_accountmodel_image_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountmodel',
            name='image_profile',
        ),
    ]