# Generated by Django 3.2.9 on 2021-11-14 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mobile_number',
        ),
    ]
