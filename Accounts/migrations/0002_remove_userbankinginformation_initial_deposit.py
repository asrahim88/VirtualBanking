# Generated by Django 5.1.3 on 2024-11-21 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbankinginformation',
            name='initial_deposit',
        ),
    ]
