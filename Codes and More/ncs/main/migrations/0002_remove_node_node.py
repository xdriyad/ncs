# Generated by Django 2.2.1 on 2019-12-15 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='node',
        ),
    ]
