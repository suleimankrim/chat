# Generated by Django 4.0.4 on 2022-05-02 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_roommodel_last_message_alter_roommodel_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommodel',
            name='room_name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]