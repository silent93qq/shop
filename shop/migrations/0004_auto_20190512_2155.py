# Generated by Django 2.2 on 2019-05-12 17:55

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190512_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='text',
            field=tinymce.models.HTMLField(default='', max_length=100000, verbose_name='Описание'),
        ),
    ]
