# Generated by Django 4.1.3 on 2022-11-05 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0007_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advocate',
            name='owner',
        ),
    ]