# Generated by Django 2.2 on 2019-05-12 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190512_2349'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductInOrder',
        ),
    ]