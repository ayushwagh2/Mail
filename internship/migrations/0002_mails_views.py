# Generated by Django 4.1.2 on 2023-03-09 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mails',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
