# Generated by Django 4.0.4 on 2022-05-03 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_messagemodel_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommodel',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
