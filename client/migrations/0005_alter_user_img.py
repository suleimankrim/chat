# Generated by Django 4.0.4 on 2022-05-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_alter_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]