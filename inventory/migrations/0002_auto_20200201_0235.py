# Generated by Django 3.0.2 on 2020-01-31 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Available',
            new_name='is_available',
        ),
    ]
