# Generated by Django 4.1 on 2022-11-15 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0015_alter_accountmodel_image_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='image_profile',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
