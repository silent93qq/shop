# Generated by Django 2.2 on 2019-05-08 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='Product',
            new_name='product',
        ),
    ]
